from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))


driver.get("http://the-internet.herokuapp.com/inputs")
sleep(3)
element = driver.find_element(By.CSS_SELECTOR, "input")
element.send_keys("1000")
sleep(3)
element.clear()
element.send_keys("999")
sleep(3)
driver.quit()
