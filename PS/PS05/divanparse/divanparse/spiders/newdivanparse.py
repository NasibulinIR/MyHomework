import scrapy


class NewdivanparseSpider(scrapy.Spider):
    name = "newdivanparse"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        divans = response.css('div._Ud0k')
        for divan in divans:
            yield {
                'name': divan.css('div.lsooF span::text').get(),
                'price': divan.css('div.pY3d2 span::text').get(),
                'urls': divan.css('a').attrib['href']
            }

