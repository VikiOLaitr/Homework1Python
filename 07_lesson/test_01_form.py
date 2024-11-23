import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from FormPage import FormPage


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


def test_fill_form(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
               )
    form_page = FormPage(driver)

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
        form_page.fill_field(field_name, value)

    # Нажатие на кнопку Submit
    form_page.submit_form()

    # Проверка цвета фона поля "Zip code" после отправки формы
    zip_code_color = form_page.get_field_background_color("zip-code")
    expected_zip_code_color = 'rgba(248, 215, 218, 1)'
    assert zip_code_color == expected_zip_code_color, (
        "Expected Zip code background color: {expected_zip_code_color},"
        "but got: {zip_code_color}"
    )

    # Проверка цвета остальных полей
    green_fields = ["first-name", "last-name", "address", "city", "e-mail",
                    "phone", "job-position", "company"]
    expected_green_color = 'rgba(209, 231, 221, 1)'

    for field_name in green_fields:
        field_color = form_page.get_field_background_color(field_name)
        assert field_color == expected_green_color, (
            "Expected background color for {field_name}:"
            " {expected_green_color}, but got: {field_color}"
        )

