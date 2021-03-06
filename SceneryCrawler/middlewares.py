from fake_useragent import UserAgent
import time
import hashlib
import scrapy
import pymysql
import requests
import json
import yagmail


class ErrorMiddleware(object):
    """
    发生错误处理中间件
    """
    @staticmethod
    def is_verify(response):
        """ 判断是否弹出验证 """
        return False if response.url.find("verify.meituan.com") >= 0 else True

    @staticmethod
    def send_mail(content):
        mail = yagmail.SMTP(user="caijidianping@163.com",
                            password="caiji123456",
                            host="smtp.163.com")
        mail.send("406857586@qq.com", "Spider Error！", content)

    def process_response(self, request, response, spider):
        if not self.is_verify(response):  # 检测是否需要验证
            print('请输入验证码！ - ' + str(request.url))
            self.send_mail("出现验证码，关闭爬虫")
            # return scrapy.Request(url=request.url, dont_filter=True)
            spider.crawler.engine.close_spider(spider, "出现验证码，关闭爬虫")

        if response.status in [403]:  # 检测是否403
            print('403！ - ' + str(request.url))
            self.send_mail("403 - Cookie失效，关闭爬虫")
            # return scrapy.Request(url=request.url, dont_filter=True)
            spider.crawler.engine.close_spider(spider, "403 - User-Agent失效，关闭爬虫")

        return response

    def process_exception(self, request, exception, spider):
        if isinstance(exception, TimeoutError):
            return request


class RandomUserAgentMiddleware(object):
    """
    随机 User-Agent
    """
    def process_request(self, request, spider):
        # location = 'SceneryCrawler/utils/fake_useragent.json'
        # ua = UserAgent(path=location)
        ua = UserAgent()
        request.headers['User-Agent'] = ua.random


class ProxyMiddleware(object):
    """
    策略一：动态代理转发 IP
        一封一个准
    """
    def __init__(self):
        self.orderno = 'ZF20201130031xfsgnI'
        self.secret = 'c2d1442c6c184a54a14c42d03fe26a0c'

    def process_request(self, request, spider):
        request.meta['proxy'] = 'http://forward.xdaili.cn:80'
        timestamp = str(int(time.time()))  # 时间戳
        string = "orderno=" + self.orderno + "," + "secret=" + self.secret + "," + "timestamp=" + timestamp
        md5_string = hashlib.md5(string.encode('utf-8')).hexdigest()  # sign
        sign = md5_string.upper()
        auth = "sign=" + sign + "&" + "orderno=" + self.orderno + "&" + "timestamp=" + timestamp
        request.headers['Proxy-Authorization'] = auth

    """
    策略二：API获取优质代理IP，用前判断是否可用，可用则用，不可用则删除，被封也删除，用完用API接着获取
    """
    # def __init__(self):
    #     self.conn = pymysql.connect(host="localhost", user="root", password="123456", db="scenery", charset='utf8', port=3306)
    #     self.cursor = self.conn.cursor()
    #     self.ip = ''
    #
    # def process_request(self, request, spider):
    #     """ 设置代理 """
    #     print('Proxy - 正在设置代理IP...')
    #     if self.ip == '':
    #         self.ip = self.get_random_ip()
    #
    #     if self.verify_id(self.ip.split(':')[0], self.ip.split(':')[1]):
    #         request.meta['proxy'] = 'http://' + self.ip
    #         print('Proxy - 正在使用代理IP：' + 'http://' + self.ip)
    #     else:
    #         self.ip = self.get_random_ip()
    #         request.meta['proxy'] = 'http://' + self.ip
    #         print('Proxy - 正在使用代理IP：' + 'http://' + self.ip)
    #
    # # def process_response(self, request, response, spider):
    # #     """ 代理被封，则更换代理，重新请求 """
    # #     if response.status in [403, 303]:
    # #         self.invalid_ip(self.ip.split(':')[0], self.ip.split(':')[1])
    # #         self.ip = self.get_random_ip()
    # #         print('Proxy - 上一个代理被封，正在使用更换后的代理IP：' + 'http://' + self.ip)
    # #         return request
    # #     else:
    # #         return responsew
    #
    # def invalid_ip(self, ip, port):
    #     """ 设置无效或被封IP的状态为0 """
    #     sql = "update proxy set status = 0 where ip = '%s' and port = '%s'" % (ip, port)
    #     self.cursor.execute(sql)
    #     self.conn.commit()
    #
    # def verify_id(self, ip, port):
    #     """ 验证代理IP可用性 """
    #     test_url = "http://www.baidu.com"
    #     proxy_url = "http://{}:{}".format(ip, port)
    #     print("Proxy - 正在验证代理IP：" + proxy_url)
    #     try:
    #         response = requests.get(test_url, proxies={'http': proxy_url}, timeout=5)
    #     except Exception as e:
    #         self.invalid_ip(ip, port)
    #         print("Proxy - 无效的代理IP：" + proxy_url)
    #         return False
    #
    #     code = response.status_code
    #     if 200 <= code < 300:
    #         print("Proxy - 有效的代理IP：" + proxy_url)
    #         return True
    #     else:
    #         self.invalid_ip(ip, port)
    #         print("Proxy - 无效的代理IP：" + proxy_url)
    #         return False
    #
    # def get_random_ip(self):
    #     print('Proxy - 正在获取随机代理IP...')
    #     """ 随机获取代理IP """
    #     sql = """
    #         select ip, port from proxy where status = 1
    #         order by rand() limit 1
    #     """
    #     self.cursor.execute(sql)
    #     # 数据库没有代理了，从API获取一些
    #     result = self.cursor.fetchall()
    #     # print("Proxy - 从数据库获取了：" + str(result))
    #     if len(result) == 0:
    #         print("Proxy - 数据库中没有代理IP。")
    #         url = 'http://api.xdaili.cn/xdaili-api//greatRecharge/getGreatIp?spiderId=73a4f2d48eb840f788897019b8e75bca&orderno=YZ20201127062aaeUwe&returnType=2&count=20'
    #         r = requests.get(url=url)
    #         dic = json.loads(r.text.encode('utf-8'))
    #         print("Proxy - 已从API获取代理IP：" + str(dic))
    #         for info in dic['RESULT']:
    #             insert_sql = "insert into proxy(ip, port) values ('%s', '%s')" % (info['ip'], info['port'])
    #             self.cursor.execute(insert_sql)
    #             self.conn.commit()
    #         self.cursor.execute(sql)
    #         result = self.cursor.fetchall()
    #
    #     # 从数据库随机获取有效IP返回
    #     for ip_info in result:
    #         if self.verify_id(ip_info[0], ip_info[1]):
    #             print("Proxy - 从数据库获取的这个代理IP有效：" + str(ip_info[0]) + "：" + str(ip_info[1]))
    #             return "{}:{}".format(ip_info[0], ip_info[1])
    #         else:
    #             return self.get_random_ip()
