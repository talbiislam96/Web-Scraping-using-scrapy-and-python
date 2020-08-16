# -*- coding: utf-8 -*-
import scrapy


class JobsSpider(scrapy.Spider):
    
    name = 'jobs'
    allowed_domains = ['tanitjobs.com']
    start_urls = ['https://www.tanitjobs.com/jobs']

    def parse(self, response):
        pass
        
        all_jobs = response.css(".listing-item__jobs")
        
        for job in all_jobs:
            item = {
                'jobname' : job.css("article.listing-item div.listing-item__title a::text").getall(),
                "companyname" : job.css(".listing-item__info--item-company::text").extract(),
                "city" : job.css(".listing-item__info--item-location::text").extract() ,
                "joblink": job.css("article.listing-item div.listing-item__title a::attr(href)").extract(),
                }
        
            yield item

        next_page = response.css(".pad_right_small a::attr(href)").extract_first()
        if next_page:
           next_page = response.urljoin(next_page)
           yield scrapy.Request(url=next_page, callback=self.parse)
        