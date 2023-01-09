

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service


class TestPages:
    def setup_method(self):
        self.driver = webdriver.Firefox(service=Service("../../geckodriver-v0.32.0-win64/geckodriver.exe"))

    def teardown_method(self):
        self.driver.close()
        self.driver.quit()

    def test_pages(self):
        self.driver.maximize_window()
        self.driver.get("http://127.0.0.1/")
        self.driver.implicitly_wait(5)
        assert self.driver.title == "WatchFest: Home"
        self.driver.find_element(By.ID, "home_bar").click()
        assert self.driver.title == "WatchFest: Home"
        self.driver.find_element(By.ID, "about_bar").click()
        assert self.driver.title == "WatchFest: About"
        self.driver.find_element(By.ID, "articles_bar").click()
        assert self.driver.title == "WatchFest: Articles"
        self.driver.find_element(By.ID, "registration_bar").click()
        assert self.driver.title == "WatchFest: Register"
        self.driver.find_element(By.ID, "login_bar").click()
        assert self.driver.title == "WatchFest: Login"

        self.driver.find_element(By.ID, "home_bar").click()
        self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[5]/div[1]/a[1]").click()
        assert self.driver.title == "WatchFest: Register"
        self.driver.find_element(By.ID, "home_bar").click()
        self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[5]/div[1]/a[2]").click()
        assert self.driver.title == "WatchFest: Login"
        self.driver.find_element(By.XPATH, "//a[@class='link'][contains(text(),'Registracia')]").click()
        assert self.driver.title == "WatchFest: Register"


if __name__ == "__main__":
    test = TestPages()
    test.setup_method()
    test.test_pages()
    test.teardown_method()
