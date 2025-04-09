from selenium import webdriver  # Import the Selenium WebDriver module (Selenium WebDriver 모듈 임포트)
from selenium.webdriver.chrome.service import Service  # Import the Chrome driver service manager (Chrome 드라이버 서비스 매니저 임포트)
from selenium.webdriver.common.by import By  # Import locator strategies (요소 탐색 전략 클래스 임포트)
from selenium.webdriver.support.ui import WebDriverWait  # Import explicit wait utility (명시적 대기를 위한 WebDriverWait 임포트)
from selenium.webdriver.support import expected_conditions as EC  # Import expected conditions (기대 조건 클래스 임포트)
from selenium.webdriver.common.keys import Keys  # Import keyboard key constants (키보드 키 입력 상수 임포트)
import os
import pyperclip  # Import clipboard utility (클립보드 기능을 위한 모듈)
import time  # Import time module for delays (지연을 위한 time 모듈 임포트)
import pandas as pd  # Import pandas for data storage and analysis (데이터 저장 및 분석을 위한 pandas 모듈 임포트)

# Set Chrome options (Chrome 브라우저 옵션 설정)
optionSet = webdriver.ChromeOptions()
optionSet.add_argument("no-sandbox")  # Disable sandbox mode (샌드박스 모드 비활성화)

# Start Chrome with defined service and options (정의된 서비스와 옵션으로 Chrome 실행)
myChrome = Service("./chromedriver-win64/chromedriver-win64/chromedriver.exe")
myChrome = webdriver.Chrome(service=myChrome, options=optionSet)
myChrome.maximize_window()  # Maximize browser window (브라우저 창 최대화)

# Set wait time for elements (요소 대기 시간 설정)
myWait = WebDriverWait(myChrome, 3)
time.sleep(2)  # Initial loading buffer (초기 로딩 대기)

# === Utility functions for element interaction (요소 탐색을 위한 유틸리티 함수 정의) ===

def find_present(css_value):  # Wait until element is present in DOM (요소가 DOM에 존재할 때까지 대기)
    return myWait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_value)))

def finds_present(css_value):  # Wait and return multiple present elements (존재 확인 후 여러 요소 반환)
    find_present(css_value)
    return myChrome.find_elements(By.CSS_SELECTOR, css_value)

def find_visible(css_value):  # Wait until element is visible (요소가 화면에 보일 때까지 대기)
    return myWait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, css_value)))

def finds_visible(css_value):  # Wait and return multiple visible elements (보이는 여러 요소 반환)
    find_visible(css_value)
    return myChrome.find_elements(By.CSS_SELECTOR, css_value)

# === Component options mapping for Danawa (다나와 조립 PC의 부품 옵션 번호 매핑) ===
pcOptions = {
    "CPU": "873",
    "mainBoard": "875",
    "memory": "874",
    "graphicCard": "876",
    "ssd": "32617",
    "case": "879",
    "power": "880"
}

# Prepare lists for product data (데이터 저장용 리스트 선언)
pcOptions_list = list(pcOptions.keys())  # 옵션 이름 리스트

# Lists for ad products (광고 상품 리스트)
prodCompany_ad_list = []
prodName_ad_list = []
prodPrice_ad_list = []

# Lists for non-ad products (비광고 상품 리스트)
prodCompany_not_ad_list = []
prodName_not_ad_list = []
prodPrice_not_ad_list = []

# === Access the Danawa page (다나와 조립 PC 페이지 접속) ===
myChrome.get("https://shop.danawa.com/virtualestimate/?controller=estimateMain&methods=index&marketPlaceSeq=16")
myChrome.execute_script("window.scrollTo(0,1400)")  # Scroll down to load component area (옵션 선택 영역까지 스크롤)
time.sleep(5)  # Wait for full page and options to load (페이지 및 옵션 로딩 대기)

# === Loop through each PC component option (각 조립PC 부품 옵션 반복) ===
for v in range(len(pcOptions_list)):
    current_page = 1  # Reset page count for each option (옵션별 페이지 초기화)
    print(f"Current Option: {pcOptions_list[v]}")

    # Click on the current component option (해당 부품 옵션 클릭)
    prod_option_detail = pcOptions.get(pcOptions_list[v])
    find_visible(f"dd[class^='category_{prod_option_detail}']").click()
    print(f"{pcOptions_list[v]} 클릭 및 접속완료!")
    time.sleep(5)

    # Loop through product pages (해당 옵션의 여러 페이지 반복)
    while True:
        print(f"Current Page : {current_page}")

        # === Collect product name & price data (상품명 및 가격 수집) ===
        prodName_not_ad = finds_visible("tr[class^='productList_']> td.title_price > p.subject")  # 일반 제품명
        prodPirce_not_ad = finds_visible("tr[class^='productList_']> td.rig_line > p.low_price > span.prod_price")  # 일반 가격
        prodName_ad = finds_visible("tr[class^='recom_area']> td.title_price > p.subject")  # 광고 제품명
        prodPrice_ad = finds_visible("tr[class^='recom_area']> td.rig_line > p.low_price > span.prod_price")  # 광고 가격

        # Store ad product info (광고 제품 정보 저장)
        for v in prodName_ad:
            prodName_ad_list.append(v.text)
            prodCompany_ad = v.text.split(" ")[0]
            prodCompany_ad_list.append(prodCompany_ad)
        for v in prodPrice_ad:
            price = v.text.strip()
            if "판매준비" in price:
                prodPrice_ad_list.append("판매준비")
            else:
                prodPrice_ad_list.append(price.replace(",", "") + "원")

        # Store non-ad product info (비광고 제품 정보 저장)
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

        # === Pagination: Try next page (다음 페이지 존재 시 이동) ===
        try:
            current_page += 1
            if current_page > 3:
                print("✅ 페이지 3 도달 - 다음 옵션으로 이동")  # 3페이지까지만 탐색
                break

            pageNum_next = find_visible(f"li.pagination-box__item[page='{current_page}'] a")
            pageNum_next.click()
            print(f"➡ Next page ({current_page}) click complete!")
            time.sleep(3)
        except:
            print("❌ There isn't next button.")  # 다음 페이지 없음
            break

# === Print result summary (결과 요약 출력) ===
print(len(prodName_ad_list))
print(prodCompany_ad_list)
print(prodName_ad_list)
print(prodPrice_ad_list)

print(len(prodName_not_ad_list))
print(prodCompany_not_ad_list)
print(prodName_not_ad_list)
print(prodPrice_not_ad_list)

# === Save to CSV (CSV로 저장) ===

# Cut to shortest length to avoid mismatch error (길이 불일치 방지)
min_len_ad = min(len(prodCompany_ad_list), len(prodName_ad_list), len(prodPrice_ad_list))
prod_ad_df = pd.DataFrame({
    "Company name": prodCompany_ad_list[:min_len_ad],
    "Product name": prodName_ad_list[:min_len_ad],
    "Product price": prodPrice_ad_list[:min_len_ad]
})
prod_ad_df.to_csv("./seleniumDF/AD_prod.csv", index=False, encoding="utf-8-sig")  # 광고 제품 CSV 저장

min_len_not_ad = min(len(prodCompany_not_ad_list), len(prodName_not_ad_list), len(prodPrice_not_ad_list))
prod_not_ad_df = pd.DataFrame({
    "Company name": prodCompany_not_ad_list[:min_len_not_ad],
    "Product name": prodName_not_ad_list[:min_len_not_ad],
    "Product price": prodPrice_not_ad_list[:min_len_not_ad]
})
prod_not_ad_df.to_csv("./seleniumDF/NonAD_prod.csv", index=False, encoding="utf-8-sig")  # 비광고 제품 CSV 저장

time.sleep(3)
myChrome.close()  # Close the browser (브라우저 종료)