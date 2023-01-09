

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
        assert "Odhlásenie" not in self.driver.page_source
        assert "Pouzivatelia" not in self.driver.page_source

        isPresent = len(self.driver.find_elements(By.ID, "user_bar"))
        assert isPresent == 0

        self.driver.find_element(By.ID, "articles_bar").click()
        assert self.driver.title == "WatchFest: Articles"
        assert "Vytvor novy clanok" not in self.driver.page_source
        assert "Upravit" not in self.driver.page_source
        assert "Zmazat" not in self.driver.page_source


if __name__ == "__main__":
    test = TestPages()
    test.setup_method()
    test.test_pages()
    test.teardown_method()
