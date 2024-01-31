from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://calcus.ru/kalkulyator-ipoteki")
cost = driver.find_element(By.NAME, 'cost')
cost.click()
cost.send_keys("1000000")
st_sum = driver.find_element(By.NAME, 'start_sum')
st_sum.click()
st_sum.send_keys("300000")
period = driver.find_element(By.NAME, 'period')
period.click()
period.send_keys("15")
percent = driver.find_element(By.NAME, 'percent')
percent.click()
percent.send_keys("5")
button = driver.find_element(By.CSS_SELECTOR, "input[type='submit'][value='Рассчитать']")
button.click()
wait = WebDriverWait(driver, timeout=3)
wait.until(lambda d: driver.find_element(By.ID, 'credit-total-chart').is_displayed())
driver.save_screenshot("D:\QA326\screenshot3.jpg")
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.ID, 'credit-payments-chart')).perform()
driver.save_screenshot("D:\QA326\screenshot4.jpg")
action.move_to_element(driver.find_element(By.CSS_SELECTOR, 'div.calc-panel')).perform()
driver.save_screenshot("D:\QA326\screenshot5.jpg")