import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

current_dir = os.path.dirname(os.path.abspath(__file__))

driver_path = os.path.join(current_dir, 'chromedriver.exe')

service = Service(executable_path=driver_path)

chrome_browser = webdriver.Chrome(service=service)

chrome_options = Options()
chrome_options.add_argument('--ignore-ssl-errors=yes')
chrome_options.add_argument('--ignore-certificate-errors')


chrome_browser = webdriver.Chrome(service=service, options=chrome_options)
chrome_browser.maximize_window()
chrome_browser.get('https://www.selenium.dev/selenium/web/web-form.html')

#assert 'Web form' in chrome_browser.title

assert 'Color picker' in chrome_browser.page_source

user_message = chrome_browser.find_element(By.ID, 'my-text-id')
user_message.clear()
user_message.send_keys('Palmeiras!!!')

time.sleep(10)  # Keep the browser open for 5 seconds before closing

