import scrapy
from ..items import ClothingScraperItem

class ClothingspiderSpider(scrapy.Spider):
    name = 'clothingspider'
    # allowed_domains = ['test.com']
    start_urls = ['https://www.sastodeal.com/mens-fashion/clothing/jackets.html']
    page_no = 1

    def parse(self, response):
        item = ClothingScraperItem()
        products = response.css("div.product.details.product-item-details")
        for product in products:
            name = product.css("a.product-item-link::text").get()
            price = product.css("span.price::text").get()
            item['name'] = name
            item['price'] = price
            yield item

        
        next_page = 'https://www.sastodeal.com/mens-fashion/clothing/jackets.html?p=' + str(self.page_no)
        print(next_page)
        if self.page_no < 15:
            self.page_no += 1
            yield response.follow(url=next_page, callback=self.parse)
        