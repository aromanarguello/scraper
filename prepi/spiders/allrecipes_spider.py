import scrapy


class AllRecipesSpider(scrapy.Spider):
    name = "all_recipes"
    start_urls = [
        'https://www.myrecipes.com/recipe/turkey-and-swiss-pinwheels']

    def start_request(self):
        urls = [
            'https://www.myrecipes.com/recipe/turkey-and-swiss-pinwheels'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        filename = "test.html"
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
