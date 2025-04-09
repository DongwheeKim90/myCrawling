# Import the Selenium WebDriver module
# Selenium WebDriver 모듈 임포트
from selenium import webdriver

# Import the Chrome driver service manager
# Chrome 드라이버 서비스 매니저 임포트
from selenium.webdriver.chrome.service import Service

# Import locator strategies
# 요소 탐색 전략 클래스 임포트
from selenium.webdriver.common.by import By

# Import explicit wait utility
# 명시적 대기를 위한 WebDriverWait 임포트
from selenium.webdriver.support.ui import WebDriverWait

# Import expected conditions
# 기대 조건 클래스 임포트
from selenium.webdriver.support import expected_conditions as EC

# Import keyboard key constants
# 키보드 키 입력 상수 임포트
from selenium.webdriver.common.keys import Keys

# Import system-level utilities
# 시스템(파일 경로 등) 관련 기능 제공 모듈 임포트
import os

# Import clipboard utility
# 클립보드 기능을 위한 모듈 임포트
import pyperclip

# Import time module for delays
# 지연을 위한 time 모듈 임포트
import time

# Import pandas for data storage and analysis
# 데이터 저장 및 분석을 위한 pandas 모듈 임포트
import pandas as pd

# Set Chrome browser options
# Chrome 브라우저 옵션 설정
optionSet = webdriver.ChromeOptions()
# Disable sandbox mode for compatibility
# 샌드박스 모드 비활성화 (일부 환경에서 충돌 방지)
optionSet.add_argument("no-sandbox")

# Start Chrome browser with specified service and options
# 정의된 서비스와 옵션으로 Chrome 브라우저 실행
myChrome = Service("./chromedriver-win64/chromedriver-win64/chromedriver.exe")
myChrome = webdriver.Chrome(service=myChrome, options=optionSet)

# Maximize the browser window
# 브라우저 창 최대화
myChrome.maximize_window()

# Set explicit wait object with 3 seconds timeout
# 3초의 명시적 대기 객체 설정
myWait = WebDriverWait(myChrome, 3)

# Wait for initial page load
# 초기 페이지 로딩 대기
time.sleep(2)

# === Utility functions for element interaction ===
# === 요소 탐색을 위한 유틸리티 함수 정의 ===

# Wait until element is present in the DOM
# 요소가 DOM에 존재할 때까지 대기
def find_present(css_value):
    return myWait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_value)))

# Wait and return multiple present elements
# 여러 개의 DOM 요소가 존재하는지 확인 후 반환
def finds_present(css_value):
    find_present(css_value)
    return myChrome.find_elements(By.CSS_SELECTOR, css_value)

# Wait until element is visible
# 요소가 화면에 보일 때까지 대기
def find_visible(css_value):
    return myWait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, css_value)))

# Wait and return multiple visible elements
# 여러 개의 보이는 요소가 있을 때까지 대기 후 반환
def finds_visible(css_value):
    find_visible(css_value)
    return myChrome.find_elements(By.CSS_SELECTOR, css_value)

# === Component category mapping for Danawa PC builder ===
# === 다나와 조립 PC의 부품 옵션 번호 매핑 ===
pcOptions = {
    "CPU": "873",
    "mainBoard": "875",
    "memory": "874",
    "graphicCard": "876",
    "ssd": "32617",
    "case": "879",
    "power": "880"
}

# Create list of component option names
# 부품 옵션 이름 리스트 생성
pcOptions_list = list(pcOptions.keys())

# Lists to store ad product data
# 광고 제품 데이터를 저장할 리스트
prodCompany_ad_list = []
prodName_ad_list = []
prodPrice_ad_list = []

# Lists to store non-ad product data
# 비광고 제품 데이터를 저장할 리스트
prodCompany_not_ad_list = []
prodName_not_ad_list = []
prodPrice_not_ad_list = []

# Navigate to Danawa PC builder page
# 다나와 조립 PC 페이지 접속
myChrome.get("https://shop.danawa.com/virtualestimate/?controller=estimateMain&methods=index&marketPlaceSeq=16")

# Scroll to component option area
# 부품 옵션 영역까지 스크롤
myChrome.execute_script("window.scrollTo(0,1400)")

# Wait for components to fully load
# 부품 항목들이 모두 로딩될 때까지 대기
time.sleep(5)

# === Iterate through each PC component ===
# === 각 조립PC 부품 옵션 반복 ===
for v in range(len(pcOptions_list)):
    # Reset current page to 1
    # 현재 페이지 번호 초기화
    current_page = 1
    print(f"Current Option: {pcOptions_list[v]}")

    # Click on component option
    # 해당 부품 옵션 클릭
    prod_option_detail = pcOptions.get(pcOptions_list[v])
    find_visible(f"dd[class^='category_{prod_option_detail}']").click()
    print(f"{pcOptions_list[v]} 클릭 및 접속완료!")
    time.sleep(5)

    # Loop through pages of product listings
    # 부품 옵션의 상품 리스트 페이지 반복
    while True:
        print(f"Current Page : {current_page}")

        # Find non-ad product names
        # 비광고 상품명 수집
        prodName_not_ad = finds_visible("tr[class^='productList_']> td.title_price > p.subject")
        # Find non-ad product prices
        # 비광고 가격 수집
        prodPirce_not_ad = finds_visible("tr[class^='productList_']> td.rig_line > p.low_price > span.prod_price")

        # Find ad product names
        # 광고 상품명 수집
        prodName_ad = finds_visible("tr[class^='recom_area']> td.title_price > p.subject")
        # Find ad product prices
        # 광고 가격 수집
        prodPrice_ad = finds_visible("tr[class^='recom_area']> td.rig_line > p.low_price > span.prod_price")

        # Store ad product information
        # 광고 제품 정보 저장
        for v in prodName_ad:
            prodName_ad_list.append(v.text)
            prodCompany_ad = v.text.split(" ")[0]  # First word = manufacturer
            # 첫 번째 단어를 제조사로 저장
            prodCompany_ad_list.append(prodCompany_ad)

        for v in prodPrice_ad:
            price = v.text.strip()
            if "판매준비" in price:
                # If not for sale yet
                # 아직 판매 준비 중이라면
                prodPrice_ad_list.append("판매준비")
            else:
                prodPrice_ad_list.append(price.replace(",", "") + "원")  # Remove commas and add "원"

        # Store non-ad product information
        # 비광고 제품 정보 저장
        for v in prodName_not_ad:
            prodName_not_ad_list.append(v.text)
            prodCompany_not_ad = v.text.split(" ")[0]
            prodCompany_not_ad_list.append(prodCompany_not_ad)

        for v in prodPirce_not_ad:
            price = v.text.strip()
            if "판매준비" in price:
                prodPrice_not_ad_list.append("판매준비")
            else:
                prodPrice_not_ad_list.append(price.replace(",", "") + "원")

        # Try to move to the next page (limit to 3 pages)
        # 다음 페이지로 이동 시도 (최대 3페이지까지)
        try:
            current_page += 1
            if current_page > 3:
                print("✅ 페이지 3 도달 - 다음 옵션으로 이동")
                break

            pageNum_next = find_visible(f"li.pagination-box__item[page='{current_page}'] a")
            pageNum_next.click()
            print(f"➡ Next page ({current_page}) click complete!")
            time.sleep(3)
        except:
            print("❌ There isn't next button.")  # 다음 페이지 없음
            break

# === Print result summary ===
# === 결과 요약 출력 ===
print(len(prodName_ad_list))  # 광고 제품 수
print(prodCompany_ad_list)
print(prodName_ad_list)
print(prodPrice_ad_list)

print(len(prodName_not_ad_list))  # 비광고 제품 수
print(prodCompany_not_ad_list)
print(prodName_not_ad_list)
print(prodPrice_not_ad_list)

# === Save to CSV files ===
# === CSV 파일로 저장 ===

# Shorten lists to same length to avoid mismatch
# 길이 불일치 방지를 위해 최소 길이로 자름
min_len_ad = min(len(prodCompany_ad_list), len(prodName_ad_list), len(prodPrice_ad_list))
prod_ad_df = pd.DataFrame({
    "Company name": prodCompany_ad_list[:min_len_ad],
    "Product name": prodName_ad_list[:min_len_ad],
    "Product price": prodPrice_ad_list[:min_len_ad]
})
# Save ad product data to CSV
# 광고 제품 CSV 저장
prod_ad_df.to_csv("./seleniumDF/AD_prod.csv", index=False, encoding="utf-8-sig")

min_len_not_ad = min(len(prodCompany_not_ad_list), len(prodName_not_ad_list), len(prodPrice_not_ad_list))
prod_not_ad_df = pd.DataFrame({
    "Company name": prodCompany_not_ad_list[:min_len_not_ad],
    "Product name": prodName_not_ad_list[:min_len_not_ad],
    "Product price": prodPrice_not_ad_list[:min_len_not_ad]
})
# Save non-ad product data to CSV
# 비광고 제품 CSV 저장
prod_not_ad_df.to_csv("./seleniumDF/NonAD_prod.csv", index=False, encoding="utf-8-sig")

# Wait briefly before closing the browser
# 브라우저 종료 전 잠깐 대기
time.sleep(3)
# Close the browser
# 브라우저 종료
myChrome.close()
