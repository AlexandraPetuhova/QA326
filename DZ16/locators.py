from selenium.webdriver.common.by import By

first_name = (By.ID, "FirstName")
last_name = (By.ID, "LastName")
email = (By.ID, "Email")
password = (By.ID, 'Password')
confirm_password = (By.ID, 'ConfirmPassword')
register_button = (By.ID, 'register-button')
login = (By.CSS_SELECTOR, '.header-links li a[href="/customer/info"]')
save_button = (By.NAME, "save-info-button")