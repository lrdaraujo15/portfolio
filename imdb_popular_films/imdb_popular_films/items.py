# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ImdbPopularFilmsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    nome = scrapy.Field()
    ano = scrapy.Field()
    nota = scrapy.Field()
    duracao = scrapy.Field()
    diretor = scrapy.Field()
    classificacao_do_filme = scrapy.Field()
    imdb_link = scrapy.Field()
    sinopse = scrapy.Field()
    poster_link = scrapy.Field()
    popularidade_score = scrapy.Field()
    popularidade_tendencia = scrapy.Field()
    pass
