from selenium import webdriver  # Import the Selenium WebDriver module (Selenium WebDriver 모듈 임포트)
from selenium.webdriver.chrome.service import Service  # Import the Chrome driver service manager (Chrome 드라이버 서비스 매니저 임포트)
from selenium.webdriver.common.by import By  # Import locator strategies (요소 탐색 전략 클래스 임포트)
from selenium.webdriver.support.ui import WebDriverWait  # Import explicit wait utility (명시적 대기를 위한 WebDriverWait 임포트)
from selenium.webdriver.support import expected_conditions as EC  # Import expected conditions (기대 조건 클래스 임포트)
from selenium.webdriver.common.keys import Keys  # Import keyboard key constants (키보드 키 입력 상수 임포트)
import os
import pyperclip  # Import clipboard utility (클립보드 기능을 위한 모듈)
import time  # Import time module for delays (지연을 위한 time 모듈 임포트)

# Set Chrome browser options (Chrome 브라우저 옵션 설정)
myOptions = webdriver.ChromeOptions()
myOptions.add_argument("no-sandbox")  # Disable Chrome sandbox for compatibility (보안 샌드박스 비활성화)

# Define ChromeDriver path and service (ChromeDriver 경로 및 서비스 정의)
myService = Service("./chromedriver-win64/chromedriver-win64/chromedriver.exe")

# Launch Chrome browser with options and service (옵션과 서비스로 Chrome 브라우저 실행)
myBrowser = webdriver.Chrome(service=myService, options=myOptions)

# Maximize the browser window (브라우저 창 최대화)
myBrowser.maximize_window()

# Define short and long wait durations (짧은 대기/긴 대기 시간 설정)
short_wait = WebDriverWait(myBrowser, 3)  # 3-second wait (3초 대기)
long_wait = WebDriverWait(myBrowser, 10)  # 10-second wait (10초 대기)

# Initial sleep to allow browser to load (브라우저 로딩을 위한 초기 대기)
time.sleep(5)

# Open Naver Shopping homepage (네이버 쇼핑 홈페이지 열기)
myBrowser.get("https://shopping.naver.com/ns/home")
print("Enter web!")  # Indicate that the page has been entered (페이지 진입 메시지 출력)

product_inputBox = short_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input._searchInput_search_text_83jy9._searchInput_placeholder_AG5yA._nlog_click")))
product_inputBox.send_keys("iphone case\n")
print("input product name complete!")
time.sleep(5)

pd_list = list()
#무한 스크롤
# Get initial scroll height before scrolling (스크롤 내리기 전의 높이)
scroll_location = myBrowser.execute_script("return document.body.scrollHeight")
cnt_scroll = 0  # Initialize scroll count (스크롤 횟수 초기화)
print(f"scroll_location {scroll_location}")

while True:
    myBrowser.execute_script("window.scrollTo(0,document.body.scrollHeight)")  # Scroll to bottom (페이지 맨 아래로 스크롤)
    time.sleep(10)  # Wait for content to load (콘텐츠 로딩 대기)

    scroll_height = myBrowser.execute_script("return document.body.scrollHeight")  # Get new scroll height (새로운 스크롤 높이)
    print(f"scroll height {scroll_height}")
    # Find product titles (상품 제목 요소들 찾기)
    searchingProds = myBrowser.find_elements(By.CSS_SELECTOR, "strong[class^='basicProductCardInformation_']")
    for v in searchingProds:
        pd_list.append(v.text)

    cnt_scroll += 1  # Increase scroll count (스크롤 횟수 증가)

    # If scroll height hasn't changed, stop (스크롤 높이에 변화가 없으면 종료)
    if scroll_location == scroll_height:
        print("✅ Complete scrolling to the bottom!")
        print(f"Total scrolls: {cnt_scroll}")
        break

    scroll_location = scroll_height  # Update scroll position (스크롤 위치 갱신)
    time.sleep(2)  # Short delay before next scroll (다음 스크롤 전 짧은 대기)


print(f"Product COUNT : {len(pd_list)}")
print(pd_list)


time.sleep(5)

# Close the browser (브라우저 종료)
myBrowser.close()