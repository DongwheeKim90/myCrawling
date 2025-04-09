from selenium import webdriver  # Import the Selenium WebDriver module (Selenium WebDriver 모듈을 임포트)
from selenium.webdriver.chrome.service import Service  # Import the Chrome driver service manager (Chrome 드라이버 서비스 매니저 임포트)
import time  # Import the time module to use sleep (time 모듈을 임포트하여 sleep 사용)

'''
browser = webdriver.Chrome("D:/myCrawling/chromedriver-win64/chromedriver-win64/chromedriver.exe")
browser.get("http://naver.com")
In recent versions of Selenium (especially Selenium 4.x and above), specifying the ChromeDriver path directly as a string when creating the WebDriver object is no longer supported.
That is, the above method is no longer valid.
(최근 버전의 Selenium (특히 Selenium 4.x 이상)은 WebDriver 객체를 생성할 때 크롬 드라이버의 경로를 직접 문자열로 지정하는 방식을 지원하지 않음.
즉, 위 방식은 더 이상 유효하지 않음)
'''

# Define the ChromeDriver service using the proper method (적절한 방식으로 ChromeDriver 서비스 정의)
myService = Service("D:/myCrawling/chromedriver-win64/chromedriver-win64/chromedriver.exe")

# Create a Chrome browser instance using the service (Service를 사용하여 Chrome 브라우저 인스턴스 생성)
browser = webdriver.Chrome(service=myService)

# Navigate to the Naver website (네이버 웹사이트로 이동)
browser.get("http://naver.com")

# Wait for 10 seconds to keep the browser open (브라우저를 10초 동안 열어둠)
time.sleep(10)

# Close the browser window (브라우저 창 닫기)
browser.close()