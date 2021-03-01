# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv

class ImoocScrapyPipeline:

    def __init__(self):
        self.f = open('course.csv','w',encoding='utf-8')
        self.csv_f = csv.writer(self.f)
        self.csv_f.writerow(('id','课程名','封面地址','课程时长','课程价格','课程简介','讲师','地址'))
        self.f.close()
        self.ff = open('course.csv','a+',encoding='utf-8')
        self.csv_ff = csv.writer(self.ff)

    def process_item(self, item, spider):
        tu = (item['id'],item['course_name'],item['cover_img_address'],item['course_duration'],item['course_price'],item['course_information'],item['course_teacher'],item['course_video_address'])
        self.csv_ff.writerow(tu)
        return item



    def __del__(self):
        self.ff.close()
