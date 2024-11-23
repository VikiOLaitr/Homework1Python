import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from ShopPage import ShopCartPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shopping_cart(driver):
    driver.get("https://www.saucedemo.com/")
    shopping_cart_page = ShopCartPage(driver)

    shopping_cart_page.login("standard_user", "secret_sauce")

    products = [
        "sauce-labs-backpack",
        "sauce-labs-bolt-t-shirt",
        "sauce-labs-onesie"
    ]

    shopping_cart_page.add_products_to_cart(products)
    shopping_cart_page.go_to_cart()

    shopping_cart_page.checkout("Kristina", "Kalaburdina", "250011")

    total_text = shopping_cart_page.get_total()
    assert total_text == "Total: $58.29"

    shopping_cart_page.complete_purchase()
