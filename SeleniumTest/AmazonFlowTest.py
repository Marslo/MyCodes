from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

weburl = "http://www.amazon.com"

ff = webdriver.Firefox()
ff.implicitly_wait(10)

# try:
ff.get(weburl)

if 'Amazon.com' in ff.title:
  inputElement = ff.find_element_by_id("twotabsearchtextbox")
  inputElement.send_keys("clean code")
  inputElement.submit()

  firstbook = ff.find_element_by_xpath("//div[@id='result_0']//div[2]//a[1]")
  WebDriverWait(ff, 10).until(
      EC.presence_of_element_located((By.ID, "result_0"))
    )
  firstbook.click()


else:
  print 'The target is not Amazon. Please check the URL and run this again.'

# finally:
  # driver.quit()
