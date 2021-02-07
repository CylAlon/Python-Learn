'''
# -*- coding:utf-8 -*-: 
Descripttion: 
Author: Cyl
Date: 2021-02-05 11:03:45
'''
# Scrapy settings for search project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import redis

BOT_NAME = 'search'

SPIDER_MODULES = ['search.spiders']
NEWSPIDER_MODULE = 'search.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36'
PROXY_LIST =[
    'https://115.221.241.234:9999',
    'https://103.80.83.48:3127',
    'https://114.239.151.83:9999',
    'https://78.111.97.180:3140'
]
# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'search.middlewares.SearchSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
#    'search.middlewares.SearchDownloaderMiddleware': 543,
    'search.middlewares.UserAgentMiddleware': 299,
    'search.middlewares.ProxyMiddleware': 300,
    # 'search.middlewares.ChromeMiddleware': 301,

}
# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'search.pipelines.SearchPipeline': 300,
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

# FIND_NAME = ''

FLAG = True

pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)

COOKIE = "SINAGLOBAL=8144964158650.4.1609506642704; wvr=6; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5.G2nEPhWV5xb6NOxlEBTE5JpX5KMhUgL.Fo-ESh27Soece0z2dJLoIE-LxKqLBoMLBK2LxKMLB-eL1K2_i--fi-i8i-88i--Ni-8hiK.p; ALF=1644124499; SSOLoginState=1612588500; SCF=ApvaIfNe02THQN2fnLIg0-XBX61pNiiVkwk5Z-_HjJRaQfYtrLfBxB_oWKBBIzfjlg3aaFuyhGpjViZ5Cav39CU.; SUB=_2A25NGlWEDeRhGeNM71MR9i3KyD6IHXVubsBMrDV8PUNbmtANLWTBkW9NTjRPLSKcANd51zXSbHkA0jjppZMXAbB0; _s_tentry=login.sina.com.cn; UOR=,,www.baidu.com; Apache=4692495885050.207.1612588504091; ULV=1612588504100:2:2:2:4692495885050.207.1612588504091:1612516615060; WBtopGlobal_register_version=2021020613; webim_unReadCount=%7B%22time%22%3A1612589155610%2C%22dm_pub_total%22%3A5%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A43%2C%22msgbox%22%3A0%7D; WBStorage=8daec78e6a891122|undefined"