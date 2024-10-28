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

    def field(self, fields):
        self.fields = fields
        fields = {
            "first-name": "Иван",
            "last-name": "Петров",
            "address": "Ленина, 55-3",
            "e-mail": "test@skypro.com",
            "phone": "+7985899998787",
            "zip-code": "",
            "city": "Москва",
            "country": "Россия",
            "job-position": "QA",
            "company": "SkyPro",
        }

        # Заполнение формы
        for field_name, value in fields.items():
            field = WebDriverWait(self.driver, 40).until(
                EC.presence_of_element_located((By.NAME, field_name))
            )
            field.send_keys(value)

    # Нажатие на кнопку Submit
    def submit_button(self, submit_button):
        submit_button = WebDriverWait(self.driver, 40).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Submit']"))
        )
        submit_button.click()

    # Проверка цвета фона поля "Zip code" после отправки формы
    def zip_code_element(self, zip_code_element):
        zip_code_element = WebDriverWait(self.driver, 40).until(
            EC.presence_of_element_located((By.ID, "zip-code"))
        )
        zip_code_color = zip_code_element.value_of_css_property('background-color')
        expected_zip_code_color = 'rgba(248, 215, 218, 1)'
        assert zip_code_color == expected_zip_code_color
        "Expected Zip code background color: {expected_zip_code_color}, but got:"
        "{zip_code_color}"

    # Проверка цвета остальных полей
    def green_fields(self, green_fields):
        green_fields = ["first-name", "last-name", "address", "city", "e-mail",
                        "phone", "job-position", "company"]
        expected_green_color = 'rgba(209, 231, 221, 1)'

        for field_id in green_fields:
            try:
                field = WebDriverWait(self.driver, 40).until(
                    EC.presence_of_element_located((By.ID, field_id))
                )
                field_color = field.value_of_css_property('background-color')
                assert field_color == expected_green_color
                "Expected background color for {field_id}: {expected_green_color},"
                "but got: {field_color}"
            except Exception as e:
                print((
                        f"Не удалось найти поле с ID {field_id} для проверки "
                        f"цвета фона. Ошибка: {e}"
                        ))
