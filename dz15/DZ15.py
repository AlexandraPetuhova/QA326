from random import choice
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get("https://demowebshop.tricentis.com/register")
    driver.maximize_window()
    driver.implicitly_wait(2)
    yield driver
    driver.quit()


def random_word(count):
    alphabet = ["A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "H", "h", "I", "i", "J", "j", "K",
                "k", "L", "l", "M", "m", "N", "n", "O", "o", "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t", "U", "u",
                "V", "v", "W", "w", "X", "x", "Y", "y", "Z", "z"]
    word = []
    for i in range(count):
        word.append(choice(alphabet))
    return "".join(word)


with open("params.txt", "r") as file:
    params = file.read()
    file.close()
params = params.split(";\n\n")
params = list(map(lambda x: eval(x), params))


@pytest.mark.parametrize("input_value", params)
def test_registration(driver, input_value):
    if input_value['Gender'] == "f":
        gender_button = driver.find_element(By.CSS_SELECTOR, ".gender input[value='F']")
        gender_button.click()
    elif input_value['Gender'] == "m":
        gender_button = driver.find_element(By.CSS_SELECTOR, ".gender input[value='M']")
        gender_button.click()
    first_name = driver.find_element(By.ID, "FirstName")
    first_name.send_keys(input_value['First name'])
    last_name = driver.find_element(By.ID, "LastName")
    last_name.send_keys(input_value['Last name'])
    email = driver.find_element(By.ID, "Email")
    email.send_keys(input_value['Email'])
    password = driver.find_element(By.ID, 'Password')
    password.send_keys(input_value['Password'])
    confirm_password = driver.find_element(By.ID, 'ConfirmPassword')
    confirm_password.send_keys(input_value['Confirm Password'])
    register_button = driver.find_element(By.ID, 'register-button')
    register_button.click()
    if input_value['expected_result'] == 'valid':
        assert driver.current_url == "https://demowebshop.tricentis.com/registerresult/1"
        # меняем email, чтобы не ругался при повторном запуске теста
        login = driver.find_element(By.CSS_SELECTOR, '.header-links li a[href="/customer/info"]')
        while login.text == input_value['Email']:
            login.click()
            new_email = random_word(8) + "@mail.com"
            email = driver.find_element(By.ID, "Email")
            email.clear()
            email.send_keys(new_email)
            save_button = driver.find_element(By.NAME, "save-info-button")
            save_button.click()
            login = driver.find_element(By.CSS_SELECTOR, '.header-links li a[href="/customer/info"]')
    elif input_value['expected_result'] == 'invalid':
        assert driver.current_url == "https://demowebshop.tricentis.com/register"
