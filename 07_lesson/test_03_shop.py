import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from ShopPage import ShopPage


def test_shop():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    shopPage = ShopPage(browser)
    shopPage.get()
    shopPage.authorization("standard_user", "secret_sauce")

    product = [
        "sauce-labs-backpack",
        "sauce-labs-bolt-t-shirt",
        "sauce-labs-onesie"
        ]
    shopPage.add_product(product)

    shopPage.go_cart()
    shopPage.button()
    shopPage.initialization("Viki", "Burlachenko", "765325")

    shopPage.get_summary()
    assert shopPage.get_summary == "Total: $58.29"

    shopPage.finish
    
    yield browser
    browser.quit()
