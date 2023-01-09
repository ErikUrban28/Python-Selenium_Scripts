import random
import string
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service


class TestUser:
    def setup_method(self):
        self.driver = webdriver.Firefox(service=Service("../../geckodriver-v0.32.0-win64/geckodriver.exe"))

    def teardown_method(self):
        self.driver.close()
        self.driver.quit()

    def test_users(self):
        rnd = ''.join(random.choices(string.ascii_lowercase + string.digits + string.ascii_uppercase, k=10))
        self.driver.maximize_window()
        self.driver.get("http://127.0.0.1/")
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.ID, "registration_bar").click()
        self.driver.find_element(By.ID, "register-login").click()
        self.driver.find_element(By.ID, "register-login").send_keys(rnd)
        self.driver.find_element(By.ID, "register-email").click()
        self.driver.find_element(By.ID, "register-email").send_keys("abcdef@gmail.com")
        self.driver.find_element(By.ID, "register-password").click()
        self.driver.find_element(By.ID, "register-password").send_keys("gfdreyy")
        assert self.driver.page_source.count('Validne') == 3
        self.driver.find_element(By.NAME, "submit").click()
        assert self.driver.title == "WatchFest: Admin"

        self.driver.find_element(By.ID, "users_bar").click()
        assert self.driver.title == "WatchFest: Users"
        assert "Upravit" in self.driver.page_source
        assert "Zmazat" in self.driver.page_source
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        self.driver.find_element(By.ID, rnd + "-delete").click()
        assert rnd not in self.driver.page_source
        assert self.driver.title == "WatchFest: Home"


if __name__ == "__main__":
    test = TestUser()
    test.setup_method()
    test.test_users()
    test.teardown_method()
