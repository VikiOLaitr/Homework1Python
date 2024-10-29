import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from FormPage import FormPage


def test_form():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    formPage = FormPage(browser)
    formPage.get()

    formPage.field()
    field = {
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
    for field_name, value in field.items():
        formPage.field(field_name, value)

    formPage.submit_button()

    formPage.zip_code_element()
    expected_zip_code_color = 'rgba(248, 215, 218, 1)'
    assert formPage.zip_code_element == expected_zip_code_color, (
        "Expected Zip code background color: {expected_zip_code_color},"
        "but got:{formPage.zip_code_element}")

    green_fields = ["first-name", "last-name", "address", "city", "e-mail",
                    "phone", "job-position", "company"]
    expected_green_color = 'rgba(209, 231, 221, 1)'

    for field_id in green_fields:
        field_color = formPage.green_fields(field_id)
        assert field_color == expected_green_color(
            "Expected background color for {field_id}: {expected_green_color},"
            "but got: {field_color}")
        
    yield browser
    browser.quit()
