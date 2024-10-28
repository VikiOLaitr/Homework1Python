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

    def slow_calculator(self):
        # Ввести значение 45 в поле с локатором #delay
        delay_field = WebDriverWait(self.driver, 40).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#delay"))
            )
        delay_field.clear()
        delay_field.send_keys("45")

    def buttons(self, buttons):
        # Нажать на кнопки 7, +, 8, =
        buttons = ['7', '+', '8', '=']
        for button in buttons:
            button_element = WebDriverWait(self.driver, 40).until(
                EC.element_to_be_clickable((By.XPATH, f"//span[text()='{button}']"))
            )
            button_element.click()

    def result_locator(self):
        # Ожидать появления результата
        result_locator = (By.CSS_SELECTOR, "#result")
        try:
            WebDriverWait(self.driver, 45).until(
                EC.text_to_be_present_in_element(result_locator, "15")
            )
            result_element = self.driver.find_element(*result_locator)
            result_text = result_element.text
            print(f"Текущий текст результата: {result_text}")

            # Проверка, что результат действительно равен 15
            assert result_text == "15", "Ожидался результат 15, "
            "но получен: {result_text}"
        except Exception as e:
            print(f"Ошибка: {e}")
