#!/usr/bin/python

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.item import Item

class BlogSpider(CrawlSpider):
    name = "blogSpider"
    allowed_domains = [
        "wordpress.org", 
        "blogspot.com", 
        "blogger.com",
        "livejournal.com",
        "typepad.com", 
        "tumblr.com"]

    ## TK: Change this so we cna get arguments from the command line
    start_urls = ["http://scatter.wordpress.com"]

    rules = (
        Rule(SgmlLinkExtractor(allow=('/', )))
    )

    def parse(self, response):
        data_dir = "data"
        filename = ""
        open(filename, 'wb').write(response.body)