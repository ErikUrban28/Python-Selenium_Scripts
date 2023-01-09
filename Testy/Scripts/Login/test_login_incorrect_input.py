import random
import string

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service


class TestLogin:
    def setup_method(self):
        self.driver = webdriver.Firefox(service=Service("../../geckodriver-v0.32.0-win64/geckodriver.exe"))

    def teardown_method(self):
        self.driver.close()
        self.driver.quit()

    def test_login(self):
        rndTest = ''.join(random.choices(string.ascii_lowercase + string.digits + string.ascii_uppercase, k=10))
        rnd = ''.join(random.choices(string.ascii_lowercase + string.digits + string.ascii_uppercase, k=2))
        self.driver.maximize_window()
        self.driver.get("http://127.0.0.1/")
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.ID, "login_bar").click()
        login = self.driver.find_element(By.ID, "login-login")
        login.click()
        login.send_keys(rndTest)
        password = self.driver.find_element(By.ID, "login-password")
        password.click()
        password.send_keys("gfdreyywer")
        assert self.driver.page_source.count('Validne') == 2


        self.driver.find_element(By.ID, "login_bar").click()
        login = self.driver.find_element(By.ID, "login-login")
        login.click()
        login.clear()
        login.send_keys(rnd)
        self.driver.find_element(By.NAME, "submit").click()

        password = self.driver.find_element(By.ID, "login-password")
        password.clear()
        password.click()
        password.send_keys("abcd")

        self.driver.find_element(By.NAME, "submit").click()

        assert self.driver.title == "WatchFest: Login"



if __name__ == "__main__":
    test = TestLogin()
    test.setup_method()
    test.test_login()
    test.teardown_method()
