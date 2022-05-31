import scrapy
import os
import pathlib
import csv
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import ImdbPopularFilmsItem
import numpy as np

class PopularFilmsSpider(CrawlSpider):
    name = 'popular_films'
    allowed_domains = ['www.imdb.com']
    start_urls = ['https://www.imdb.com/chart/moviemeter/']

    if os.path.exists("filmes_mais_populares_imdb.csv"):
        os.remove("filmes_mais_populares_imdb.csv")

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//td[@class="titleColumn"]/a'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        items = ImdbPopularFilmsItem()

        d = response.xpath("//li[@class= 'ipc-inline-list__item']/text()").extract()
        du = "".join(d)
        cf = response.xpath("//span[@class= 'sc-8c396aa2-2 itZqyK']/text()").extract()

        if len(cf) == 1:
            cf.append('Not rated')

        upordown2 = response.xpath("//div[@class= 'sc-f6306ea-4 bhunpA']//svg/@id").extract()

        if len(upordown2) > 2:
            upordown3 = str(upordown2[2])
            upordown1 = upordown3.strip('iconContext-')
        elif len(upordown2) <= 2:
            upordown3 = str(upordown2[0])
            upordown1 = upordown3.strip('iconContext-')

        nome = response.xpath("//h1/text()").get().encode('utf-8')
        # ano = response.xpath("//span[@class= 'sc-8c396aa2-2 itZqyK']/text()").get()
        ano = cf[0]
        nota = response.xpath("//span[@class= 'sc-7ab21ed2-1 jGRxWM']/text()").get()
        duracao = du
        diretor = response.xpath("//a[@class= 'ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link']/text()").get()
        classificacao_do_filme = cf[1]
        imdb_link = response.url
        sinopse = response.xpath("//span[@class= 'sc-16ede01-2 gXUyNh']/text()").get()
        poster_link = response.urljoin(response.xpath("//a[@class= 'ipc-lockup-overlay ipc-focusable']/@href").get())
        popularidade_score = response.xpath("//div[@class= 'sc-edc76a2-1 gopMqI']/text()").get()
        popularidade_tendencia = upordown1



        items['nome'] = nome
        items['ano'] = ano
        items['nota'] = nota
        items['duracao'] = duracao
        items['diretor'] = diretor
        items['classificacao_do_filme'] = classificacao_do_filme
        items['imdb_link'] = imdb_link
        items['sinopse'] = sinopse
        items['poster_link'] = poster_link
        items['popularidade_score'] = popularidade_score
        items['popularidade_tendencia'] = popularidade_tendencia

        yield items

#scrapy crawl popular_films
#scrapy crawl popular_films -o filmes_mais_populares_imdb.csv