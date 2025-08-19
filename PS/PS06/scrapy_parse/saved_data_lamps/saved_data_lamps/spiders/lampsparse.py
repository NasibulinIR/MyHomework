import scrapy


class LampsParseSpider(scrapy.Spider):
    name = "lampsparse"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet/page-3"]

    def parse(self, response):
        lamps = response.css('div._Ud0k')
        for lamp in lamps:
            yield {
                'Наименование товара':lamp.css('div.lsooF span::text').get(),
                'Цена':lamp.css('div.pY3d2 span::text').get(),
                'Ссылка на товар':lamp.css('a').attrib['href']
            }
# .CVS сформировал через команду scrapy crawl lampsparse -o lamps.csv в консоли терминала