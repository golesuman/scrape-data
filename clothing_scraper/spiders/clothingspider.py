import scrapy
from ..items import ClothingScraperItem
from ..itemloaders import ClothingLoader

class ClothingspiderSpider(scrapy.Spider):
    name = 'clothingspider'
    # allowed_domains = ['test.com']
    start_urls = ['https://www.sastodeal.com/mens-fashion/clothing.html']
    page_no = 1

    def parse(self, response):
        item = ClothingScraperItem()
        products = response.css("div.product.details.product-item-details")
        for product in products:
            cloth = ClothingLoader(item=item, selector=product)
            cloth.add_css("name", "a.product-item-link::text")
            cloth.add_css("price","span.price::text")
            yield cloth.load_item()

        self.page_no += 1
        next_page = 'https://www.sastodeal.com/mens-fashion/clothing.html?p=' + str(self.page_no)
        if next_page:
            yield response.follow(url=next_page, callback=self.parse)
        