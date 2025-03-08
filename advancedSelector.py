from bs4 import BeautifulSoup as bs  # Import BeautifulSoup to parse HTML
import requests as req  # Import requests to send HTTP requests

# Prompt the user to enter a product name for search
searchPd = input("Please input the product name you want to search\t:\t")

# Insert the search keyword into the Naver Shopping search URL
enterUrl = f'''https://search.shopping.naver.com/ns/search?query={searchPd}'''
print(f"Entered link : {enterUrl}")  # Display the generated search URL

# Send an HTTP GET request to retrieve the webpage's HTML data (with a User-Agent to prevent request blocking)
res = req.get(enterUrl, headers={"User-agent": "Mozilla/5.0"})

# Parse the HTML using BeautifulSoup
soup = bs(res.text, "html.parser")

# Find the <ul> tag containing the product list (based on the specified class name)
target_area = soup.select_one("ul.compositeCardList_product_list__Ih4JR")

# Extract a list of <div> tags containing individual product cards within the <ul> tag
search_pds = target_area.select("div.basicProductCard_basic_product_card__TdrHT")

# Create lists to store product information
pd_link_list = list()       # List to store product URLs
pd_name_list = list()       # List to store product names
pd_price_list = list()      # List to store product prices
pd_discount_list = list()   # List to store discount rates

# Iterate through the retrieved product list and extract individual product information
for i, v in enumerate(search_pds):

    i += 1  # Product number (starting from 1)

    # Extract the individual product page URL (get the href attribute from the <a> tag)
    individual_pd_url = v.select_one("a").get("href")
    pd_link_list.append(individual_pd_url)  # Add URL to the list

    # Extract the product name (get the text from the <strong> tag with the specified class)
    individual_pd_name = v.select_one("strong.basicProductCardInformation_title__Bc_Ng").get_text(strip=True)
    pd_name_list.append(individual_pd_name)  # Add product name to the list

    # Find <span> tags containing price information (filtering by class name "priceTag_price_area__iHlni")
    price_info = v.select("div.basicProductCardInformation_wrap_price__largu span.priceTag_price_area__iHlni")

    # Since multiple price elements may exist, process them using a loop
    for p in price_info:
        price_info = p.get_text(strip=True)  # Extract price information as text

        # If "할인" (discount) is included in the price information (indicating a discounted price)
        if "할인" in price_info:
            # Split the text by "할인" and extract the discounted price
            product_price = int(price_info.split("할인")[1][:-1].replace(",", ""))
            pd_price_list.append(product_price)  # Add the discounted price to the list

            # Extract the discount rate (which appears before "할인")
            discount_rate = price_info.split("할인")[0][:-1]
            pd_discount_list.append(discount_rate)  # Add the discount rate to the list

        # If there is no discount information (regular price is displayed)
        else:
            # Extract the original price by splitting the text at "원"
            product_price = int(price_info.split("원")[0][:-1].replace(",", ""))
            pd_price_list.append(product_price)  # Add the regular price to the list

            discount_rate = 0  # No discount (0%)
            pd_discount_list.append(discount_rate)  # Add 0 to the discount rate list

    # Print individual product information
    print("=================================================================")
    print(f"Product Number : {i}")
    print(f"Product Name : {individual_pd_name}")
    print(f"Discount Rate : {discount_rate} %")
    print(f"Product Price : {product_price}")
    print(f"Product Link : {individual_pd_url}")