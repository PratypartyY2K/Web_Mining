import scrapy

class EcommerceSpider(scrapy.Spider):
   #name of spider
   name = 'shopclues'

   #list of allowed domains
   allowed_domains = ['www.shopclues.com/mobiles-featured-store-4g-smartphone.html']
   #starting url
   start_urls = ['http://www.shopclues.com/mobiles-featured-store-4g-smartphone.html/']
   #location of csv file
   custom_settings = {
       'FEED_URI' : 'Ecommerce/shopclues.csv'
   }


   def parse(self, response):
       #Extract product information
       product_titles = response.css('img::attr(title)').extract()
       product_images = response.css('img::attr(data-img)').extract()
       product_prices = response.css('.p_price::text').extract()
       product_discounts = response.css('.prd_discount::text').extract()


       for item in zip(product_titles,product_prices,product_images,product_discounts):
           scraped_info = {
               'title' : item[0],
               'price' : item[1],
               'image_urls' : [item[2]], #Set's the url for scrapy to download images
               'cdiscount' : item[3]
           }

           yield scraped_info