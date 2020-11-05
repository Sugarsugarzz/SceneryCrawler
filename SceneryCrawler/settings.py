import datetime
import random

BOT_NAME = 'SceneryCrawler'

SPIDER_MODULES = ['SceneryCrawler.spiders']
NEWSPIDER_MODULE = 'SceneryCrawler.spiders'

# 日志
LOG_LEVEL = 'DEBUG'
to_day = datetime.datetime.now()
log_file_path = '/Users/sugar/Documents/Projects/PythonProjects/SceneryCrawler/SceneryCrawler/log/' + \
                'scrapy_dianping_review_{}_{}_{}_part3.log'.format(to_day.year, to_day.month, to_day.day)
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
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16
DOWNLOAD_TIMEOUT = 15
# Disable cookies (enabled by default)
COOKIES_ENABLED = False  # 一个坑，使用settings文件中的cookie，需要解除注释，设置为False，否则注释情况下默认是True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
cookies = [
    # 13011243036
    'fspop=test; cy=2; cye=beijing; _lxsdk_cuid=17592466debc8-03fb9ea04183d1-31687304-1aeaa0-17592466debc8; _lxsdk=17592466debc8-03fb9ea04183d1-31687304-1aeaa0-17592466debc8; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1604476891; _hc.v=43d7f57f-3fc8-8000-dbde-ddb97ff08785.1604476891; dplet=fc66be10f5ef320868e4393c83fa3219; dper=c2f02f2236015a9f5620477a7890ac9542feb653869ed916af67653c647457520c9b04133cb26e538f817a82f0d096a181e6e740c7b9896af616b425720cc7dec43ba55d9be92acede6305d26e1a2474b379754d431ab0c9980c6dc7e1731846; ll=7fd06e815b796be3df069dec7836c3df; ua=13011243036; ctu=7cb3d70a27bdab332741260addc0bc31aac5627bd8ac0825566f58eea4b14b5c; s_ViewType=10; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1604477214; _lxsdk_s=17592466dec-cb4-636-2d5%7C%7C67',
    # 18811315629
    'fspop=test; cy=2; cye=beijing; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=175924cacbac8-0c9ce06ed97ed3-31687304-1aeaa0-175924cacbac8; _lxsdk=175924cacbac8-0c9ce06ed97ed3-31687304-1aeaa0-175924cacbac8; _hc.v=3a50c218-f460-8d19-642d-52906b85bcac.1604477300; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1604477301; lgtoken=0431d946e-0561-4be4-8467-dc263ee571a1; dplet=20a05018f07db48353039f6bbc925039; dper=5ea05e18c6d8c7095a715f9fd972a686e7e9988efc3eaa05a2499ee3753f113fda167d4aefa17354d740c1077d774d8ebd9dde7c8066aebd2d53717b7d0d9398e077f419ae6bff404e874c6c14366035ff5541bbbd07f233a2459ad785eed678; ll=7fd06e815b796be3df069dec7836c3df; ua=18811315629; ctu=d4df631f5235e8d029e57745af6ad097b990b7d04ad60d5b745b3b6cf276934c; s_ViewType=10; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1604477324; _lxsdk_s=175924cacbb-5ff-3b7-8ec%7C%7C66',
    # 13001230577
    'fspop=test; cy=2; cye=beijing; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1604470058,1604470066; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1604478052; _lxsdk_cuid=17591de2d49c8-0c42bf1490b50f-445c6e-1aeaa0-17591de2d49c8; _lxsdk=17591de2d49c8-0c42bf1490b50f-445c6e-1aeaa0-17591de2d49c8; _hc.v=c19f61c0-b1cd-9e9a-c45a-8096222c8284.1604470059; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; ctu=d4df631f5235e8d029e57745af6ad097b8e500a482b46b42aefcea86655dae3d; s_ViewType=10; _lxsdk_s=1759257b4bc-c72-390-1c2%7C%7C52; lgtoken=0163d4cea-91f0-44e5-bdce-775fb5ae354e; dplet=5728b9807ce0e8853c1f1a3527c92fe5; dper=de0737b36330e4ebe65a08979b56c834614e8be5753210b7b71d26795c8c015ed70fed1ae6cd4f25425a33b71562a2281fe0ef644cdefdaa2b11303ffcd16187216f4ace187f41124d72bf30356f51e66c39f045f258fa881c7023c77f61ab4b; ll=7fd06e815b796be3df069dec7836c3df; ua=13001230577'
    # 16733957594  被冻结

]
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'Accept-Encoding': 'gzip, deflate',
  'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
  'Connection': 'keep-alive',
  'Cookie': '_lxsdk_cuid=1756254e31dc8-0dbb2f5b84c02a-31687304-1aeaa0-1756254e31dc8; _lxsdk=1756254e31dc8-0dbb2f5b84c02a-31687304-1aeaa0-1756254e31dc8; _hc.v=a497ceb2-53d2-fcc1-b83f-acb8e5671083.1603672532; s_ViewType=10; ctu=5fecefa74ea59558a4d9dddd24fb293b8f9710fb8079edab2e1f02e28d5987bd; aburl=1; cityid=2; switchcityflashtoast=1; source=m_browser_test_33; seouser_ab=shop%3AA%3A1%7Cindex%3AA%3A1; fspop=test; cy=2; cye=beijing; _dp.ac.v=74219ac2-4dbb-477e-9231-0fd74de26434; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1603884877,1603885103,1604467986,1604477568; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; ll=7fd06e815b796be3df069dec7836c3df; ua=13001230577; dper=de0737b36330e4ebe65a08979b56c834b9602c8862530f8446719d728944e7dd9f07ae085b3660fa7c130ceed6577343874ada06506c4c7496c61a3fbfa5c9e9c18fc58faf3cd79e22001e0ac24cdd5aadef08b3ed2310b6446c72833203b9d2; dplet=e90e69973778b14eeb4bb744283f8d93; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1604539840; _lxsdk_s=17596045176-5e4-9a1-ad8%7C%7C222',
  # 'Cookie': random.choice(cookies),
  'Host': 'www.dianping.com',
  'Upgrade-Insecure-Requests': 1,
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
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
