from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShopCartPage:
    def __init__(self, driver):
        self.driver = driver
        self.waiter = WebDriverWait(driver, 40)

    def login(self, username, password):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()

    def add_products_to_cart(self, products):
        for product in products:
            product_locator = (By.ID, f"add-to-cart-{product}")
            self.waiter.until(
                EC.element_to_be_clickable(product_locator)
            ).click()

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    def checkout(self, first_name, last_name, postal_code):
        self.waiter.until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        ).click()
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()

    def get_total(self):
        return self.waiter.until(
            EC.visibility_of_element_located((By.CLASS_NAME,
                                              "summary_total_label"))
        ).text

    def complete_purchase(self):
        self.waiter.until(EC.element_to_be_clickable((By.ID, "finish"))
                          ).click()
