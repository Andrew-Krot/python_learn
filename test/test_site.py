import time
from pages.homePage import HomePage
from pages.productPage import ProductPage

def test_open_s6(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_galaxy_s6()
    productpage = ProductPage(browser)
    productpage.check_title_is('Samsung galaxy s6')

def test_two_items(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_monitors()
    time.sleep(3)
    productpage = ProductPage(browser)
    productpage.check_product_count(2)