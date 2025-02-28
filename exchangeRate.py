import requests as req  # Import the requests library for sending HTTP requests
import re  # Import the regular expressions module for pattern matching
import math  # Import the math module for mathematical operations
import datetime  # Import the datetime module for handling date and time

# Define the target website URL (Naver Finance - Market Index page)
target_web = "https://finance.naver.com/marketindex/"

# Send an HTTP GET request to fetch the webpage content
res = req.get(target_web)

# Store the response text (HTML content) in the variable 'body'
body = res.text

# --- Regular Expression: Extracting exchange rate information ---
# Define a regex pattern to search for currency name and exchange rate
# Explanation of the regex pattern:
# - 'h_lst.*?blind\">' : Matches the section containing the currency name
# - '(.*?)' : Captures the currency name (e.g., "USD" for US Dollar)
# - '</span>.*?value\">' : Matches the surrounding HTML structure leading to the exchange rate
# - '(.*?)' : Captures the exchange rate value
# - 're.DOTALL' : Ensures that multi-line text is included in the search scope
# - '?' : Performs a non-greedy match, ensuring a minimal match rather than consuming too much text
searchPattern = re.compile(
    r"h_lst.*?blind\">(.*?)</span>.*?value\">(.*?)</",
    re.DOTALL  # Enables matching across multiple lines
)

# --- Extract values matching the defined regex pattern ---
# The findall() function searches for all occurrences and returns a list of tuples
myCaptures = searchPattern.findall(body)

# Convert the extracted exchange rate to a floating-point number, remove commas, and round up to the nearest integer
today_usdRate = math.ceil(float(myCaptures[0][1].replace(",", "")))

# Get today's date in YYYY-MM-DD format
todayDate = datetime.datetime.today().date()

# --- Display the exchange rate information ---
print("Today's USD exchange rate (unit: Korean Won)")
print(f"{todayDate}\t:\t{today_usdRate}")

# Prompt the user to enter the amount in Korean Won
myWon = int(input("Please enter your won\t:\t"))

# Convert the entered Korean Won amount to USD using the exchange rate and round up
myUsd = math.ceil(myWon / today_usdRate)

# Display the conversion results
print(f"Your WON\t:\t{myWon}")
print(f"Your USD\t:\t{myUsd}")
print("=====================================")
