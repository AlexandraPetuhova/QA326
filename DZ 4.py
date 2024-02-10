import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

# ЗАДАНИЕ
# Опишите два тест кейса для данной страницы с авторизацией (без пользователя и с выбранным пользователем)
# https://www.globalsqa.com/angularJs-protractor/BankingProject/#/customer
#
# Напишите тестовые функции по составленным тест-кейсам


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
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
users = ("Hermoine Granger", "Harry Potter", "Ron Weasly", "Albus Dumbledore", "Neville Longbottom")
@pytest.mark.parametrize("input_value", users)
def test_user_login(driver, input_value):
    customer_name = Select(driver.find_element(By.ID, "userSelect"))
    customer_name.select_by_visible_text(input_value)
    wait = WebDriverWait(driver, timeout=2)
    wait.until(lambda d: driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/form/button').is_displayed())
    button = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/form/button")
    button.click()
    wait.until(lambda d: driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/strong').is_displayed())
    assert driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div[1]/strong').text == f"Welcome {input_value} !!"


    # проверка, что кнопка входа не отображается, если пользователь не выбран
def test_no_button_without_user(driver):
    button = driver.find_element(By.XPATH, "html/body/div/div/div[2]/div/form/button")
    assert button.get_attribute("class") == "btn btn-default ng-hide"


    # проверка, что кнопка входа не кликабельна, если пользователь не выбран
def test_no_button_without_user2(driver):
    button = driver.find_element(By.XPATH, "html/body/div/div/div[2]/div/form/button")
    assert is_clickable(button) == False


    # проверка, что кнопка входа не работает после сброса пользователя
def test_no_button_without_user3(driver):
    customer_name = Select(driver.find_element(By.ID, "userSelect"))
    customer_name.select_by_visible_text("Hermoine Granger")
    customer_name.select_by_visible_text("---Your Name---")
    button = driver.find_element(By.XPATH, "html/body/div/div/div[2]/div/form/button")
    assert is_clickable(button) == False


# Дополнительное ЗАДАНИЕ(необязательное)
# https://www.omdbapi.com/ для данного сайта составьте тест-кейсы на проверку работы апи с параметрами (можно выбрать один любой параметр)
# напишите  тестовые функции по составленным тест-кейсам

import pytest
import requests

base_url = "http://www.omdbapi.com/"
search = "%22Rotten%20Tomatoes%22"
apikey = "73a953dd"
url = f"{base_url}?apikey={apikey}&s={search}"
print(url)

def test_search_by_name():
    response = requests.get(url)
    assert response.status_code in range(200, 300)
    assert response.json()['Response'] == "True"

def test_search_by_id():
    id = "&i=tt13683866"
    url = f"{base_url}?apikey={apikey}{id}"
    response = requests.get(url)
    assert response.status_code in range(200, 300)
    assert response.json()['Response'] == "True"

def test_no_apikey():
    apk = ""
    url = f"{base_url}?apikey={apk}&s={search}"
    response = requests.get(url)
    assert response.status_code >= 400
    assert response.json()['Response'] == "False"

def test_invalid_search():
    search = "m"
    url = f"{base_url}?apikey={apikey}&s={search}"
    response = requests.get(url)
    assert response.status_code in range(200, 300)
    assert response.json()['Response'] == "False"