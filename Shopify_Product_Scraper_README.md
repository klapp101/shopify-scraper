
# Shopify Product Scraper - README

## Overview

This script is designed to scrape product data from a Shopify store, specifically from the products JSON endpoint. It fetches product details including title, vendor, product type, and image URL, and generates a descriptive prompt for each product.

## Requirements

- Python 3
- Libraries: `requests`, `pandas`

Install the required libraries using pip:

```bash
pip install requests pandas
```

## Usage

1. **Set the Base URL**:
   - Modify the `base_url` variable to point to the desired Shopify store's products JSON endpoint. 
   - Example: `base_url = "https://example-shopify-store.com/products.json"`

2. **Run the Scraper**:
   - Execute the script to start scraping the products. 
   - The script paginates through the product listings, retrieving up to 250 products per page.
   - It halts when an empty product list is encountered or if there's an HTTP error.

3. **Dataframe Creation**:
   - The scraped data is stored in a Pandas DataFrame.
   - Columns include `title`, `vendor`, `product_type`, and `product_image`. 
   - If a product has no image, `product_image` is set to None.

4. **Generating Product Prompts**:
   - For each product, a descriptive prompt is generated, combining the title, vendor, product type, and a link to the product image.

5. **Output**:
   - The final DataFrame, with all product details and prompts, can be viewed or exported as needed.

## Notes

- **Rate Limiting**: The script includes a delay between requests to avoid overwhelming the server.
- **Error Handling**: Basic error handling is included, primarily focusing on HTTP status codes.
- **Customization**: Modify the script for specific data needs or formatting preferences.
- **Compliance**: Ensure usage of this script is compliant with Shopify's terms of service and legal regulations.
