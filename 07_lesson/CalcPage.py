from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:

    def __init__(self, browser):
        self.driver = browser
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    def get(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def slow_calculator(self, delay):
        # Ввести значение 45 в поле с локатором #delay
        delay_field = WebDriverWait(self.driver, 40).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#delay"))
            )
        delay_field.clear()
        delay_field.send_keys(delay)

    def buttons(self, button):
        button_element = WebDriverWait(self.driver, 40).until(
                EC.element_to_be_clickable((By.XPATH, f"//span[text()='{button}']"))
            )
        button_element.click()

    def result_locator(self):
        result_locator = (By.CSS_SELECTOR, "#result")
        return WebDriverWait(self.driver, 40).until(EC.presence_of_element_located(result_locator)).text
