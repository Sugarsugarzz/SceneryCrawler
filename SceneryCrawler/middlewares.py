from fake_useragent import UserAgent
import time
import hashlib
import pymysql
import requests
import json


class RandomUserAgentMiddleware(object):
    """
    随机 User-Agent
    """
    def process_request(self, request, spider):
        location = 'SceneryCrawler/utils/fake_useragent.json'
        ua = UserAgent(path=location)
        request.headers['User-Agent'] = ua.random


class ProxyMiddleware(object):
    """
    代理 IP
    策略一：动态转发代理IP 一封一个准
    策略二：API获取优质代理IP，用前判断是否可用，可用则用，不可用则删除，被封也删除，用完用API接着获取
    """
    # def __init__(self):
    #     self.orderno = 'ZF20201130031xfsgnI'
    #     self.secret = 'c2d1442c6c184a54a14c42d03fe26a0c'
    #
    # def process_request(self, request, spider):
    #     request.meta['proxy'] = 'http://forward.xdaili.cn:80'
    #     timestamp = str(int(time.time()))  # 时间戳
    #     string = "orderno=" + self.orderno + "," + "secret=" + self.secret + "," + "timestamp=" + timestamp
    #     md5_string = hashlib.md5(string.encode('utf-8')).hexdigest()  # sign
    #     sign = md5_string.upper()
    #     auth = "sign=" + sign + "&" + "orderno=" + self.orderno + "&" + "timestamp=" + timestamp
    #     request.headers['Proxy-Authorization'] = auth

    def __init__(self):
        self.conn = pymysql.connect(host="localhost", user="root", password="123456", db="scenery", charset='utf8', port=3306)
        self.cursor = self.conn.cursor()
        self.ip = ''

    def process_request(self, request, spider):
        print('正在设置代理IP...')
        if self.ip == '':
            self.ip = self.get_random_ip()

        if self.verify_id(self.ip.split(':')[0], self.ip.split(':')[1]):
            request.meta['proxy'] = 'http://' + self.ip
            print('正在使用代理IP：' + 'http://' + self.ip)
        else:
            self.ip = self.get_random_ip()
            request.meta['proxy'] = 'http://' + self.ip
            print('正在使用代理IP：' + 'http://' + self.ip)


    def delete_ip(self, ip):
        """ 设置无效或被封IP的状态为0 """
        sql = "update proxy set status = 0 where ip = '%s'" % ip
        self.cursor.execute(sql)
        self.conn.commit()

    def verify_id(self, ip, port):
        """ 验证代理IP可用性 """
        test_url = "http://www.baidu.com"
        proxy_url = "http://{}:{}".format(ip, port)
        print("正在验证代理IP：" + proxy_url)
        try:
            response = requests.get(test_url, proxies={'http': proxy_url})
        except Exception as e:
            # self.delete_ip(ip)
            print("无效的代理IP：" + proxy_url)
            return False

        code = response.status_code
        if code >= 200 and code < 300:
            print("有效的代理IP：" + proxy_url)
            return True
        else:
            # self.delete_ip(ip)
            print("无效的代理IP：" + proxy_url)
            return False

    def get_random_ip(self):
        print('正在获取随机代理IP...')
        """ 随机获取代理IP """
        sql = """
            select ip, port from proxy
            where status = 1
            order by rand()
            limit 1
        """
        self.cursor.execute(sql)
        # 数据库没有代理了，从API获取一些
        print("从数据库获取了：" + str(self.cursor.fetchall()))
        if len(self.cursor.fetchall()) == 0:
            print("数据库中没有代理IP。")
            url = 'http://api.xdaili.cn/xdaili-api//greatRecharge/getGreatIp?spiderId=73a4f2d48eb840f788897019b8e75bca&orderno=YZ20201127062aaeUwe&returnType=2&count=20'
            r = requests.get(url=url)
            dic = json.loads(r.text.encode('utf-8'))
            print("已从API获取代理IP：" + str(dic))
            for info in dic['RESULT']:
                insert_sql = "insert into proxy(ip, port) values ('%s', '%s')" % (info['ip'], info['port'])
                self.cursor.execute(insert_sql)
                self.conn.commit()

        self.cursor.execute(sql)
        # 从数据库随机获取有效IP返回
        for ip_info in self.cursor.fetchall():
            if self.verify_id(ip_info[0], ip_info[1]):
                print("从数据库获取的这个代理IP有效：" + str(ip_info[0]) + "：" + str(ip_info[1]))
                return "{}:{}".format(ip_info[0], ip_info[1])
            else:
                return self.get_random_ip()
