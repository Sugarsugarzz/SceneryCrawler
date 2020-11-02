import scrapy
from SceneryCrawler.items import SceneryItem, ReviewItem
from SceneryCrawler.utils.decrypt import get_number, get_chinese, get_other_chinese


class DianpingSpider(scrapy.Spider):
    """ 大众点评 - 北京景点信息采集 """
    name = 'dianping-s'
    start_urls = ['http://www.dianping.com/beijing/ch35/o3']

    def parse(self, response, **kwargs):
        """ 获取父类别 """
        categories = response.xpath('//div[@id="classfy"]/a')
        # for a in categories:
        for a in categories[:1]:  # 测试
            category = a.xpath('span/text()').get()
            url = a.xpath('@href').get()
            self.logger.info("一级：" + category + " - " + url)
            print("一级：" + category + " - " + url)
            yield scrapy.Request(url=url, callback=self.sub_category_parse, meta={'category': category})

    def sub_category_parse(self, response):
        """ 获取子类别 """
        sub_categories = response.xpath('//div[@id="classfy-sub"]/a')
        if sub_categories:
            # for a in sub_categories[1:]:
            for a in sub_categories[1:2]:  # 测试
                category = a.xpath('span/text()').get()
                url = a.xpath('@href').get()
                self.logger.info("二级：" + category + " - " + url)
                print("二级：" + category + " - " + url)
                yield scrapy.Request(url=url, callback=self.page_parse, meta={'category': category})
        else:  # 没有子类别的情况
            yield scrapy.Request(url=response.url, callback=self.page_parse,
                                 meta={'category': response.meta['category']}, dont_filter=True)

    def page_parse(self, response):
        """ 页码解析 """
        page_num = response.xpath('//div[@class="page"]/a[last()-1]/text()').get()
        if page_num is None:  # 只有一页的情况
            page_num = 1
        print("{} Total page number is : {}".format(response.meta['category'], page_num))
        self.logger.info("{} Total page number is : {}".format(response.meta['category'], page_num))
        # for i in range(1, int(page_num) + 1):
        for i in range(1, 2):  # 测试
            url = response.url + "p" + str(i)
            yield scrapy.Request(url=url, callback=self.item_parse, meta={'category': response.meta['category']})

    def item_parse(self, response):
        print("{} Processing page : {}".format(response.meta['category'], response.url))
        self.logger.info("{} Processing page : {}".format(response.meta['category'], response.url))
        """ 景点基本信息采集 """
        for li in response.xpath('//div[@id="shop-all-list"]/ul/li'):
            item = SceneryItem()
            item['name'] = li.xpath('.//div[@class="txt"]/div[@class="tit"]//h4/text()').get().strip()
            b = li.xpath('.//div[@class="comment"]/a[@class="review-num"]/b')
            item['review_count'] = get_chinese(b.xpath('string(.)').get())
            b = li.xpath('.//div[@class="comment"]/a[@class="mean-price"]/b')
            item['per_cost'] = get_chinese(b.xpath('string(.)').get()).replace('￥', '')
            b = li.xpath('.//span[@class="comment-list"]/span[1]/b')
            item['total_score'] = get_chinese(b.xpath('string(.)').get())
            b = li.xpath('.//span[@class="comment-list"]/span[2]/b')
            item['env_score'] = get_chinese(b.xpath('string(.)').get())
            b = li.xpath('.//span[@class="comment-list"]/span[3]/b')
            item['serve_score'] = get_chinese(b.xpath('string(.)').get())
            item['category'] = response.meta['category']
            b = li.xpath('.//div[@class="tag-addr"]/a[2]/span')
            item['location'] = get_number(b.xpath('string(.)').get())
            b = li.xpath('.//span[@class="addr"]')
            item['address'] = get_other_chinese(b.xpath('string(.)').get())
            item['pic'] = li.xpath('.//div[@class="pic"]//img/@src').get()
            item['source'] = '大众点评'
            item['url'] = li.xpath('.//div[@class="tit"]//a/@href').get()
            item['ref_url'] = response.url

            yield item
