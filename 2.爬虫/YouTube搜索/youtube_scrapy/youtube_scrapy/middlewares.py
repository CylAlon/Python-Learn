# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
import utils
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys
import time
from scrapy.http import HtmlResponse
class UserAgentMiddleware(object):

    def process_request(self, request,spider):
        user_gent = utils.userGentRandom()
        request.headers['USER_AGENT'] = user_gent

class ChromeMiddleware(object):
    def __init__(self):
        # self.driver = webdriver.Chrome() 
        # self.driver.set_window_size(500, 500)
        self.options = Options()
        self.options.headless = True
        self.driver = webdriver.Chrome(options=self.options)
        
        time.sleep(1)
        

    def process_request(self, request, spider):
        self.driver.get(request.url)
        
        time.sleep(5)

        # 模拟滚轮

        # 获取页面初始高度
        # hi = "return document.body.scrollHeight;"
        # height = self.driver.execute_script(hi)
        hi = sys.maxsize
        status = True #设置循环标志
        # old_time = time.time()
        # new_time = 0
        # le = 300
        
        while status:
            en=f"window.scrollTo(0,{hi});"
            # new_time = time.time()
            self.driver.execute_script(en)
            hi+=500
            time.sleep(1)
            # da = self.driver.page_source
            try:
                cc = self.driver.find_element_by_xpath('//*[@id="contents"]/ytd-message-renderer/yt-formatted-string').text
            except Exception as e:
                cc = ''
            if cc=='无更多结果':
                break
            # if new_time-old_time>30:
            #     print('时间到')
            #     break
            # //*[@id="message"]
            # new_height = self.driver.execute_script(hi) # 每执行一次滚动条拖到最后，就进行一次参数校验，并且刷新页面高度
            # print('-----',new_height,'-----',height)
            # if new_height > height:
            #     height = new_height
                
                
            # else:
            #     # 当页面高度不再增加的时候，我们就认为已经是页面最底部，结束条件判断
            #     print("滚动条已经处于页面最下方!")
            #     # self.driver.execute_script('window.scrollTo(0, 0)')  # 把滚动条拖到页面顶部
            #     break



        body = self.driver.page_source
        # self.driver.quit()
        # utils.testWriteFile(str(body),hz='html')
        return  HtmlResponse(self.driver.current_url,
                        body=body,
                        encoding='utf-8',
                        request=request)
        
    # def __del__(self):
    #     self.driver.quit()



class YoutubeScrapySpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class YoutubeScrapyDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
