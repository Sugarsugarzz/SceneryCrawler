from fake_useragent import UserAgent


class RandomUserAgentMiddleware(object):
    """
    随机 User-Agent
    """
    def process_request(self, request, spider):
        ua = UserAgent()
        request.headers['User-Agent'] = ua.random


