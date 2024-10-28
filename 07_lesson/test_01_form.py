import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from FormPage import FormPage


@pytest.fixture
def test_form():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    formPage = FormPage(browser)
    formPage.get()
    formPage.field()
    formPage.submit_button()
    formPage.zip_code_element()
    formPage.green_fields()

    yield browser
    browser.quit()
