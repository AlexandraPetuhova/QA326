from pages.users import *
import pytest
from helpers import *
from config import *
from pages.registration import *


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get(base_url)
    driver.implicitly_wait(2)
    yield driver
    driver.quit()


def change_email(driver, input_value):
    my_login = driver.find_element(*login)
    while my_login.text == input_value['Email']:
        my_login.click()
        new_email = random_word(10, "e") + "@mail.com"
        my_email = driver.find_element(*email)
        my_email.clear()
        my_email.send_keys(new_email)
        button = driver.find_element(*save_button)
        button.click()
        my_login = driver.find_element(*login)


@pytest.mark.parametrize("input_value", test_cases)
def test_registration(driver, input_value):
    registration = Registration(driver)
    if input_value['Gender'] == "f":
        gender_button = driver.find_element(By.CSS_SELECTOR, ".gender input[value='F']")
        gender_button.click()
    elif input_value['Gender'] == "m":
        gender_button = driver.find_element(By.CSS_SELECTOR, ".gender input[value='M']")
        gender_button.click()
    registration.register(input_value)
    if input_value['expected_result'] == 'valid':
        assert driver.current_url == redirected_url
        change_email(driver, input_value)
    elif input_value['expected_result'] == 'invalid':
        assert driver.current_url == base_url
