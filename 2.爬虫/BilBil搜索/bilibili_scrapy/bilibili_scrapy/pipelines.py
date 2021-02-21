# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import utils

class BilibiliScrapyPipeline:
    def __init__(self):
        self.file = utils.writeFile('bilibili')

    def process_item(self, item, spider):
        item = dict(item)
        utils.addFile(self.file,item)
            
        return item

    def __del__(self):
        utils.closeFile(self.file)
        print('写入文件成功.....')
