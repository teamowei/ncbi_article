# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from openpyxl import Workbook,load_workbook
import os

class NcbiPipeline(object):
    def open_spider(self,spider):
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append(['sid', '时间', '名字', '引用次数'])
    def process_item(self, item, spider):
        # with open("my_Ncbi.txt", 'a') as fp:
        #     fp.write(item['sid'].encode("utf8").decode() + '\n'+item['journal_time'].encode("utf8").decode() + '\n'+item['journal_name'].encode("utf8").decode() + '\n'+item['cited_times'].encode("utf8").decode() + '\n\n')

        line=[item['sid'],item['journal_time'],item['journal_name'],item['cited_times']]
        self.ws.append(line)
        return item

    def close_spider(self, spider):
        save_file=os.getcwd()+"\\result.xlsx"
        print('done')

        self.wb.save(save_file)
