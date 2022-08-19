import scrapy


class ImdbSpider(scrapy.Spider):
    name = 'imdb' 
    start_urls = ['https://www.imdb.com/chart/top/']

    def parse(self, response):
        for movies in response.css('.titleColumn'):
            yield{
                'title' : movies.css('.titleColumn a::text').get(),
                'years' : movies.css('.secondaryInfo::text').get()[1:-1],
                'rating' : response.css('strong::text').get()
            }