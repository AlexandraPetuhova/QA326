import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import logging

# Без этого почему-то не сохраняет логи
from imp import reload
reload(logging)

logging.basicConfig(filename='results.log', filemode="w", encoding='utf-8', level=logging.INFO,
                    format='%(asctime)s  | %(levelname)s  |  %(message)s')


# Тест-кейсы на сайте
# https://www.globalsqa.com/angularJs-protractor/BankingProject/#/customer


@pytest.fixture()
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/customer")
    driver.implicitly_wait(2)
    driver.maximize_window()
    yield driver
    driver.quit()


def is_clickable(element):
    try:
        element.click()
    except:
        return False
    return True

# проверка успешного входа при выполнении необходимых условий
users = ("Hermoine Granger", "Harry Potter", "Intentional Error")

@pytest.mark.parametrize("input_value", users)
def test_user_login(driver, input_value):
    logging.info(f"Testing login as {input_value}")
    try:
        try:
            customer_name = Select(driver.find_element(By.ID, "userSelect"))
            customer_name.select_by_visible_text(input_value)
        except:
            logging.error(f"User {input_value} is NOT found.")
        wait = WebDriverWait(driver, timeout=2)
        wait.until(lambda d: driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/form/button').is_displayed())
        button = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/form/button")
        button.click()
        wait.until(
            lambda d: driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/strong').is_displayed())
        assert driver.find_element(By.XPATH,
                                   '/html/body/div/div/div[2]/div/div[1]/strong').text == f"Welcome {input_value} !!"
        logging.info(f"Test for user {input_value} was successful")
    except:
        logging.error(f"Test for user {input_value} was NOT successful")
        assert driver.find_element(By.XPATH,
                                   '/html/body/div/div/div[2]/div/div[1]/strong').text == f"Welcome {input_value} !!"

# проверка, что кнопка входа не отображается, если пользователь не выбран
def test_no_button_without_user(driver):
    logging.info("Testing the absence of login button with no user selected")
    try:
        button = driver.find_element(By.XPATH, "html/body/div/div/div[2]/div/form/button")
        assert button.get_attribute("class") == "btn btn-default ng-hide"
        logging.info("Test was successful")
    except:
        logging.error("Test failed")

# проверка, что кнопка входа не кликабельна, если пользователь не выбран
def test_no_button_without_user2(driver):
    logging.info("Testing that login button is not clickable with no user selected")
    try:
        button = driver.find_element(By.XPATH, "html/body/div/div/div[2]/div/form/button")
        assert is_clickable(button) == False
        logging.info("Test was successful")
    except:
        logging.error("Test failed")

# проверка, что кнопка входа не работает после сброса пользователя
def test_no_button_without_user3(driver):
    logging.info("Testing that login button is not clickable after the user was unselected")
    try:
        customer_name = Select(driver.find_element(By.ID, "userSelect"))
        customer_name.select_by_visible_text("Hermoine Granger")
        customer_name.select_by_visible_text("---Your Name---")
        button = driver.find_element(By.XPATH, "html/body/div/div/div[2]/div/form/button")
        assert is_clickable(button) == False
        logging.info("Test was successful")
    except:
        logging.error("Test failed")
