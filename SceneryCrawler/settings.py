import datetime
import random

BOT_NAME = 'SceneryCrawler'

SPIDER_MODULES = ['SceneryCrawler.spiders']
NEWSPIDER_MODULE = 'SceneryCrawler.spiders'

# 日志
LOG_LEVEL = 'DEBUG'
to_day = datetime.datetime.now()
log_file_path = '/Users/sugar/Documents/Projects/PythonProjects/SceneryCrawler/SceneryCrawler/log/' + \
                'scrapy_dianping_review_{}_{}_{}_part2.log'.format(to_day.year, to_day.month, to_day.day)
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
DOWNLOAD_DELAY = 2
DOWNLOAD_TIMEOUT = 10
RETRY_ENABLED = True
RETRY_TIMES = 5
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True  # 一个坑，使用settings文件中的cookie，需要解除注释，设置为False，否则注释情况下默认是True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
cookies = [
    # 13011243036 ️√
    # 18811315629  √
    # 13001230577
    # 17184232696 √
    # 13329352337
    # 17172395742
    # 17050820646
    # 16228080923
    # 16255724657
    # 16733957245
    # 17179476710
    # 16533852041
    # 16740948128
    # 16222525784
    # 16532761051 (checkin)
    #
    #
    #
    #
]
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Encoding': 'gzip, deflate',
  'Accept-Language': 'zh-cn',
  'Connection': 'keep-alive',
  # 'Cookie': '_lxsdk_s=175aac99a26-479-c7c-059%7C%7C86; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1604888160; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1604888141; ctu=7cb3d70a27bdab332741260addc0bc31684a118bcc3b4be4e20cdb241a090546; dper=c2f02f2236015a9f5620477a7890ac952a5941dff3e680268b94df57813bdcce354b7c964fa677ebc626717d279619f4a85ec4118f78413b3260323c0ddebad2f20272f995f4ecfa5ae561e1daab5b7c809658f062b49e160e44d5f67142fc87; dplet=9f01f0d226be7aa37a93e9662813072b; ll=7fd06e815b796be3df069dec7836c3df; s_ViewType=10; ua=13011243036; lgtoken=07aeb023c-7409-4e0b-9443-2ea35aab3645; _hc.v=b7eb2456-769e-908a-ad3f-dd97de557740.1604888140; _lxsdk=175aac99a25c8-0b6f3502f015ee8-3e62694b-1aeaa0-175aac99a25c8; _lxsdk_cuid=175aac99a25c8-0b6f3502f015ee8-3e62694b-1aeaa0-175aac99a25c8',
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
   'SceneryCrawler.middlewares.CookieMiddleware': 2,
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
