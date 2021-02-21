import redis


BOT_NAME = 'bilibili_scrapy'

SPIDER_MODULES = ['bilibili_scrapy.spiders']
NEWSPIDER_MODULE = 'bilibili_scrapy.spiders'


# 该user_gent未使用 使用faker随机构造
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36'


# Obey robots.txt rules
ROBOTSTXT_OBEY = False


DOWNLOADER_MIDDLEWARES = {
   'bilibili_scrapy.middlewares.UserAgentMiddleware': 543,
}
ITEM_PIPELINES = {
   'bilibili_scrapy.pipelines.BilibiliScrapyPipeline': 300,
}
pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool,decode_responses=True)

WEEK =0
DAY = 3
HOUR = 0
MINUTE = 0
SECOND =0

COOKIES = ''

LOG_FILE = "log.log"

LOG_LEVEL = "INFO"