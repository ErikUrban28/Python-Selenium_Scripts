import random
import string

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service


class TestRegistration:
    def setup_method(self):
        self.driver = webdriver.Firefox(service=Service("../../geckodriver-v0.32.0-win64/geckodriver.exe"))

    def teardown_method(self):
        self.driver.close()
        self.driver.quit()

    def test_registration(self):
        rndTest = ''.join(random.choices(string.ascii_lowercase + string.digits + string.ascii_uppercase, k=10))
        rnd = ''.join(random.choices(string.ascii_lowercase + string.digits + string.ascii_uppercase, k=2))
        self.driver.maximize_window()
        self.driver.get("http://127.0.0.1/")
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.ID, "registration_bar").click()
        submit = self.driver.find_element(By.NAME, "submit")

        self.driver.find_element(By.ID, "register-login").click()
        self.driver.find_element(By.ID, "register-login").send_keys(rndTest)
        self.driver.find_element(By.ID, "register-email").click()
        self.driver.find_element(By.ID, "register-email").send_keys("abcdef@gmail.com")
        self.driver.find_element(By.ID, "register-password").click()
        self.driver.find_element(By.ID, "register-password").send_keys("gfdreyy")
        assert self.driver.page_source.count('Validne') == 3

        # nepovolena dlzka loginu
        login = self.driver.find_element(By.ID, "register-login")
        login.clear()
        login.click()
        login.send_keys(rnd)
        submit.click()
        assert "Login musi mat aspon 3 charaktery" in self.driver.page_source

        # nepovoleny znak pred @
        email = self.driver.find_element(By.ID, "register-email")
        email.clear()
        email.click()
        email.send_keys(rnd + "!@gmail.com")
        submit.click()
        assert "Neplany Email" in self.driver.page_source
        # nepovoleny znak za @
        email.send_keys(Keys.CONTROL + "a")
        email.send_keys(rnd + "@g_mail.com")
        assert "Neplany Email" in self.driver.page_source

        # nepovolena dlzka hesla
        password = self.driver.find_element(By.ID, "register-password")
        password.clear()
        password.click()
        password.send_keys("gfdr")
        submit.click()
        assert "Heslo musi mat viac ako 6 znakov" in self.driver.page_source

        assert self.driver.title == "WatchFest: Register"


if __name__ == "__main__":
    test = TestRegistration()
    test.setup_method()
    test.test_registration()
    test.teardown_method()
