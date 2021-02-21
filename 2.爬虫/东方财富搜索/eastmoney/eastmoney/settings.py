import redis

BOT_NAME = 'eastmoney'

SPIDER_MODULES = ['eastmoney.spiders']
NEWSPIDER_MODULE = 'eastmoney.spiders'


# 该user_gent未使用 使用faker随机构造
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36'


# Obey robots.txt rules
ROBOTSTXT_OBEY = False


DOWNLOADER_MIDDLEWARES = {
   'eastmoney.middlewares.UserAgentMiddleware': 543,
}
ITEM_PIPELINES = {
   'eastmoney.pipelines.EastmoneyPipeline': 300,
   
}
pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool,decode_responses=True)

WEEK =0
DAY = 3
HOUR = 0
MINUTE = 0
SECOND =0

COOKIES = 'qgqp_b_id=2cad6ec7b714175e8c44e1d89bd750c9; waptgshowtime=2021221; st_si=27029812180483; st_asi=delete; emshistory=%5B%22%E4%B8%AD%E5%9B%BD%E5%B9%B3%E5%AE%89%22%2C%22%E8%B5%B5%E4%B8%BD%E9%A2%96%22%5D; st_pvi=83011421220916; st_sp=2021-02-20%2018%3A18%3A49; st_inirUrl=http%3A%2F%2Fso.eastmoney.com%2Fweb%2Fs; st_sn=76; st_psi=20210221180053879-111000300841-0432681167'

LOG_FILE = "log.log"

LOG_LEVEL = "INFO"