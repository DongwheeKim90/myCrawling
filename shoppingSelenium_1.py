from selenium import webdriver  # Import the Selenium WebDriver module (Selenium WebDriver 모듈 임포트)
from selenium.webdriver.chrome.service import Service  # Import Chrome driver service to manage driver instance (Chrome 드라이버 인스턴스 관리용 서비스 임포트)
from selenium.webdriver.common.by import By  # Provide locator strategies like ID, CLASS_NAME, CSS_SELECTOR, etc. (요소 탐색 전략 제공)
from selenium.webdriver.support.ui import WebDriverWait  # Wait for certain conditions to be met (조건이 만족될 때까지 기다리는 유틸리티)
from selenium.webdriver.support import expected_conditions as EC  # Conditions used with WebDriverWait (WebDriverWait에서 사용할 조건들 정의)
from selenium.webdriver.common.keys import Keys  # Simulate keyboard input like ENTER (키보드 입력을 시뮬레이션할 때 사용)
import os
import pyperclip  # Copy and paste using clipboard (클립보드 기능을 통한 복사/붙여넣기)
import time  # Pause execution for a given time (지정 시간 동안 코드 실행 일시 중지)

# Set Chrome browser options (Chrome 브라우저 옵션 설정)
myOptions = webdriver.ChromeOptions()
myOptions.add_argument("no-sandbox")  # Disable Chrome sandbox for compatibility (보안 샌드박스 비활성화)

# Define ChromeDriver path and service (ChromeDriver 경로 및 서비스 정의)
myService = Service("./chromedriver-win64/chromedriver-win64/chromedriver.exe")

# Launch Chrome browser with options and service (옵션 및 서비스로 Chrome 브라우저 실행)
myBrowser = webdriver.Chrome(service=myService, options=myOptions)

# Maximize the browser window (브라우저 창 최대화)
myBrowser.maximize_window()

# Define explicit wait durations (명시적 대기를 위한 대기 시간 설정)
short_wait = WebDriverWait(myBrowser, 3)  # Short wait: 3 seconds (짧은 대기: 3초)
long_wait = WebDriverWait(myBrowser, 10)  # Long wait: 10 seconds (긴 대기: 10초)

# Initial delay to allow browser to fully load (브라우저가 완전히 로드되도록 5초 대기)
time.sleep(5)

# Open Naver Shopping homepage (네이버 쇼핑 메인 페이지 열기)
myBrowser.get("https://shopping.naver.com/ns/home")
print("Enter web!")  # Confirmation message (웹 진입 확인 메시지)

# Wait for search input box to load (검색창이 로드될 때까지 대기)
product_inputBox = short_wait.until(EC.presence_of_element_located((
    By.CSS_SELECTOR, "input._searchInput_search_text_83jy9._searchInput_placeholder_AG5yA._nlog_click"
)))
# input._searchInput_search_text_83jy9... 는 입력창의 class 이름들입니다 (브라우저 개발자 도구로 확인 가능)
product_inputBox.send_keys("iphone case\n")  # Type "iphone case" and press Enter (검색어 입력 후 Enter 키 입력)
print("input product name complete!")  # 로그 출력
time.sleep(5)  # 검색 결과 로딩 대기

# Wait for the first product title to be visible (첫 번째 상품 제목이 보일 때까지 대기)
searchingProds_1 = long_wait.until(EC.visibility_of_element_located((
    By.CSS_SELECTOR, "strong[class^='basicProductCardInformation_title__Bc_Ng']"
)))
# class^="..." 는 '해당 class 속성이 특정 문자열로 시작하는 요소'를 의미합니다.
# 예: class="basicProductCardInformation_title__Bc_Ng123" 도 매칭됨
# class^='...' => "starts with" operator in CSS selector (CSS 선택자에서 '시작하는 문자열'을 의미)
print(searchingProds_1.text)  # 첫 번째 상품명 출력
print("===========================================================================")

# Prepare a list to collect product titles (상품명 저장용 리스트 준비)
pd_list = list()

# Find all product title elements (모든 상품 제목 요소 탐색)
searchingProds_2 = myBrowser.find_elements(By.CSS_SELECTOR, "strong[class^='basicProductCardInformation_']")
# 이 선택자도 class 이름이 basicProductCardInformation_ 으로 시작하는 요소들을 찾습니다
# 예: class="basicProductCardInformation_title__Bc_Ng", class="basicProductCardInformation_price__123" 등 모두 포함됨

# Extract text from each element and add to the list (각 요소에서 텍스트 추출 후 리스트에 추가)
for v in searchingProds_2:
    pd_list.append(v.text)
# Output the number of products and list content (상품 개수 및 목록 출력)
print(f"Product COUNT : {len(pd_list)}")
print(pd_list)


# Pause before closing the browser (결과 확인을 위해 브라우저 닫기 전 대기)
time.sleep(10)

# Close the browser (브라우저 종료)
myBrowser.close()