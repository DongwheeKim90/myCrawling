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

# Wait for login button to be visible and click it (로그인 버튼이 보일 때까지 대기 후 클릭)
login_btn = long_wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.gnb_btn_login")))
login_btn.click()
print("Login button click!")  # Login button clicked message (로그인 버튼 클릭 메시지 출력)

# Wait for ID input box, copy and paste ID (ID 입력창 대기 후 ID 복사 및 붙여넣기)
input_myID = short_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input.input_id")))
pyperclip.copy("zion-d")  # Copy ID to clipboard (ID를 클립보드에 복사)
input_myID.send_keys(Keys.CONTROL, "v")  # Paste ID using Ctrl + V (Ctrl + V로 ID 붙여넣기)

# Wait for password input box, copy and paste password (비밀번호 입력창 대기 후 복사 및 붙여넣기)
input_myPW = short_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input.input_pw")))
pyperclip.copy(os.getenv("naverPW"))  # Copy password to clipboard (비밀번호를 클립보드에 복사)
input_myPW.send_keys(Keys.CONTROL, "v")  # Paste password using Ctrl + V (Ctrl + V로 비밀번호 붙여넣기)
input_myPW.send_keys("\n")  # Press Enter to submit (Enter 키로 로그인 제출)
print("Input ID/PW Finish!")  # Login input complete message (ID/PW 입력 완료 메시지)
print("Login Success!")  # Login success message (로그인 성공 메시지)
time.sleep(5)

# Close the browser (브라우저 종료)
myBrowser.close()