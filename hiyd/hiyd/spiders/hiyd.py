import scrapy
from hiyd.hiyd.items import FoodCrawlerItem


class HiydSpider(scrapy.Spider):
    name = 'hiyd'
    allowed_domains = ['food.hiyd.com']
    start_urls = ['http://food.hiyd.com/']

    def parse(self, response):
        selector = response.xpath('//div[@class="box-bd"]/ul/li')

        for food in selector:
            food_detail = FoodCrawlerItem()
            cate_name = response.xpath('//div[@class="box"]/div[@class="box-hd"]/h2/text()')
            food_detail['cate_name'] = cate_name

            food_name = food.xpath('a/div[@class="cont"]/h3/text()')
            food_detail['food_name'] = food_name

            food_url = food.xpath('a/@href')
            food_detail['food_url'] = food_url

    def parse_detail(self, response):
        selector = response.xpath('//div[@class="nurt-list"]')

        for food_detail in selector:
            food_detail = FoodCrawlerItem()

            calories = food_detail.xpath('ul[not(@class="no-margin")]/li[2]')
            food_detail['calories'] = calories

            fat = food_detail.xpath('ul[not(@class="no-margin")]/li[3]')
            food_detail['fat'] = fat

            carbohydrate = food_detail.xpath('ul[not(@class="no-margin")]/li[4]')
            food_detail['carbohydrate'] = carbohydrate

            protein = food_detail.xpath('ul[not(@class="no-margin")]/li[5]')
            food_detail['protein'] = protein

            cholesterol = food_detail.xpath('ul[not(@class="no-margin")]/li[6]')
            food_detail['cholesterol'] = cholesterol

            cellulose = food_detail.xpath('ul[not(@class="no-margin")]/li[8]')
            food_detail['cellulose'] = cellulose

            v_a = food_detail.xpath('ul[not(@class="no-margin")]/li[9]')
            food_detail['v_a'] = v_a

            v_c = food_detail.xpath('ul[not(@class="no-margin")]/li[10]')
            food_detail['v_c'] = v_c

            v_e = food_detail.xpath('ul[not(@class="no-margin")]/li[11]')
            food_detail['v_e'] = v_e

            carotene = food_detail.xpath('ul[not(@class="no-margin")]/li[12]')
            food_detail['carotene'] = carotene

            thiamine = food_detail.xpath('ul[not(@class="no-margin")]/li[13]')
            food_detail['thiamine'] = thiamine

            riboflavin = food_detail.xpath('ul[not(@class="no-margin")]/li[14]')
            food_detail['riboflavin'] = riboflavin

            niacin = food_detail.xpath('ul[not(@class="no-margin")]/li[15]')
            food_detail['niacin'] = niacin

            magnesium = food_detail.xpath('ul[contains(@class,"no-margin")]/li[2]')
            food_detail['magnesium'] = magnesium

            calcium = food_detail.xpath('ul[contains(@class,"no-margin")]/li[3]')
            food_detail['calcium'] = calcium

            iron = food_detail.xpath('ul[contains(@class,"no-margin")]/li[4]')
            food_detail['iron'] = iron

            zinc = food_detail.xpath('ul[contains(@class,"no-margin")]/li[5]')
            food_detail['zinc'] = zinc

            copper = food_detail.xpath('ul[contains(@class,"no-margin")]/li[6]')
            food_detail['copper'] = copper

            manganese = food_detail.xpath('ul[contains(@class,"no-margin")]/li[7]')
            food_detail['manganese'] = manganese

            potassium = food_detail.xpath('ul[contains(@class,"no-margin")]/li[8]')
            food_detail['potassium'] = potassium

            phosphorus = food_detail.xpath('ul[contains(@class,"no-margin")]/li[9]')
            food_detail['phosphorus'] = phosphorus

            sodium = food_detail.xpath('ul[contains(@class,"no-margin")]/li[10]')
            food_detail['sodium'] = sodium

            selenium = food_detail.xpath('ul[contains(@class,"no-margin")]/li[11]')
            food_detail['selenium'] = selenium

        pass
