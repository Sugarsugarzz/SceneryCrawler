import scrapy
import pymysql
import pandas as pd
from SceneryCrawler.items import ReviewItem
from SceneryCrawler.utils.svg_map import replace_map
from SceneryCrawler.utils.filter_emoji import filter_emoji


class DianpingSpider(scrapy.Spider):
    """ 大众点评 - 景点网友评论数据采集 """
    name = 'dianping-r'

    def start_requests(self):
        """ 从数据库获取景点URL，补充URL获取所有评论页面 """
        db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='scenery')
        sql = "SELECT id, `name`, url FROM sceneries"
        df = pd.read_sql(sql=sql, con=db)
        for index, row in df.iterrows():
            if index > 210:
                url = row['url']
                self.logger.info("Process {}  {} ：{}".format(index, row['name'], row['url']))
                print("Process {}  {} ：{}".format(index, row['name'], row['url']))
                yield scrapy.Request(url=url, callback=self.review_all_parse, meta={'scenery_name': row['name'], 'index': index})

    def review_all_parse(self, response):
        """ 加一层，从景点主页跳到评论页面，直接访问评论页面被ban的概率大 """
        url = response.url + '/review_all'
        yield scrapy.Request(url=url, callback=self.page_parse, meta={'scenery_name': response.meta['scenery_name'], 'index': response.meta['index']})

    def page_parse(self, response):
        """ 用户评论页码解析 """
        page_num = response.xpath('//div[@class="reviews-pages"]/a[last()-1]/text()').get()
        if page_num is None:
            page_num = 1
        self.logger.info("{}  {} Total page number is : {}".format(response.meta['index'], response.meta['scenery_name'], page_num))
        print("{}  {} Total page number is : {}".format(response.meta['index'], response.meta['scenery_name'], page_num))
        # for i in range(2, 3):  # 测试
        for i in range(1, int(page_num) + 1):
            # if response.meta['index'] != 186 or (response.meta['index'] == 186 and i < 3):
            url = response.url + '/p' + str(i)
            yield scrapy.Request(url=url, callback=self.review_parse, meta={'scenery_name': response.meta['scenery_name'], 'index': response.meta['index']})

    def review_parse(self, response):
        """ 用户评论信息采集 """
        print("{}  {} Processing page : {}".format(response.meta['index'], response.meta['scenery_name'], response.url))
        self.logger.info("{}  {} Processing page : {}".format(response.meta['index'], response.meta['scenery_name'], response.url))
        # 解密
        for i in replace_map:
            response = response.replace(body=response.text.replace(i['code'], i['word']))

        lis = response.xpath('//div[@class="reviews-items"]/ul/li')
        for li in lis:
            item = ReviewItem()
            item['name'] = li.xpath('.//div[@class="dper-info"]/a/text()').get().strip()
            div = li.xpath('.//div[@class="review-words Hide"]')
            if div is None or div == []:
                div = li.xpath('.//div[@class="review-words"]')
            content = div.xpath('string(.)').get().replace('收起评价', '').replace('\n\n', '\n').strip()
            item['content'] = filter_emoji(content)
            item['publish_time'] = li.xpath('.//div[@class="misc-info clearfix"]/span[@class="time"]/text()').get().strip()
            item['pics'] = []
            for pic_li in li.xpath('.//div[@class="review-pictures"]/ul/li'):
                item['pics'].append(pic_li.xpath('.//img/@data-big').get())
            item['scenery_name'] = response.meta['scenery_name']
            item['source'] = '大众点评'
            item['url'] = response.url
            home_url = li.xpath('.//div[@class="dper-info"]/a/@href').get()
            item['home_url'] = home_url.split('/')[-1]

            yield item
