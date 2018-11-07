# -*- coding: utf-8 -*-
import scrapy


class TonghuashuanSpider(scrapy.Spider):
    name = 'tonghuashuan'
    allowed_domains = ['stockpage.10jqka.com.cn']
    start_urls = ['http://stockpage.10jqka.com.cn/603895/company/#detail/']

    def parse(self, response):
        # //*[@id="ml_001"]/table/tbody/tr[1]/td[1]/a
        res_selector = response.xpath("//*[@id=\"ml_001\"]/table/tbody/tr[1]/td[1]/a")

        pass
