
import redis
BOT_NAME = 'xinlang_scrapy'

SPIDER_MODULES = ['xinlang_scrapy.spiders']
NEWSPIDER_MODULE = 'xinlang_scrapy.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36'


# Obey robots.txt rules
ROBOTSTXT_OBEY = False


DOWNLOADER_MIDDLEWARES = {
   'xinlang_scrapy.middlewares.UserAgentMiddleware': 543,
}
ITEM_PIPELINES = {
   'xinlang_scrapy.pipelines.XinlangScrapyPipeline': 300,
}
pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool,decode_responses=True)

DAY = 7
