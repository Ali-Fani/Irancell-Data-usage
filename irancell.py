from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import json
chrome_options = Options()
chrome_options.add_argument("--headless")
driver=webdriver.Chrome(options=chrome_options)
driver.get("https://my.irancell.ir/")
msidn=driver.find_element_by_name('msisdn')
msidn.send_keys("989370529220")
msidn.send_keys(Keys.ENTER)
wait = WebDriverWait(driver, 10)
enterwithpass = wait.until(EC.element_to_be_clickable((By.ID, 'verifyEcarePass')))
enterwithpass.click()
password=driver.find_element_by_id("inputFieldPassword")
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)
time.sleep(2)
driver.get("https://my.irancell.ir/api/myaccounts_test")
pre = driver.find_element_by_tag_name("pre").text
data = json.loads(pre)
print(data['account']['data'])
