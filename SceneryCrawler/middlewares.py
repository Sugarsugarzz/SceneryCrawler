from fake_useragent import UserAgent


class RandomUserAgentMiddleware(object):
    """
    随机 User-Agent
    """
    def process_request(self, request, spider):
        ua = UserAgent()
        request.headers['User-Agent'] = ua.random


class ProxyMiddleware(object):
    """
    代理 IP
    """
    def process_request(self, request, spider):
        ip = ''
        request.meta['proxy'] = ip


