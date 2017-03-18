# -*- coding: utf-8 -*-
import scrapy
import json


class CarparksSpider(scrapy.Spider):
    name = "carparks"
    allowed_domains = ["http://en.parkopedia.co.uk/"]
    start_urls = [
#        'http://en.parkopedia.co.uk/parking/London/',
        'http://en.parkopedia.co.uk/parking/Manchester/',
#        'http://en.parkopedia.co.uk/parking/Birmingham/',
#        'http://en.parkopedia.co.uk/parking/Wolverhampton/',
#        'http://en.parkopedia.co.uk/parking/Leeds/',
#        'http://en.parkopedia.co.uk/parking/Bradford/',
#        'http://en.parkopedia.co.uk/parking/Glasgow/',
#        'http://en.parkopedia.co.uk/parking/Southampton/',
#        'http://en.parkopedia.co.uk/parking/Portsmouth/',
#        'http://en.parkopedia.co.uk/parking/Liverpool/',
#        'http://en.parkopedia.co.uk/parking/Newcastle/',
#        'http://en.parkopedia.co.uk/parking/Nottingham/',
#        'http://en.parkopedia.co.uk/parking/Sheffield/',
#        'http://en.parkopedia.co.uk/parking/Bristol/',
#        'http://en.parkopedia.co.uk/parking/Belfast/',
#        'http://en.parkopedia.co.uk/parking/Leicester/',
#        'http://en.parkopedia.co.uk/parking/Cardiff/',
    ]

    def parse(self, response):
        items = []
        page = response.url.split("/")[-2]
        filename = 'carparks-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
        data = response.xpath(
            "//div [@id='App']/div/@data-react-props").extract()
        carparks = json.loads(data[0])['locations']['all']
        for c in carparks:
            details = [f for f in c['features'] if not f['geometry']]
            for d in details:
                # print(d)
                if 'name' in d['properties']:
                    name = d['properties']['name']
                else:
                    name = "-"
                if 'capacity' in d['properties']:
                    capacity = d['properties']['capacity']
                else:
                    capacity = 1
                if 'max_height' in d['properties']:
                    max_height = d['properties']['max_height']
                else:
                    max_height = 999
                if 'typeid' in d['properties']:
                    typeid = d['properties']['typeid']
                else:
                    typeid = "-"
                if 'city' in d['properties']:
                    city = d['properties']['city']
                else:
                    city = "-"
                items.append((city, name, typeid, capacity, max_height))
        for i in items:
            print(i)
        pass
