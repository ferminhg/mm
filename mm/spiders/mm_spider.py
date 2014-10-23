import scrapy

from mm.items import MmItem

class MmSpider(scrapy.Spider):
    name = "mm"
    allowed_domains = ["medievalesartesanos.com"]
    start_urls = [
        "http://www.medievalesartesanos.com/buscar-ferias-mercados-medievales/-"
        #"http://www.medievalesartesanos.com/buscar-ferias-mercados-medievales/-/ALICANTE",
        #"http://www.medievalesartesanos.com/buscar-ferias-mercados-medievales/-/VALENCIA",
        #"http://www.medievalesartesanos.com/buscar-ferias-mercados-medievales/-/CASTELL%C3%93N",
        #"http://www.medievalesartesanos.com/buscar-ferias-mercados-medievales/-/MURCIA"
    ]

    def parse(self, response):
        for sel in response.xpath('//table/tr'):
            row = sel.xpath('td/text()').extract()
            if len(row) > 0:
                my_item = MmItem();
                my_item['ciudad'] = row[0]
                my_item['provincia'] = row[1]
                my_item['fDesde'] = row[2]
                my_item['fHasta'] = row [3]
                my_item['name'] = row[4]
                yield my_item


#            my_item = MmItem()
#            my_item['name'] = item.select('td//text()').extract()
#            my_item['name'] = item.select('td//text()').extract()
#            my_item['fDesde'] = item.select('td//text()').extract()
#            my_item['fHasta'] = item.select('td//text()').extract()
#            my_item['ciudad'] = item.select('td//text()').extract()
#            yield my_item