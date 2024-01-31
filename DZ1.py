from selenium.webdriver import Keys
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.python.org/")
elem = driver.find_element(By.ID, 'id-search-field')
elem.click()
elem.send_keys("python")
elem.send_keys(Keys.ENTER)
driver.save_screenshot("D:\QA326\screenshot.jpg")
driver.back()
elem.clear()
elem.send_keys("anaconda")
elem.send_keys(Keys.ENTER)
driver.save_screenshot("D:\QA326\screenshot2.jpg")
