# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MmItem(scrapy.Item):
    name = scrapy.Field()
    provincia = scrapy.Field()
    fDesde = scrapy.Field()
    fHasta = scrapy.Field()
    ciudad = scrapy.Field()
