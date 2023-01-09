import random
import string
import time

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
        rnd = ''.join(random.choices(string.ascii_lowercase + string.digits + string.ascii_uppercase, k=10))
        self.driver.maximize_window()
        self.driver.get("http://127.0.0.1/")
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.ID, "login_bar").click()
        self.driver.find_element(By.NAME, "submit").click()
        assert "Chybne vyplnene udaje" in self.driver.page_source

        login = self.driver.find_element(By.ID, "login-login")
        login.click()
        login.send_keys(rnd)
        self.clear(login)
        self.driver.find_element(By.NAME, "submit").click()
        assert "Login musi byt vyplneny" in self.driver.page_source


        password = self.driver.find_element(By.ID, "login-password")
        password.click()
        password.send_keys("gfdreyy")
        self.clear(password)
        self.driver.find_element(By.NAME, "submit").click()
        assert "Heslo musi byt vyplnene" in self.driver.page_source

        assert self.driver.title == "WatchFest: Login"

    def clear(self, element):
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)


if __name__ == "__main__":
    test = TestLogin()
    test.setup_method()
    test.test_login()
    test.teardown_method()
