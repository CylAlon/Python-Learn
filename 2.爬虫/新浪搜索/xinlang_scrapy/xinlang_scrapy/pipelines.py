# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import utils
from xinlang_scrapy.settings import DAY


class XinlangScrapyPipeline:
    def __init__(self):
        self.index = 0
        self.file = utils.writeFile('xinlang')

    def process_item(self, item, spider):

        item = dict(item)
        agotime = utils.dateAgo(day=DAY)
        boo = True
        if item['time'] is not None:
            boo = utils.compare(item['time'],agotime)

        #if utils.compare(item['time'],agotime):
        if boo:
            utils.addFile(self.file,item)

        return item


    def __del__(self):
        utils.closeFile(self.file)
        print('写入文件成功.....')