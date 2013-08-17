#!/usr/bin/python

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from blogcrawler.items import BlogcrawlerItem
from urlparse import urlparse

class BlogSpider(CrawlSpider):    
    name = "blogspider"
    allowed_domains = [
        "wordpress.org", 
        "blogspot.com", 
        "blogger.com",
        "livejournal.com",
        "typepad.com", 
        "tumblr.com"]

    ## TK: Change this so we cna get arguments from the command line
    start_urls = ["http://badhessian.org"]

    curr_url = urlparse(start_urls[0])[1]

    rules = (
        Rule(SgmlLinkExtractor(
            allow=('/', ),
            deny=('www\.blogger\.com', 'profile\.typepad\.com', 
                'http:\/\/wordpress\.com', '[A-Za-z]+\.trac\.wordpress\.com',
                '.+\.wordpress\.org', 'wordpress\.org', 'www\.tumblr\.com', ),
                ), callback = "parse_item", follow = True), 
    )

    def parse_item(self, response):
        item = BlogcrawlerItem()

        item['url1'] = self.curr_url
        item['url2'] = urlparse(response.url)[1]

        self.curr_url = item['url2']

        yield item