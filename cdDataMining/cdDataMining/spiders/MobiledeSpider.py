#coding: utf-8

import scrapy
from datetime import datetime
from dateparser import parse
import hashlib
from hashlib import sha224
from datetime import datetime
from ..database import *
from bson.objectid import ObjectId


class MobiledeSpider(scrapy.Spider):
    name = 'MobiledeSpider'
    base_urls = ['https://www.autoscout24.com/']
    
    def __init__(self):
        self.start_urls = self.base_urls
        self.pushData=[]

    def start_requests(self):
        urls = ["https://www.autoscout24.com/lst/audi?sort=price&desc=0&custtype=D&doorfrom=4&doorto=5&ustate=N%2CU&size=20&page=20&powerfrom=120&powertype=kw&fregfrom=2013&atype=C&ac=0&"]
        for url in urls:
            request = scrapy.Request(url, self.parse)
            yield request
    
    def parse(self, response):
        cars_section = response.xpath("/html/body/div[1]/div[9]/div[4]/div[2]/div[3]/div[2]/div[2]/div/div/div/div/div/div[1]")
        i=1
        for car in cars_section:
            print("here")
        
            ilink = car.xpath("//div[@class='cl-list-element cl-list-element-gap'][{}]//div[@class='cldt-summary-titles']/a/@href".format(i)).extract_first()
            i+=1
            print(ilink)
            if ilink is not None:
                request = scrapy.Request('https://www.autoscout24.com' + ilink, callback=self.parseCarDetail, dont_filter=True)
                yield request
            
    def parseCarDetail(self, response):
        make = response.selector.xpath("/html/body/div[1]/main/div[3]/div/div/div[7]/div[2]/div[1]/div[2]/dl/dd[1]/text()").extract_first().strip()
        year=int(response.selector.xpath("/html/body/div[1]/main/div[2]/div[3]/div[2]/div[1]/div[2]/span[1]/text()").extract_first().split("/")[1])
        capacity=response.selector.xpath("/html/body/div[1]/main/div[2]/div[3]/div[2]/div[1]/div[3]/span[1]/text()").extract_first().split(" ")[0]
        price = response.selector.xpath("/html/body/div[1]/main/div[2]/div[3]/div[1]/div[1]/h2/text()").extract_first()
        price = int(price[2:-3].strip().replace(',',''))
        model = response.selector.xpath("/html/body/div[1]/main/div[3]/div/div/div[7]/div[2]/div[1]/div[2]/dl/dd[2]/a/text()").extract_first().strip()
        fuel = response.selector.xpath("/html/body/div[1]/main/div[2]/div[3]/div[2]/div[1]/div[3]/span[3]/text()").extract_first().split(" ")[1]
        mileage=int(response.selector.xpath("/html/body/div[1]/main/div[2]/div[3]/div[2]/div[1]/div[1]/span/text()").extract_first().split(" ")[0].replace(',',''))
        desc=response.selector.xpath("/html/body/div[1]/main/div[1]/div/div[1]/h1/span[2]/text()").extract_first().strip()
        gearbox = response.selector.xpath("/html/body/div[1]/main/div[2]/div[3]/div[2]/div[1]/div[3]/span[3]/text()").extract_first().split(" ")[0][:-1]
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
 
    
        print(desc)
        print(model)
        print(make)
        print(price)
        print(fuel)
        print(gearbox)
        print(fuel)
        print(year)
        print(mileage)
        print(capacity)
        print(type(year))
        print(type(price))
        print(type(mileage))
        insertCar(make,year,capacity,price,model,fuel,"macedonian",mileage,{},"euro4",desc,[],gearbox,ObjectId("5f9dd3ba42915114689913e6"))
  