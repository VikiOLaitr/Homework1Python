import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from CalcPage import CalcPage


@pytest.fixture
def test_calc():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    calcPage = CalcPage(browser)
    calcPage.get()
    calcPage.slow_calculator()
    calcPage.buttons()
    calcPage.result_locator()

    yield browser
    browser.quit()
