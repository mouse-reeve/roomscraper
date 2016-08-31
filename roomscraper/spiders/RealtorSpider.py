''' Crawl realtor.com images '''

import scrapy
from roomscraper.items import ListingItem

class RealtorSpider(scrapy.Spider):
    ''' spider behavior for realtor.com '''
    name = 'realtor'
    allowed_domains = ['realtor.com']
    start_urls = ['http://www.realtor.com/realestateandhomes-search/Houston_TX']

    def parse(self, response):
        ''' process search or listing page '''
        title = response.xpath('//title/text()').extract()[0]

        # check if we're on the search results page
        if 'Houston, TX Real Estate' in title:
            # follow all listing detail links
            try:
                links = response.xpath('//a[contains(@href, "realestateandhomes-detail")]/@href')
            except:
                pass
            else:
                for link in links:
                    yield scrapy.http.Request('http://www.realtor.com' + link.extract())

            # follow next page links
            for link in response.xpath('//a[@class="next"]/@href'):
                yield scrapy.http.Request('http://www.realtor.com' + link.extract())
        else:
            # listing pages
            item = ListingItem()
            item['address'] = title.split(' - ')[0]
            item['url'] = response.url
            item['image_urls'] = []
            try:
                images = response.xpath('//img[@class="owl-lazy"]/@data-src')
                for image in images:
                    item['image_urls'].append(image.extract())
            except:
                pass
            yield item

