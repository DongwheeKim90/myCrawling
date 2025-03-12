# 라이브러리 호출
# Import required libraries
import requests as req
from bs4 import BeautifulSoup as bs

# 네이버 금융 인기 검색 종목 URL 설정
# Set the target URL for Naver Finance popular stock search
targetUrl = "https://finance.naver.com/sise/lastsearch2.naver"

# HTTP GET 요청을 보내 웹페이지의 HTML을 가져옴
# Send an HTTP GET request to fetch the webpage HTML
res = req.get(targetUrl)

# BeautifulSoup을 사용하여 HTML 파싱
# Parse the HTML using BeautifulSoup
soup = bs(res.text, "html.parser")

# 기업명, 주가, 변동률을 저장할 리스트 초기화
# Initialize lists to store company names, stock prices, and price change rates
company_list = list()
company_price_list = list()
price_rate_list = list()

# "table.type_5" 클래스를 가진 테이블의 모든 행(<tr>)을 선택
# Select all rows (<tr>) from the table with class "type_5"
for v in soup.select("table.type_5 tr"):

    # 각 행에서 기업명을 포함하는 <td> 내부의 <a> 태그 선택
    # Select the <a> tag containing the company name inside a <td>
    company_name = v.select_one("td a.tltle")

    # 기업명이 존재하는 경우에만 데이터를 추가
    # Proceed only if the company name element exists
    if company_name:

        # 기업명 텍스트를 가져와 리스트에 추가
        # Extract company name text and add it to the list
        company_name = company_name.get_text(strip=True)
        company_list.append(company_name)

        # 네 번째 <td> 태그에서 주가를 가져와 ',' 제거 후 정수로 변환하여 리스트에 추가
        # Extract stock price from the 4th <td>, remove commas, convert to int, and add to the list
        company_price = int(v.select_one(":nth-child(4)").get_text(strip=True).replace(",", ""))
        company_price_list.append(company_price)

        # 여섯 번째 <td> 태그에서 변동률을 가져와 소수점과 '%' 제거 후 정수로 변환하여 리스트에 추가
        # Extract fluctuation rate from the 6th <td>, remove '.' and '%', convert to int, and add to the list
        fluctuation_rate = int(v.select_one(":nth-child(6)").get_text(strip=True).replace(".", "").replace("%", ""))
        price_rate_list.append(fluctuation_rate)

        # 기업명, 주가, 전일 대비 변동률 출력
        # Print company name, stock price, and fluctuation rate
        print(f"기업명 : {company_name}, 주가 : {company_price} 원, 전일대비 : {fluctuation_rate} %")
