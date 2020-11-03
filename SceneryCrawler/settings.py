import datetime
import random

BOT_NAME = 'SceneryCrawler'

SPIDER_MODULES = ['SceneryCrawler.spiders']
NEWSPIDER_MODULE = 'SceneryCrawler.spiders'

# 日志
LOG_LEVEL = 'DEBUG'
to_day = datetime.datetime.now()
log_file_path = '/Users/sugar/Documents/Projects/PythonProjects/SceneryCrawler/SceneryCrawler/log/' + \
                'scrapy_dianping_review_{}_{}_{}.log'.format(to_day.year, to_day.month, to_day.day)
LOG_FILE = log_file_path

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'SceneryCrawler (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
HTTPERROR_ALLOWED_CODES = [403, 400]
# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = eval("%.1f" % (random.random() * 10+ 5))
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False  # 一个坑，使用settings文件中的cookie，需要解除注释，设置为False，否则注释情况下默认是True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'Accept-Encoding': 'gzip, deflate',
  'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
  'Connection': 'keep-alive',
  'Cookie': '_lxsdk_cuid=1756254e31dc8-0dbb2f5b84c02a-31687304-1aeaa0-1756254e31dc8; _lxsdk=1756254e31dc8-0dbb2f5b84c02a-31687304-1aeaa0-1756254e31dc8; _hc.v=a497ceb2-53d2-fcc1-b83f-acb8e5671083.1603672532; s_ViewType=10; ctu=5fecefa74ea59558a4d9dddd24fb293b8f9710fb8079edab2e1f02e28d5987bd; aburl=1; cityid=2; baidusearch_ab=citybranch%3AA%3A1%7Cindex%3AA%3A1; switchcityflashtoast=1; source=m_browser_test_33; seouser_ab=shop%3AA%3A1%7Cindex%3AA%3A1; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1603678545,1603716657,1603884877,1603885103; fspop=test; cy=2; cye=beijing; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _dp.ac.v=74219ac2-4dbb-477e-9231-0fd74de26434; lgtoken=0a686c1fc-1097-4bb4-911b-45917ab65c23; dper=c2f02f2236015a9f5620477a7890ac95d5ec1fde137b9b0af934635ac8b3a2492632b3fad3f6a5bc636373667c3fc3915a1dcdee13b8402686301bd59e8fb4a4ca8036f3060b03c34fc1edfcd1e6680920e006597ed9ceb4baabe139ebc68b30; ll=7fd06e815b796be3df069dec7836c3df; ua=dpuser_0138273573; uamo=13011243036; dplet=608daa9f6f6e67c15888e56190d95a0b; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1604377486; _lxsdk_s=1758c36cffa-f2c-c27-4d0%7C%7C757',
  'Host': 'www.dianping.com',
  'Upgrade-Insecure-Requests': 1,
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {

}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'SceneryCrawler.middlewares.ProxyMiddleware': 1,
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
