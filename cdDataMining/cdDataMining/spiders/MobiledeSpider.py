#coding: utf-8

import scrapy
from datetime import datetime
from dateparser import parse
import hashlib
from hashlib import sha224
from datetime import datetime
from ..database import *


class MobiledeSpider(scrapy.Spider):
    name = 'MobiledeSpider'
    base_urls = ['https://www.autoscout24.com/']
    
    def __init__(self):
        self.start_urls = self.base_urls
        self.pushData=[]

    def start_requests(self):
        urls = ["https://www.autoscout24.com/lst/renault?sort=price&desc=0&custtype=D&doorfrom=4&doorto=5&ustate=N%2CU&size=20&page=20&powerfrom=120&powertype=kw&fregfrom=2013&atype=C&ac=0&"]
        for url in urls:
            request = scrapy.Request(url, self.parse)
            yield request
    
    def parse(self, response):
        cars_section = response.xpath("//div[2]/div[3]/div[2]/div[2]/div/div/div")
        i=1
        for car in cars_section:
        
            ilink = car.xpath("//div[@class='cl-list-element cl-list-element-gap'][{}]//div[@class='cldt-summary-titles']/a/@href".format(i)).extract_first()
            i+=1
            if ilink is not None:
                print(ilink)
                request = scrapy.Request('https://www.autoscout24.com' + ilink, callback=self.parseCarDetail, dont_filter=True)
                yield request
            
    def parseCarDetail(self, response):
        try:
            price = response.selector.xpath("/html/body/div[1]/main/div[3]/div[3]/div[1]/div[1]/h2/text()").extract_first()
            price = price[2:-3]
            print(price)
            car = response.selector.xpath("/html/body/div[1]/main/div[2]/div/div[1]/h1/span/text()").extract_first().strip()
            desc=response.selector.xpath("/html/body/div[1]/main/div[2]/div/div[1]/h1/span[2]/text()").extract_first() 
            make = car.split(" ")[0]
            model = car.split(" ")[1]
            description = car + ' ' + desc
            power=response.selector.xpath("/html/body/div[1]/main/div[3]/div[3]/div[2]/div[1]/div[3]/span[1]/text()").extract_first().split(" ")[0]
            transmission = response.selector.xpath("/html/body/div[1]/main/div[3]/div[3]/div[2]/div[1]/div[3]/span[3]/text()").extract_first().split(" ")[0][:-1]
            fuel = response.selector.xpath("/html/body/div[1]/main/div[3]/div[3]/div[2]/div[1]/div[3]/span[3]/text()").extract_first().split(" ")[1]
            date=response.selector.xpath("/html/body/div[1]/main/div[3]/div[3]/div[2]/div[1]/div[2]/span[1]/text()").extract_first()
            date = datetime.strptime(date, "%m/%Y")
            mileage=response.selector.xpath("/html/body/div[1]/main/div[3]/div[3]/div[2]/div[1]/div[1]/span/text()").extract_first().split(" ")[0]
            image=response.selector.xpath("//div//div[@class='as24-pictures__content']//img/@src").extract_first()
            hash = sha224(make.encode() + image.encode()).hexdigest()
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            price = int(price.replace(',',''))
            mileage=int(mileage.replace(',',''))
        except:
            pass
    
        # print(description)
        # print(model)
        # print(make)
        # print(price)
        # print(power)
        # print(transmission)
        # print(fuel)
        # print(date)
        # print(mileage)
        # print(type(date))
        # print(type(price))
        # print(type(mileage))
        # print(image)
        insertCar(hash,make,model,description,fuel,image,price,power,mileage,date,'agniramadani')
  