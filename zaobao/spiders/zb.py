# -*- coding: utf-8 -*-
import scrapy
from zaobao.items import ZaobaoItem


class ZbSpider(scrapy.Spider):
    name = 'zb'
    allowed_domains = ['www.zaobao.com']
    start_urls = ['http://www.zaobao.com/special/report/politic/fincrisis']

    def parse(self, response):
        # next_url = response.xpath("//li[@class='pager-next first last']/a/@href").extract_first()
        # next_url = response.urljoin(next_url)
        for i in range(1, 21):
            next_url = 'http://www.zaobao.com/special/report/politic/fincrisis?page=' + str(i)
            print(next_url)
            yield scrapy.Request(next_url, callback=self.parse_news_url)

    def parse_news_url(self, response):
        new_url = response.xpath("//a[@data-path='special/report/politic/fincrisis']/@href").extract()
        for url in new_url:
            news_url = response.urljoin(url)
            yield scrapy.Request(news_url, callback=self.parse_news_detail)

    def parse_news_detail(self, response):
        item = ZaobaoItem()
        item['title'] = response.xpath("//h1/text()").extract_first()
        item['dt'] = response.xpath("//span[@class='datestamp date-published meta-date-published']/text()").extract()[1].strip()
        item['body'] = ''.join(i for i in response.xpath("//div[@class='article-content-container']/p/text()").extract())
        item['link'] = response.url

        yield item
