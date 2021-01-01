# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FoodCrawlerItem(scrapy.Item):
    cate_name = scrapy.Field()
    food_name = scrapy.Field()
    food_url = scrapy.Field()
    calories = scrapy.Field()  # 热量
    fat = scrapy.Field()  # 脂肪
    carbohydrate = scrapy.Field()  # 碳水化合物
    protein = scrapy.Field()  # 蛋白质
    cholesterol = scrapy.Field()  # 胆固醇
    cellulose = scrapy.Field()  # 纤维素
    v_a = scrapy.Field()  # 维a
    v_c = scrapy.Field()  # 维c
    v_e = scrapy.Field()  # 维e
    carotene = scrapy.Field()  # 胡萝卜素
    thiamine = scrapy.Field()  # 硫胺素
    riboflavin = scrapy.Field()  # 核黄素
    niacin = scrapy.Field()  # 烟酸
    magnesium = scrapy.Field()  # 镁
    calcium = scrapy.Field()  # 钙
    iron = scrapy.Field()  # 铁
    zinc = scrapy.Field()  # 锌
    copper = scrapy.Field()  # 铜
    manganese = scrapy.Field()  # 锰
    potassium = scrapy.Field()  # 钾
    phosphorus = scrapy.Field()  # 磷
    sodium = scrapy.Field()  # 钠
    selenium = scrapy.Field()  # 硒
