import requests as req
# Import BeautifulSoup from the BeautifulSoup4 package (requires installation via pip)
# BeautifulSoup is used for parsing HTML and extracting information
from bs4 import BeautifulSoup as bs

# URL of the webpage containing foreign exchange rates
url = "https://finance.naver.com/marketindex/exchangeList.naver"

# Send a GET request to the URL and retrieve the page content as text
res = req.get(url).text

# Parse the HTML content using BeautifulSoup with the 'html.parser'
soup = bs(res, "html.parser")

# Lists to store extracted currency names and their exchange rates
currencyName = list()
currencyValue = list()

# Find all <td> (table data) elements on the webpage
td_values = soup.find_all("td")

# Iterate through all <td> elements to extract currency names
for t in td_values:
    # If the <td> element does not contain an <a> (anchor) tag, skip it
    if len(t.find_all("a")) == 0:
        continue

    # Extract and clean the text inside the <td> element (currency name)
    currencyName_value = t.get_text(strip=True)

    # Append the extracted currency name to the list
    currencyName.append(currencyName_value)

# Iterate through all <td> elements again to extract exchange rates
for t in td_values:
    # Check if the <td> element has a 'class' attribute
    if "class" in t.attrs:
        # If the 'class' attribute contains 'sale', extract the exchange rate
        if "sale" in t.attrs["class"]:
            # Extract and clean the text inside the <td> element (exchange rate)
            currencyValue_value = t.get_text(strip=True)

            # Append the extracted exchange rate to the list
            currencyValue.append(currencyValue_value)

# Print the extracted currency names
print(currencyName)

# Print the extracted exchange rates
print(currencyValue)
