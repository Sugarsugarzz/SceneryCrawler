# -*- coding:utf-8 -*-
from fontTools.ttLib import TTFont
import re
import json
from SceneryCrawler.utils.decrypt_map import number_map, chinese_map, chinese_other_map


""" 字符集 """
characters = list('1234567890店中美家馆小车大市公酒行国品发电金心业商司超生装园场食有新限天面工服海华水房饰城乐汽香部利子老艺花专东肉菜学福饭人百餐茶务通味所山区门药银农龙停尚安广鑫一容动南具源兴鲜记时机烤文康信果阳理锅宝达地儿衣特产西批坊州牛佳化五米修爱北养卖建材三会鸡室红站德王光名丽油院堂烧江社合星货型村自科快便日民营和活童明器烟育宾精屋经居庄石顺林尔县手厅销用好客火雅盛体旅之鞋辣作粉包楼校鱼平彩上吧保永万物教吃设医正造丰健点汤网庆技斯洗料配汇木缘加麻联卫川泰色世方寓风幼羊烫来高厂兰阿贝皮全女拉成云维贸道术运都口博河瑞宏京际路祥青镇厨培力惠连马鸿钢训影甲助窗布富牌头四多妆吉苑沙恒隆春干饼氏里二管诚制售嘉长轩杂副清计黄讯太鸭号街交与叉附近层旁对巷栋环省桥湖段乡厦府铺内侧元购前幢滨处向座下県凤港开关景泉塘放昌线湾政步宁解白田町溪十八古双胜本单同九迎第台玉锦底后七斜期武岭松角纪朝峰六振珠局岗洲横边济井办汉代临弄团外塔杨铁浦字年岛陵原梅进荣友虹央桂沿事津凯莲丁秀柳集紫旗张谷的是不了很还个也这我就在以可到错没去过感次要比觉看得说常真们但最喜哈么别位能较境非为欢然他挺着价那意种想出员两推做排实分间甜度起满给热完格荐喝等其再几只现朋候样直而买于般豆量选奶打每评少算又因情找些份置适什蛋师气你姐棒试总定啊足级整带虾如态且尝主话强当更板知己无酸让入啦式笑赞片酱差像提队走嫩才刚午接重串回晚微周值费性桌拍跟块调糕')


def create_dict(filepath):
    """ 构造解密词典 """
    dic = {}
    font = TTFont(filepath)
    keys = font.getGlyphOrder()
    for i in range(len(keys[2:])):
        key = keys[i+2].replace('uni', r'\u').encode('utf-8').decode('unicode_escape')
        dic[key] = characters[i]
    return dic


""" 构造映射词典，存到本地 """
def store_dict():
    number_dict = create_dict('fonts/74d35eb5.woff')
    chinese_dict = create_dict('fonts/ecfbd556.woff')
    chinese_other_dict = create_dict('fonts/f24322a8.woff')
    with open('decrypt_map.py', 'w', encoding='utf-8') as f:
        dict_str = json.dumps(number_dict, ensure_ascii=False, indent=4)
        f.write('number_map = ')
        f.write(dict_str)
        f.write('\n')
        dict_str = json.dumps(chinese_dict, ensure_ascii=False, indent=4)
        f.write('chinese_map = ')
        f.write(dict_str)
        f.write('\n')
        dict_str = json.dumps(chinese_other_dict, ensure_ascii=False, indent=4)
        f.write('chinese_other_map = ')
        f.write(dict_str)


def get_number(content):
    """ 解析数字类字符串 """
    return re.sub('[\ue000-\uffff]', lambda x: number_map.get(x.group(0), x.group(0)), content)


def get_chinese(content):
    """ 解析中文类字符串 """
    return re.sub('[\ue000-\uffff]', lambda x: chinese_map.get(x.group(0), x.group(0)), content)


def get_other_chinese(content):
    """ 解析中文2类字符串 """
    return re.sub('[\ue000-\uffff]', lambda x: chinese_other_map.get(x.group(0), x.group(0)), content)


if __name__ == '__main__':
    # store_dict()
    s = '\ue66b.\ue331'
    print(get_number(s))
