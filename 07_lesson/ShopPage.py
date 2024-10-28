from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShopPage:

    def __init__(self, browser):
        self.driver = browser
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()
        self.waiter = WebDriverWait(browser, 40)

    def get(self):
        self.driver.get("https://www.saucedemo.com/")

    def authorization(self, username, password):
        self.driver.find_element(By.ID, "user-name").send_keys("username")
        self.driver.find_element(By.ID, "password").send_keys("password")
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()

    def product(self, products):
        products = [
            "sauce-labs-backpack",
            "sauce-labs-bolt-t-shirt",
            "sauce-labs-onesie"
        ]
        for product in products:
            product_locator = (By.ID, f"add-to-cart-{product}")
            self.waiter.until(
                EC.element_to_be_clickable(product_locator)
            ).click()

    def go_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    def button(self):
        self.waiter.until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        ).click()

    def initialization(self, firstname, lastname, postalcode):
        self.driver.find_element(By.ID, "first-name").send_keys("firstname")
        self.driver.find_element(By.ID, "last-name").send_keys("lastname")
        self.driver.find_element(By.ID, "postal-code").send_keys("postalcode")
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()

    def summary(self, total_element):
        total_element = self.waiter.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
        assert total_element.text == "Total: $58.29"

    def finish(self):
        self.waiter.until(EC.element_to_be_clickable((By.ID, "finish"))).click()
