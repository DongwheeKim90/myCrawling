from selenium import webdriver  # Import the Selenium WebDriver module (Selenium WebDriver 모듈을 임포트)
from selenium.webdriver.chrome.service import Service  # Import the Chrome driver service manager (Chrome 드라이버 서비스 매니저 임포트)
from selenium.webdriver.common.by import By  # Import the "By" class for element locating strategies (요소 탐색 전략을 위한 By 클래스 임포트)
from selenium.webdriver.support.ui import WebDriverWait  # Import WebDriverWait for explicit waiting (명시적 대기 기능을 위한 WebDriverWait 임포트)
from selenium.webdriver.support import expected_conditions as EC  # Import expected conditions for wait (대기 조건을 정의하는 expected_conditions 임포트)
import time  # Import time module for sleep delays (지연을 위한 time 모듈 임포트)

# Set debugging and browser launch options (디버깅 및 브라우저 실행 시 옵션 설정)
myOptions = webdriver.ChromeOptions()  # Create an instance of ChromeOptions (ChromeOptions 인스턴스 생성)
myOptions.add_argument("no-sandbox")  # Disable Chrome's security sandbox for compatibility (보안 샌드박스를 끄고 호환성 향상)

# Optional window settings (선택 사항: 창 크기 설정)
# myOptions.add_argument("window-size=1000,1000")  # Set browser window size to 1000x1000 (브라우저 창 크기를 1000x1000으로 설정)
# myOptions.add_argument("headless")  # Enable headless mode (no window appears) (창을 띄우지 않고 백그라운드에서 실행)

# Define the ChromeDriver executable location (ChromeDriver 실행 파일 경로 지정)
myService = Service("./chromedriver-win64/chromedriver-win64/chromedriver.exe")  # 경로는 자신의 환경에 맞게 설정하세요

# Launch a new Chrome browser instance with the given options and service (위 옵션과 서비스로 새 Chrome 브라우저 실행)
browser = webdriver.Chrome(service=myService, options=myOptions)

# Maximize the browser window for full visibility (브라우저 창을 최대화하여 전체 화면 보기)
browser.maximize_window()

# Wait a few seconds to allow the browser to fully load (브라우저가 완전히 로드되도록 3초 대기)
time.sleep(3)

# Navigate to Naver Shopping homepage (네이버 쇼핑 메인 페이지로 이동)
browser.get("https://shopping.naver.com/ns/home")

# Wait 6 seconds to ensure the page and dynamic elements are loaded (페이지 및 동적 요소들이 로딩되도록 6초 대기)
time.sleep(6)

# --------------------------------------------------------------------
# 📌 Ways to find elements in Selenium (셀레니움에서 요소를 찾는 다양한 방법들)
# find_element(By.NAME, "username")
# find_element(By.LINK_TEXT, "Click me")
# find_element(By.XPATH, "//div")
# find_element(By.TAG_NAME, "input")
# find_element(By.CSS_SELECTOR, ".class")
# --------------------------------------------------------------------

# Find the search input box using CSS selector (CSS 선택자를 사용해 검색 입력창 요소 찾기)
search_box = browser.find_element(
    By.CSS_SELECTOR,
    "input._searchInput_search_text_83jy9._searchInput_placeholder_AG5yA._nlog_click"
)
time.sleep(3)
# 📌 Note: Class names like '83jy9', 'AG5yA' may change dynamically. Be cautious. (주의: 이러한 클래스명은 동적으로 바뀔 수 있음)
# Print the element object to verify it was found (요소가 정상적으로 탐색되었는지 출력해서 확인)
print(search_box)

# Close the browser window (브라우저 창 닫기)
browser.close()