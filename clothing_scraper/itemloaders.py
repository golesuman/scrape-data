from itemloaders.processors import TakeFirst, MapCompose
from scrapy.loader import ItemLoader

class ClothingLoader(ItemLoader):
    default_output_processor = TakeFirst()
    price_in = MapCompose(lambda x: x.split("रु")[-1])
    