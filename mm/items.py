# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class MmItem(scrapy.Item):
    nombre = scrapy.Field()
    provincia = scrapy.Field()
    fecha_inicio = scrapy.Field()
    fecha_fin = scrapy.Field()
    ciudad = scrapy.Field()
    detalles = scrapy.Field()
