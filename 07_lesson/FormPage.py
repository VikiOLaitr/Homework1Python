from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FormPage:
    def __init__(self, driver):
        self.driver = driver
        self.waiter = WebDriverWait(driver, 40)

    def fill_field(self, field_name, value):
        field = self.waiter.until(
            EC.presence_of_element_located((By.NAME, field_name))
        )
        field.send_keys(value)

    def submit_form(self):
        submit_button = self.waiter.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Submit']"))
        )
        submit_button.click()

    def get_field_background_color(self, field_id):
        field = self.waiter.until(
            EC.presence_of_element_located((By.ID, field_id))
        )
        return field.value_of_css_property('background-color')
