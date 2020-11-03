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
        'Cookie': '_lxsdk_cuid=1756254e31dc8-0dbb2f5b84c02a-31687304-1aeaa0-1756254e31dc8; _lxsdk=1756254e31dc8-0dbb2f5b84c02a-31687304-1aeaa0-1756254e31dc8; _hc.v=a497ceb2-53d2-fcc1-b83f-acb8e5671083.1603672532; s_ViewType=10; ctu=5fecefa74ea59558a4d9dddd24fb293b8f9710fb8079edab2e1f02e28d5987bd; aburl=1; cityid=2; baidusearch_ab=citybranch%3AA%3A1%7Cindex%3AA%3A1; switchcityflashtoast=1; source=m_browser_test_33; seouser_ab=shop%3AA%3A1%7Cindex%3AA%3A1; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1603678545,1603716657,1603884877,1603885103; fspop=test; cy=2; cye=beijing; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _dp.ac.v=74219ac2-4dbb-477e-9231-0fd74de26434; lgtoken=0a686c1fc-1097-4bb4-911b-45917ab65c23; dper=c2f02f2236015a9f5620477a7890ac95d5ec1fde137b9b0af934635ac8b3a2492632b3fad3f6a5bc636373667c3fc3915a1dcdee13b8402686301bd59e8fb4a4ca8036f3060b03c34fc1edfcd1e6680920e006597ed9ceb4baabe139ebc68b30; ll=7fd06e815b796be3df069dec7836c3df; ua=dpuser_0138273573; uamo=13011243036; dplet=608daa9f6f6e67c15888e56190d95a0b; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1604377486; _lxsdk_s=1758c36cffa-f2c-c27-4d0%7C%7C757',
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