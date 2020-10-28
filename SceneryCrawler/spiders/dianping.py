import scrapy
from SceneryCrawler.items import SceneryItem, ReviewItem
from SceneryCrawler.utils.decrypt import get_number, get_chinese, get_other_chinese
from SceneryCrawler.utils.svg_map import replace_map

class DianpingSpider(scrapy.Spider):
    name = 'dianping'
    # start_urls = ['http://www.dianping.com/beijing/ch35/o3']
    start_urls = ['http://www.dianping.com/shop/k1F8YkiWg19LvoIJ/review_all']

    # def parse(self, response, **kwargs):
    #     """ 获取父类别 """
    #     categories = response.xpath('//div[@id="classfy"]/a')
    #     for a in categories:
    #         category = a.xpath('span/text()').get()
    #         url = a.xpath('@href').get()
    #         print(url)
    #         yield scrapy.Request(url=url, callback=self.sub_category_parse, meta={'category': category})
    #
    # def sub_category_parse(self, response):
    #     """ 获取子类别 """
    #     sub_categories = response.xpath('//div[@id="classfy-sub"]/a')
    #     if sub_categories:
    #         for a in sub_categories[1:]:
    #             category = a.xpath('span/text()').get()
    #             url = a.xpath('@href').get()
    #             print(category + " - " + url)
    #             yield scrapy.Request(url=url, callback=self.page_parse, meta={'category': category})
    #     else:
    #         yield scrapy.Request(url=response.url, callback=self.page_parse,
    #                              meta={'category': response.meta['category']})
    #
    # def page_parse(self, response):
    #     """ 页码解析 """
    #     page_num = response.xpath('//div[@class="page"]/a[last()-1]/text()').get()
    #     self.logger.info("{} Total page number is : {}".format(response.meta['category'], page_num))
    #     for i in range(1, int(page_num)):
    #         url = 'http://www.dianping.com/beijing/ch35/g33831o3p' + str(i)
    #         yield scrapy.Request(url=url, callback=self.item_parse, meta={'category': response.meta['category']})
    #
    # def item_parse(self, response):
    #     """ 景点基本信息采集 """
    #     for li in response.xpath('//div[@id="shop-all-list"]/ul/li'):
    #         item = SceneryItem()
    #         item['name'] = li.xpath('.//div[@class="txt"]/div[@class="tit"]//h4/text()').get().strip()
    #         b = li.xpath('.//span[@class="comment-list"]/span[1]/b')
    #         item['score'] = get_number(b.xpath('string(.)').get())
    #         item['category'] = response.meta['category']
    #         b = li.xpath('.//div[@class="tag-addr"]/a[2]/span')
    #         item['location'] = get_other_chinese(b.xpath('string(.)').get())
    #         b = li.xpath('.//span[@class="addr"]')
    #         item['address'] = get_chinese(b.xpath('string(.)').get())
    #         item['pic'] = li.xpath('.//div[@class="pic"]//img/@src').get()
    #         b = li.xpath('.//div[@class="comment"]/a[@class="review-num"]/b')
    #         item['review_count'] = get_number(b.xpath('string(.)').get())
    #         item['source'] = '大众点评'
    #         item['url'] = li.xpath('.//div[@class="tit"]//a/@href').get()
    #
    #         yield item
    #
    #         """ 跳转评论页面 """
    #         url = li.xpath('.//div[@class="tit"]//a/@href').get() + '/review_all'
    #         print(li.xpath('.//div[@class="tit"]//a/@title').get() + " - " + url)
    #         yield scrapy.Request(url=url, callback=self.review_page_parse)
    #
    def parse(self, response, **kwargs):
        """ 用户评论页码解析 """
        page_num = response.xpath('//div[@class="reviews-pages"]/a[last()-1]/text()').get()
        self.logger.info("Total page number is : {}".format(page_num))
        # for i in range(1, int(page_num)):
        for i in range(1, 3):
            url = response.url + '/p' + str(i)
            print(url)
            yield scrapy.Request(url=url, callback=self.review_parse)

    def review_parse(self, response):
        self.logger.info("请求头")
        self.logger.info(response.request.headers)
        self.logger.info(response.request.headers.getlist('Cookie'))
        """ 用户评论信息采集 """
        # 解密
        for i in replace_map:
            response = response.replace(body=response.text.replace(i['code'], i['word']))

        lis = response.xpath('//div[@class="reviews-items"]/ul/li')
        for li in lis:
            item = ReviewItem()
            item['name'] = li.xpath('.//div[@class="dper-info"]/a/text()').get().strip()
            div = li.xpath('.//div[@class="review-words Hide"]')
            print(div)
            if div is None or div == []:
                div = li.xpath('.//div[@class="review-words"]')
            item['content'] = div.xpath('string(.)').get().replace('收起评价', '').replace('\n\n', '\n').strip()
            item['pics'] = []
            for pic_li in li.xpath('.//div[@class="review-pictures"]/ul/li'):
                item['pics'].append(pic_li.xpath('.//img/@data-big').get())
            item['scenery_name'] = response.xpath('//h1[@class="shop-name"]/text()').get()
            item['source'] = '大众点评'
            item['url'] = response.url
            yield item
