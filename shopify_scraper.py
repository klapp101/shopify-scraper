import requests
import pandas as pd
import time
import random

class ShopifyProductScraper:
    def __init__(self, base_url):
        self.base_url = base_url

    def scrape_products(self, limit=250):
        all_products = []
        page = 1

        while True:
            url = f"{self.base_url}?limit={limit}&page={page}"
            response = requests.get(url)
            if response.status_code != 200:
                print(f"Failed to retrieve data: Status code {response.status_code}")
                break

            data = response.json()
            if not data["products"]:
                # Stop if the products list is empty
                break

            all_products.extend(data["products"])
            print(f"Retrieved page {page} with {len(data['products'])} products.")
            page += 1
            time.sleep(random.randint(1, 3))

        return all_products

    def create_dataframe(self, products_data):
        df = pd.DataFrame(products_data)
        df['product_image'] = df['images'].apply(lambda x: x[0]['src'] if len(x) > 0 else None)
        return df[['title', 'vendor', 'product_type', 'product_image']]

    @staticmethod
    def generate_product_prompt(row):
        title = row['title']
        vendor = row['vendor']
        product_type = row['product_type']
        image_url = row['product_image']

        prompt = f"Discover the elegance of '{title}', a premium offering by {vendor}. This {product_type.lower()}, combines unique design with quality craftsmanship."
        return prompt + f" Explore its detailed features in the image here - ({image_url})." if image_url else prompt

# Usage
base_url = "https://qdwatches.com/products.json"
scraper = ShopifyProductScraper(base_url)
products_data = scraper.scrape_products()
df = scraper.create_dataframe(products_data)
df['product_prompt'] = df.apply(ShopifyProductScraper.generate_product_prompt, axis=1)

# Display the first few rows of the DataFrame
print(df.head())
