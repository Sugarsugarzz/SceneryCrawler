import datetime
# Scrapy settings for SceneryCrawler project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'SceneryCrawler'

SPIDER_MODULES = ['SceneryCrawler.spiders']
NEWSPIDER_MODULE = 'SceneryCrawler.spiders'

# 日志
LOG_LEVEL = 'DEBUG'
to_day = datetime.datetime.now()
log_file_path = '/Users/sugar/Documents/Projects/PythonProjects/SceneryCrawler/SceneryCrawler/log/' + \
                'scrapy_{}_{}_{}.log'.format(to_day.year, to_day.month, to_day.day)
LOG_FILE = log_file_path

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'SceneryCrawler (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 9
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
  'Cookie': 'fspop=test; cy=2; cye=beijing; _lxsdk_cuid=1756254e31dc8-0dbb2f5b84c02a-31687304-1aeaa0-1756254e31dc8; _lxsdk=1756254e31dc8-0dbb2f5b84c02a-31687304-1aeaa0-1756254e31dc8; _hc.v=a497ceb2-53d2-fcc1-b83f-acb8e5671083.1603672532; s_ViewType=10; ll=7fd06e815b796be3df069dec7836c3df; ua=13001230577; ctu=5fecefa74ea59558a4d9dddd24fb293b8f9710fb8079edab2e1f02e28d5987bd; aburl=1; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1603672532,1603678545,1603716657; cityid=2; baidusearch_ab=citybranch%3AA%3A1%7Cindex%3AA%3A1; switchcityflashtoast=1; source=m_browser_test_33; seouser_ab=shop%3AA%3A1%7Cindex%3AA%3A1; dper=4e52a9b9cff46f80ab674682d9497fba82e4db7be5564c3021a718c5fedae013594e9376a0a292cd5074dbe4f4df3534db1009658fc0b0b5f7aca23ddec721a75ed92694ea9aac311b786e8023ffeb074cc54eb4e0a05dc07c78ff1dd39cbf9b; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; dplet=e5805a2a6d0d3d26f23d8f95407b932b; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1603864380; _lxsdk_s=1756dc285c6-2a0-442-995%7C%7C446',
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
