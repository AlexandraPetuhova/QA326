from QA326.DZ16.locators import *


class Registration:
    def __init__(self, driver):
        self.first_name = driver.find_element(*first_name)
        self.last_name = driver.find_element(*last_name)
        self.email = driver.find_element(*email)
        self.password = driver.find_element(*password)
        self.confirm_password = driver.find_element(*confirm_password)
        self.register_button = driver.find_element(*register_button)

    def register(self, input_value):
        self.first_name.send_keys(input_value['First name'])
        self.last_name.send_keys(input_value['Last name'])
        self.email.send_keys(input_value['Email'])
        self.password.send_keys(input_value['Password'])
        self.confirm_password.send_keys(input_value['Confirm Password'])
        self.register_button.click()
