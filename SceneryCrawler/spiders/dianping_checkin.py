import scrapy
import pymysql
import pandas as pd
import json
from SceneryCrawler.items import CheckInItem


class DianpingSpider(scrapy.Spider):
    """ 大众点评 - 用户打卡数据采集 """
    name = 'dianping-c'
    url = 'http://www.dianping.com/ajax/member/checkin/checkinList'
    headers = {
        'Cookie': '_lxsdk_cuid=1756254e31dc8-0dbb2f5b84c02a-31687304-1aeaa0-1756254e31dc8; _lxsdk=1756254e31dc8-0dbb2f5b84c02a-31687304-1aeaa0-1756254e31dc8; _hc.v=a497ceb2-53d2-fcc1-b83f-acb8e5671083.1603672532; s_ViewType=10; ctu=5fecefa74ea59558a4d9dddd24fb293b8f9710fb8079edab2e1f02e28d5987bd; aburl=1; cityid=2; baidusearch_ab=citybranch%3AA%3A1%7Cindex%3AA%3A1; switchcityflashtoast=1; source=m_browser_test_33; seouser_ab=shop%3AA%3A1%7Cindex%3AA%3A1; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1603678545,1603716657,1603884877,1603885103; fspop=test; dper=de0737b36330e4ebe65a08979b56c834b9020731acf79d6aae685c0bbefeca5bc4205bf71d4f5a33c35d70527104c462df39847a925a9ee6747233fae317b45843f66dee209f0d3adc800e3649c5ea26a29bead0cc8dcd8a5dc28d09f2d61c40; ll=7fd06e815b796be3df069dec7836c3df; ua=13001230577; cy=2; cye=beijing; dplet=d287b71f69703f1693ceeabcf334ea07; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1604304985; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_s=175877db0d2-41d-944-e0e%7C%7C1376',
        'Origin': 'http://www.dianping.com',
        'Referer': 'http://www.dianping.com/',
    }

    def start_requests(self):
        """ 从数据库获取用户的memberId，通过Ajax请求获取用户所有打卡纪录 """
        db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='scenery')
        sql = "SELECT `name`, home_url FROM reviews"
        df = pd.read_sql(sql=sql, con=db)
        for index, row in df.iterrows():
            if index == 2:  # 测试
                self.logger.info("Processing： {} - {}".format(row['name'], row['home_url'].split('/')[-1]))
                print("Processing： {} - {}".format(row['name'], row['home_url'].split('/')[-1]))
                formdata = {
                    'memberId': row['home_url'].split('/')[-1],
                    'page': '1'
                }
                print(formdata)
                yield scrapy.FormRequest(url=self.url,
                                         headers=self.headers,
                                         formdata=formdata,
                                         callback=self.content_parse,
                                         meta={'formdata': formdata, 'name': row['name']})

    def content_parse(self, response):
        """ 解析JSON获取打卡数据 """
        r = json.loads(response.body)
        data = r['msg']['checkinList']
        for dic in data:
            item = CheckInItem()
            item['member_id'] = response.meta['formdata']['memberId']
            item['name'] = response.meta['name']
            item['shop_name'] = dic['shopName']
            item['shop_address'] = dic['shopAddress']
            item['check_in_time'] = dic['time']
            item['source'] = '大众点评'
            yield item

        # 如果 more 为 True，递归
        if r['msg']['more']:
            formdata = response.meta['formdata']
            formdata['page'] = str(int(formdata['page']) + 1)
            print(formdata)
            yield scrapy.FormRequest(url=self.url,
                                     headers=self.headers,
                                     formdata=formdata,
                                     callback=self.content_parse,
                                     meta={'formdata': formdata, 'name': response.meta['name']})