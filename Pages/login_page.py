from selenium.webdriver.common.by import By

class LoginPage:

    username = (By.XPATH, "/html/body/div[1]/div/div/div/div/div/div/div/div/form/div[2]/div[1]/input")
    password = (By.XPATH, "/html/body/div[1]/div/div/div/div/div/div/div/div/form/div[2]/div[2]/div[1]/input")
    login_button = (By.XPATH, "/html/body/div[1]/div/div/div/div/div/div/div/div/form/div[2]/button")

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(*self.username).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()