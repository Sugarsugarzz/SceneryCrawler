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
  'Cookie': 'navCtgScroll=0; fspop=test; cy=2; cye=beijing; _lxsdk_cuid=1756254e31dc8-0dbb2f5b84c02a-31687304-1aeaa0-1756254e31dc8; _lxsdk=1756254e31dc8-0dbb2f5b84c02a-31687304-1aeaa0-1756254e31dc8; _hc.v=a497ceb2-53d2-fcc1-b83f-acb8e5671083.1603672532; s_ViewType=10; ll=7fd06e815b796be3df069dec7836c3df; ua=13001230577; ctu=5fecefa74ea59558a4d9dddd24fb293b8f9710fb8079edab2e1f02e28d5987bd; aburl=1; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1603672532,1603678545,1603716657; dper=4e52a9b9cff46f80ab674682d9497fba11099b33878055f75b57fe88cd55ac9e9d19d806d3eba70159b2ce16671be5473c90efc872b265a7f3729faf8c63fe1823f8bfbadea35143b56dec8df4411daa4fb64ada22c830fba9ef0ddd3feac2fd; dplet=22e5ea91a601425747e58caf97295f43; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1603766818; _lxsdk_s=17567d81e0b-1c-baa-3f1%7C%7C829',
  'Host': 'www.dianping.com',
  'Upgrade-Insecure-Requests': '1',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
}

""" 获取css """
r = requests.get("http://www.dianping.com/shop/k1F8YkiWg19LvoIJ/review_all", headers=headers)
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


