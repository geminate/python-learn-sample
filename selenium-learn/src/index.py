from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

start_time = time.time()

chrome_options = Options()
# chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)

browser = webdriver.Chrome(options=chrome_options)
browser.set_page_load_timeout(50)
browser.maximize_window()

browser.get("https://github.com/login")
print("Finish: get login page")

jq = browser.find_element_by_css_selector

jq('#login_field').send_keys("geminate")
jq('#password').send_keys("lhh89090530")

jq('input[name="commit"]').click()
print("Finish: login action")

jq('.user-nav li:nth-of-type(3) .details-overlay').click()
print("Finish: show detail")

jq('.user-nav li:nth-of-type(3) .details-overlay details-menu li:nth-of-type(3) .dropdown-item').click()
print("Finish: get profile page")

aa = jq('svg.js-calendar-graph-svg')
print(aa.screenshot_as_base64)
print(time.time() - start_time)

browser.close()
