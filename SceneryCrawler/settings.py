import datetime
import random

BOT_NAME = 'SceneryCrawler'

SPIDER_MODULES = ['SceneryCrawler.spiders']
NEWSPIDER_MODULE = 'SceneryCrawler.spiders'

# 日志
LOG_LEVEL = 'DEBUG'
to_day = datetime.datetime.now()
log_file_path = '/Users/sugar/Documents/Projects/PythonProjects/SceneryCrawler/SceneryCrawler/log/' + \
                'scrapy_dianping_review_{}_{}_{}_part1.log'.format(to_day.year, to_day.month, to_day.day)
LOG_FILE = log_file_path

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'SceneryCrawler (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
HTTPERROR_ALLOWED_CODES = [403, 400]
# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 1

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = eval("%.1f" % (random.random() * 10 + 2))
DOWNLOAD_DELAY = 3
DOWNLOAD_TIMEOUT = 15
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False  # 一个坑，使用settings文件中的cookie，需要解除注释，设置为False，否则注释情况下默认是True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
cookies = [
    # 13011243036 ️
    # 18811315629 ✔
    # 13001230577
    # 16733957594  被冻结
    # 17184232696
    # 13329352337 （有人使用）
    # 16532373495 （有人使用）
    # 16533834139
    # 17172395742
]
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Encoding': 'gzip, deflate',
  'Accept-Language': 'zh-cn',
  'Connection': 'keep-alive',
  'Cookie': '_lxsdk_s=1759b24649e-299-995-87e%7C%7C694; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1604627040; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1604580363,1604580902,1604625655,1604627013; s_ViewType=10; cy=2; cye=beijing; dper=5ea05e18c6d8c7095a715f9fd972a6861e02820f7daf406a452ce911e73e656eee11f1fa18868c42657aa1378ef9d26d892aa7006ed077ef84045aaa1721b6e71a42afc09c512f4065da380c9f7156b48dfcbc909ae7c32c477ce01514b18b9b; dplet=1dddcc7992ba9ebf3f72bc4a23b78dd9; ll=7fd06e815b796be3df069dec7836c3df; ua=18811315629; lgtoken=066af0fc7-736a-423d-b54e-5b9d95c19b7d; ctu=5fecefa74ea59558a4d9dddd24fb293b1f8251125479ba4c6db981d29ea294df; _hc.v=b765b5d5-62d1-48c6-ab3d-6bad484d4ddc.1604580457; _lxsdk=175878298eac8-0b822b24e358fa8-3e62694b-1aeaa0-175878298eac8; _lxsdk_cuid=175878298eac8-0b822b24e358fa8-3e62694b-1aeaa0-175878298eac8; fspop=test',
  # 'Cookie': random.choice(cookies),
  'Host': 'www.dianping.com',
  'Upgrade-Insecure-Requests': 1,
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15',
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'SceneryCrawler.middlewares.ProxyMiddleware': 1,
   'SceneryCrawler.middlewares.ErrorMiddleware': 5,
   # 'SceneryCrawler.middlewares.RandomUserAgentMiddleware': 543,
   # 'scrapy.downloadmiddlewares.useragent.UserAgentMiddle': None
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'SceneryCrawler.pipelines.MySQLPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
