#!/usr/bin/python

from scrapy.spider import BaseSpider

class BlogSpider(BaseSpider):
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

    def parse(self, response):
        filename = response.url.split("/")[-2]
        open(filename, 'wb').write(response.body)