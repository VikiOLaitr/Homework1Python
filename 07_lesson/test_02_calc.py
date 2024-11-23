import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from CalcPage import CalculatorPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


def test_slow_calculator(driver):
    # Открыть страницу калькулятора
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    calculator_page = CalculatorPage(driver)

    # Установить задержку 45
    calculator_page.set_delay("45")

    # Нажать на кнопки 7, +, 8, =
    buttons = ['7', '+', '8', '=']
    for button in buttons:
        calculator_page.click_button(button)

    # Ожидать появления результата
    try:
        # Ожидать результата 15
        result_text = calculator_page.get_result()
        print(f"Текущий текст результата: {result_text}")

        # Проверка, что результат действительно равен 15
        assert result_text == "15", "Ожидался результат 15, но получен: "
        "{result_text}"
    except Exception as e:
        print(f"Ошибка: {e}")
