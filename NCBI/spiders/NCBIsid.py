# -*- coding: utf-8 -*-
import scrapy
import urllib
from openpyxl import load_workbook
from selenium import webdriver
import re
import NCBI.openxls
import os
from scrapy.loader import ItemLoader
from scrapy.http import Request
from NCBI.items import NcbiItem

class NcbisidSpider(scrapy.Spider):
    name = 'NCBIsid'
    allowed_domains = ['NCBI.com']
    global aurl
    global burl

    aurl = "http://www.ncbi.nlm.nih.gov"
    burl='https://www.ncbi.nlm.nih.gov/'
    # start_urls = [
    #     'https://www.ncbi.nlm.nih.gov/pubmed/27096864',
    #     'https://www.ncbi.nlm.nih.gov/pubmed/25870838',
    #
    # ]
    start_urls = NCBI.openxls.getOpenxls()




    # def start_requests(self):
    #     urls=['https://www.ncbi.nlm.nih.gov/pubmed/27096864']
    def parse(self, response):

        Info1=response.xpath('//div[@class="rprt abstract"]')
        Info2url=response.xpath('//div[@id="disc_col"]/a/@href').extract()[0]
        surl=aurl+Info2url

        item=NcbiItem()

        item['journal_name']=Info1.xpath('./div[@class="cit"]/a/@title').extract()[0]
        item['journal_time'] =Info1.xpath('./div[@class="cit"]/text()').extract()[0].split(';')[0]
        item['sid']=Info1.xpath('./div[@class="aux"]/div[@class="resc"]/dl/dd/text()').extract()[0]
        item['cited_times']=0
        driver=webdriver.PhantomJS(executable_path='C:/Users/Wei/Downloads/phantomjs-2.1.1-windows/bin/phantomjs.exe')
        driver.get(surl)
        htmls=driver.page_source

        cited_times=re.search('(?<=Cited by ).*?(?= PubMed)',htmls)
        if cited_times:
            item['cited_times']=cited_times.group()

        yield item


