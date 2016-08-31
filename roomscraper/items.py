''' real estate listing items '''
import scrapy


class ListingItem(scrapy.Item):
    ''' individual real estate listing items '''
    address = scrapy.Field()
    url = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
