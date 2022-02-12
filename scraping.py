import requests
from bs4 import BeautifulSoup
import pandas as pd

url="https://www.croma.com/computers-tablets/laptops/c/20"
baseurl = "https://www.croma.com"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'lxml')

names = []
product_names = soup.find_all(class_ = "product-title plp-prod-title")
for product_name in product_names:
    name = product_name.find("a").contents[0]
    names.append(name)

prices = []
new_product_prices = soup.find_all("span", class_="new-price")
for new_product_price in new_product_prices:
    new_price = new_product_price.text[1:]  
    prices.append(new_price)

product_discounts = []
discounts = soup.find_all("span", class_ = "discount")
for discount in discounts:
    product_discounts.append(discount.text[:3])

df = pd.DataFrame(data={"name": names, "price":prices, "discount":product_discounts})
df.to_csv("product details.csv", index=False)