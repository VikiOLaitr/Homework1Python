from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FormPage:

    def __init__(self, browser):
        self.driver = browser
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    def get(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    def field(self, field_name, value):
        # Заполнение формы
        self.field = WebDriverWait(self.driver, 40).until(
                EC.presence_of_element_located((By.NAME, field_name))
            )
        self.field.send_keys(value)

    # Нажатие на кнопку Submit
    def submit_button(self, submit_button):
        submit_button = WebDriverWait(self.driver, 40).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Submit']"))
        )
        submit_button.click()

    # Проверка цвета фона поля "Zip code" после отправки формы
    def zip_code_element(self):
        WebDriverWait(self.driver, 40).until(
            EC.presence_of_element_located((By.ID, "zip-code"))
        ).value_of_css_property('background-color')

    # Проверка цвета остальных полей
    def green_fields(self, field_id):
        field = WebDriverWait(self.driver, 40).until(
                    EC.presence_of_element_located((By.ID, field_id))
                )
        return field.value_of_css_property('background-color')
