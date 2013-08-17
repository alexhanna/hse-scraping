#!/usr/bin/python

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from blogcrawler.items import BlogcrawlerItem
from urlparse import urlparse

class BlogSpider(CrawlSpider):    
    name = "blogspider"
    allowed_domains = [
        "wordpress.com", 
        "blogspot.com", 
        "blogger.com",
        "livejournal.com",
        "typepad.com", 
        "tumblr.com"]

    start_urls = ["http://badhessian.org"]

    rules = (
        Rule(SgmlLinkExtractor(
            allow=('/', ),
            deny=('www\.blogger\.com', 'profile\.typepad\.com', 
                'http:\/\/wordpress\.com', '.+\.trac\.wordpress\.org',
                '.+\.wordpress\.org', 'wordpress\.org', 'www\.tumblr\.com', 
                'en\..+\.wordpress\.com', 'vip\.wordpress\.com'),
                ), callback = "parse_item", follow = True), 
    )

    def parse_item(self, response):
        item = BlogcrawlerItem()

        item['url1'] = urlparse(response.request.headers.get('Referer'))[1]
        item['url2'] = urlparse(response.url)[1]

        yield item