# 라이브러리 호출
# Import required libraries
import requests as req
from bs4 import BeautifulSoup as bs

# Yahoo Finance에서 가장 많이 거래된 주식 목록 URL
# Yahoo Finance URL for the most active stocks
yahooUrl = "https://finance.yahoo.com/markets/stocks/most-active/"

# HTTP 요청 시 브라우저처럼 인식되도록 User-Agent 설정
# Set User-Agent to mimic a browser and avoid bot detection
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

# HTTP GET 요청을 보내 웹페이지의 HTML을 가져옴
# Send an HTTP GET request to fetch the webpage HTML
res = req.get(yahooUrl, headers=headers)

# BeautifulSoup을 사용하여 HTML을 파싱
# Parse the HTML using BeautifulSoup
soup = bs(res.text, "html.parser")

# 테이블에서 <tbody> 내부의 모든 <tr> 요소 선택 (주식 목록)
# Select all <tr> elements inside <tbody> of the stock table
target_area = soup.select("table tbody tr")

# 각 주식 항목을 반복하며 정보 추출
# Iterate through each stock row and extract information
for v in target_area:
    # 첫 번째 <td>에서 종목 심볼 추출
    # Extract the stock symbol from the first <td>
    company_symbol = v.select_one("td:nth-child(1)").get_text(strip=True)

    # 두 번째 <td>에서 회사명 추출
    # Extract the company name from the second <td>
    company_name = v.select_one("td:nth-child(2)").get_text(strip=True)

    # 네 번째 <td>의 특정 경로에서 현재 주가 추출
    # Extract the current stock price from the fourth <td>
    company_price = v.select_one("td:nth-child(4)>span.yf-hhhli1>div>fin-streamer").get_text(strip=True)

    # 여섯 번째 <td>에서 전일 대비 변동률 추출
    # Extract the change rate compared to the previous day from the sixth <td>
    increase_rate = v.select_one("td:nth-child(6)").get_text(strip=True)

    # 추출한 정보를 포맷하여 출력
    # Print the extracted information in a formatted string
    print(f"{company_name} ({company_symbol}) Price\t:\t{company_price} (Compared to the previous day: {increase_rate})")
