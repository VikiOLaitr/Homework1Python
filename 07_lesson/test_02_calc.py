import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from CalcPage import CalcPage


def test_calc():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    calcPage = CalcPage(browser)
    calcPage.get()
    
    calcPage.slow_calculator("45")

    # Нажать на кнопки 7, +, 8, =
    buttons = ['7', '+', '8', '=']
    for button in buttons:
        calcPage.buttons(button)

    calcPage.result_locator()
    try:
        # Ожидать результата 15
        result_text = calcPage.result_locator()
        print(f"Текущий текст результата: {result_text}")

        # Проверка, что результат действительно равен 15
        assert result_text == "15", "Ожидался результат 15, но получен: "
        "{result_text}"
    except Exception as e:
        print(f"Ошибка: {e}")

    yield browser
    browser.quit()
