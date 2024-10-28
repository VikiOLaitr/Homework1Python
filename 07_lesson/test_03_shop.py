import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from ShopPage import ShopPage


@pytest.fixture
def test_shop():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    shopPage = ShopPage(browser)
    shopPage.get()
    shopPage.authorization("standard_user", "secret_sauce")
    shopPage.product()
    shopPage.go_cart()
    shopPage.button()
    shopPage.initialization("Viki", "Burlachenko", "765325")
    shopPage.summary()

    yield browser
    browser.quit()
