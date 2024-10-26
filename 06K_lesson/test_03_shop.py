import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_shopping_cart(driver):
    driver.get("https://www.saucedemo.com/")
    waiter = WebDriverWait(driver, 40)

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.XPATH, "//input[@type='submit']").click()

    products = [
        "sauce-labs-backpack",
        "sauce-labs-bolt-t-shirt",
        "sauce-labs-onesie"
    ]

    for product in products:
        product_locator = (By.ID, f"add-to-cart-{product}")
        waiter.until(
            EC.element_to_be_clickable(product_locator)
        ).click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    waiter.until(
        EC.element_to_be_clickable((By.ID, "checkout"))
    ).click()

    driver.find_element(By.ID, "first-name").send_keys("Viki")
    driver.find_element(By.ID, "last-name").send_keys("Burlachenko")
    driver.find_element(By.ID, "postal-code").send_keys("765325")

    driver.find_element(By.XPATH, "//input[@type='submit']").click()

    total_element = waiter.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label")
                                         )
    )
    assert total_element.text == "Total: $58.29"

    waiter.until(EC.element_to_be_clickable((By.ID, "finish"))).click()