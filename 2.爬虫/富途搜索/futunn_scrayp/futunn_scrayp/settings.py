import redis

BOT_NAME = 'futunn_scrayp'

SPIDER_MODULES = ['futunn_scrayp.spiders']
NEWSPIDER_MODULE = 'futunn_scrayp.spiders'


# 该user_gent未使用 使用faker随机构造
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36'


# Obey robots.txt rules
ROBOTSTXT_OBEY = False


DOWNLOADER_MIDDLEWARES = {
   'futunn_scrayp.middlewares.UserAgentMiddleware': 543,
}
ITEM_PIPELINES = {
   'futunn_scrayp.pipelines.FutunnScrapyPipeline': 300,
   
}
pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool,decode_responses=True)

WEEK =0
DAY = 0
HOUR = 4
MINUTE = 0
SECOND =0

COOKIES = 'device_id=24700f9f1986800ab4fcc880530dd0ed; s=co14ws47pz; __utmz=1.1612710241.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); xq_a_token=176b14b3953a7c8a2ae4e4fae4c848decc03a883; xqat=176b14b3953a7c8a2ae4e4fae4c848decc03a883; xq_r_token=2c9b0faa98159f39fa3f96606a9498edb9ddac60; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTYxMzQ0MzE3MSwiY3RtIjoxNjEyNzQ0ODAyOTgyLCJjaWQiOiJkOWQwbjRBWnVwIn0.pMXyj5wBHd8FTQ05hhL1n8uofrddZFa3yO6v7uGE2wTtS4HjtKbEIFXcqAlFUPrcjvW7anYQE92SgiZnRvGGexK3muxTeAoQBmkXY0of3vhvfLHkky8z03n1cduED8vTwRWtXQ_laB71qNp4GWnZcs8f3xZCOFUmIXZtlfzJqOAs4G71grZO6brOuykyZHBB4RSqW4eJQXvO_9EZPkkRKSyCCTRR2GCYEZaVgFp0qiAR4DxAlUc-2KSczDUVf_9bq5-T0k-d9-dWbgs4y0EJG0KFWb5iH23-3RfiO4ry3xVDtowR6we_Xl1SeeSdyP7tZVMGdlQGo4mSJan-WwJ5Bw; u=531612744830973; Hm_lvt_1db88642e346389874251b5a1eded6e3=1612691258,1612709803,1612744832; __utma=1.442917859.1612710241.1612710241.1612745108.2; __utmc=1; acw_tc=2760820316127558885245920e6ec49047d7e7762c23e2d02329c67c7f1c8a; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1612756579'


LOG_FILE = "log.log"

LOG_LEVEL = "INFO"