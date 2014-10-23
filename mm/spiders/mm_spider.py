#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import scrapy
import codecs

from mm.items import MmItem

class MmSpider(scrapy.Spider):
    name = "mm"
    allowed_domains = ["medievalesartesanos.com"]
    start_urls = [
        "http://www.medievalesartesanos.com/buscar-ferias-mercados-medievales/-"
        #"http://www.medievalesartesanos.com/buscar-ferias-mercados-medievales/-/ALICANTE"
        #"http://www.medievalesartesanos.com/buscar-ferias-mercados-medievales/-/VALENCIA",
        #"http://www.medievalesartesanos.com/buscar-ferias-mercados-medievales/-/CASTELL%C3%93N",
        #"http://www.medievalesartesanos.com/buscar-ferias-mercados-medievales/-/MURCIA"
    ]

    provincias ={ 'LAVA': 1 ,
                  'ALBACETE':  2,
                  'ALICANTE':  3,
                  'ALMERA':  4,
                  'ASTURIAS':  33,
                  'VILA':  05,
                  'BADAJOZ':  06,
                  'BARCELONA':  8,
                  'BURGOS':  9,
                  'CCERES':  10,
                  'CDIZ':  11,
                  'CANTABRIA':  39,
                  'CASTELLN':  12,
                  'CEUTA':  51,
                  'CIUDAD REAL':  13,
                  'CRDOBA':  14,
                  'CUENCA':  16,
                  'GERONA':  17,
                  'GRANADA':  18,
                  'GUADALAJARA':  19,
                  'GUIPZCUA':  20,
                  'HUELVA':  21,
                  'HUESCA':  22,
                  'ISLAS BALEARES':  07,
                  'JAN':  23,
                  'LA CORUÑA':  15,
                  'LA RIOJA':  26,
                  'LAS PALMAS':  35,
                  'LEN':  24,
                  'LRIDA':  25,
                  'LUGO':  27,
                  'MADRID':  28,
                  'MLAGA':  29,
                  'MURCIA':  30,
                  'NAVARRA':  31,
                  'ORENSE':  32,
                  'PALENCIA':  34,
                  'PONTEVEDRA':  36,
                  'SALAMANCA':  37,
                  'SANTA CRUZ DE TENERIFE':  38,
                  'SEGOVIA':  40,
                  'SEVILLA':  41,
                  'SORIA':  42,
                  'TARRAGONA':  43,
                  'TERUEL':  44,
                  'TOLEDO':  45,
                  'VALENCIA':  46,
                  'VALLADOLID':  47,
                  'VIZCAYA':  48,
                  'ZAMORA':  49,
                  'ZARAGOZA':  50
                  }

    def parse(self, response):

        for sel in response.xpath('//table/tr'):
            row = sel.xpath('td/text()').extract()
            if len(row) > 0:
                my_item = MmItem();
                my_item['ciudad'] = row[0]

                my_item['provincia'] = row[1]
                provincia = my_item['provincia'].encode('ascii', 'ignore')
                my_item['provincia'] = self.provincias[provincia]

                my_item['nombre'] = row[4]
                my_item['detalles'] = "-"

                afecha = row[2].split("/")
                if len(afecha) == 3 :
                    my_item['fecha_inicio'] = afecha[2] + "-" +afecha[1] + "-" +afecha[0]
                else:
                    continue;


                afecha = row[3].split("/") 
                if len(afecha) == 3 :
                    my_item['fecha_fin'] = afecha[2] + "-" +afecha[1] + "-" +afecha[0]
                else:
                    continue;
               
                yield my_item

