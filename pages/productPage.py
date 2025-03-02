from selenium.webdriver.common.by import By

class ProductPage:

    def __init__(self, browser):
        self.browser = browser

    def check_title_is(self, title):
        page_title = self.browser.find_element(By.XPATH, '//*[@id="tbodyid"]/h2')
        assert page_title.text == 'Samsung galaxy s6'

    def check_product_count(self, count):
        items = self.browser.find_elements(By.XPATH, '//*[@id="tbodyid"]/div')
        assert len(items) == count