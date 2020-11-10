import requests
import re
import json
"""
    组件功能：实现 SVG + CSS 解密
    1. 请求文件时不需要带headers，否则访问会出错
"""

headers = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'Accept-Encoding': 'gzip, deflate',
  'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
  'Connection': 'keep-alive',
  'Cookie': '_lxsdk_s=175afcb6881-d31-b45-097%7C%7C330; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1604972995; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1604972145; s_ViewType=10; ctu=aadae538ed0e2afd1824f1d232d874090ce0ba28fb118d894d7175d245b50dda; cy=2; cye=beijing; dper=f7a77db35082ebf93004d24c78a3fad8cbb4b1f70b53419431eb2eade85ace439dc242d5398ecc276af0d1f6486420a78e445d2ff52a9816cf8cf389a851918c1663c438a476e1f6e242a45f461ad6ddfd01d8863169a1f739b0dfd2c8a33c85; dplet=99c2caa8b18e5218272a2dbc0d76ddbe; ll=7fd06e815b796be3df069dec7836c3df; ua=16222525784; _hc.v=c384d451-6dcb-bb2d-9d47-1c7057de33c5.1604972145; _lxsdk=175afcb6880c8-0a738574374bb9-3e62694b-1aeaa0-175afcb6880c8; _lxsdk_cuid=175afcb6880c8-0a738574374bb9-3e62694b-1aeaa0-175afcb6880c8; fspop=test',
  'Host': 'www.dianping.com',
  'Upgrade-Insecure-Requests': '1',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:82.0) Gecko/20100101 Firefox/82.0',
}

""" 获取css """
r = requests.get("http://www.dianping.com/shop/k1F8YkiWg19LvoIJ/review_all", headers=headers)
print(r.text)
css_url = "http:" + re.findall('href="(//s3plus.meituan.net.*?svgtextcss.*?.css)"', r.text)[0]
css_content = requests.get(css_url)
""" 获取svg """
def svg_parser(url):
    """ 解析svg文件内容 """
    r = requests.get(url)
    font = re.findall('" y="(\d+)">(\w+)</text>', r.text, re.M)  # 获取每一行的y值和对应字体
    if not font:
        font = []
        z = re.findall('" textLength.*?(\w+)</textPath>', r.text, re.M)
        y = re.findall('id="\d+" d="\w+\s(\d+)\s\w+"', r.text, re.M)
        for a, b in zip(y, z):
            font.append((a, b))
    width = re.findall("font-size:(\d+)px", r.text, re.M)[0]
    new_font = []
    for i in font:
        new_font.append((int(i[0]), i[1]))
    return new_font, int(width)
""" 解析svg结果 """
svg_url = re.findall('class\^="(\w+)".*?(//s3plus.*?\.svg)', css_content.text)
s_parser = []
for c, u in svg_url:  # class - url
    f, w = svg_parser("http:" + u)  # font, width
    s_parser.append({"code": c, "font": f, "fw": w})
print(s_parser)
""" 从css获取所有class对应的xy坐标 """
css_list = re.findall('(\w+){background:.*?(\d+).*?px.*?(\d+).*?px;', '\n'.join(css_content.text.split('}')))
css_list = [(i[0], int(i[1]), int(i[2])) for i in css_list]
print(css_list)

""" 根据class坐标在svg中找到具体文字 """
# y是文字所在的行数（所在区间），x是字体的宽度
def font_parser(ft):
    for i in s_parser:
        if i['code'] in ft[0]:
            font = sorted(i['font'])
            if ft[2] < int(font[0][0]):  # class的y值小于最小的行数，则从第一行找
                x = int(ft[1]/i['fw'])
                return font[0][1][x]
            for j in range(len(font)):
                if (j+1) in range(len(font)):
                    if int(font[j][0]) <= ft[2] < int(font[j + 1][0]):
                        x = int(ft[1]/i['fw'])
                        return font[j+1][1][x]
""" 根据坐标，构建映射关系 """
replace_dict = []
for i in css_list:
    replace_dict.append({"code": '<svgmtsi class="' + i[0] + '"></svgmtsi>', "word": font_parser(i)})
print(replace_dict)

""" 存到本地 """
with open('svg_map.py', 'w', encoding='utf-8') as f:
    dict_str = json.dumps(replace_dict, ensure_ascii=False, indent=4)
    f.write('replace_map = ')
    f.write(dict_str)


