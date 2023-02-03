import re
import pandas as pd

# A sequence of string contains items and prices
experiment = 'I paid 2.00 for apple, 3.50 for banana, 1.20 for potato.'

# Define find price
find_price = re.findall('\d\.\d{2}\s(?=for)', experiment)
print(find_price)

# Define find items
find_item = re.findall('(?<=for)\s\w+', experiment)
print(find_item)

fruit_price = {'fruit': find_item, 'price': find_price}
fruit_price_df = pd.DataFrame(fruit_price)

fruit_price_df['fruit'] = [fruit.strip() for fruit in fruit_price_df['fruit']]
fruit_price_df['price'] = [price.strip() for price in fruit_price_df['price']]

print(fruit_price_df)