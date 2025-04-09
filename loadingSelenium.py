from selenium import webdriver  # Import the Selenium WebDriver module (Selenium WebDriver 모듈을 임포트)
from selenium.webdriver.chrome.service import Service  # Import the Chrome driver service manager (Chrome 드라이버 서비스 매니저 임포트)
from selenium.webdriver.common.by import By  # Locator strategy (요소를 찾기 위한 방법 By 모듈 임포트)
from selenium.webdriver.support.ui import WebDriverWait  # Wait functionality (명시적 대기를 위한 WebDriverWait 임포트)
from selenium.webdriver.support import expected_conditions as EC  # Expected conditions for wait (조건을 만족할 때까지 대기하기 위한 EC 임포트)
import time  # Import time module for sleep (sleep 기능을 위해 time 모듈 임포트)

# Set debugging options (디버깅 및 실행 환경 옵션 세팅)
myOptions = webdriver.ChromeOptions()
# myOptions.add_argument("window-size=1000,1000")  # Set browser window size to 1000x1000 (브라우저 창 크기 설정: 가로 1000, 세로 1000)
myOptions.add_argument("no-sandbox")  # Disable Chrome sandbox security (크롬의 샌드박스 보안 기능 비활성화)
# myOptions.add_argument("headless")  # Uncomment this line to run browser in headless mode (이 줄을 활성화하면 브라우저 창 없이 실행됨)

# Define the ChromeDriver service (ChromeDriver 서비스 정의)
myService = Service("./chromedriver-win64/chromedriver-win64/chromedriver.exe")

# Create a Chrome browser instance using the defined service and options (정의한 서비스와 옵션을 사용해 Chrome 브라우저 인스턴스 생성)
browser = webdriver.Chrome(service=myService, options=myOptions)
browser.maximize_window()
time.sleep(3)  # Wait for 3 seconds to allow the browser to fully start (브라우저가 완전히 시작되도록 3초 대기)

# Navigate to Naver Shopping home page (네이버 쇼핑 메인 페이지로 이동)
browser.get("https://shopping.naver.com/ns/home")

# Wait until the search input box with specific classes is loaded (특정 클래스명을 가진 검색창 요소가 로딩될 때까지 대기)
WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "._searchInput_search_text_83jy9._searchInput_placeholder_AG5yA._nlog_click"))
)
print("Finish : wait for untill class")  # Print message when wait is complete (대기 완료 시 메시지 출력)

# Close the browser (브라우저 종료)
browser.close()