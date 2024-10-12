from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))


driver.get("http://the-internet.herokuapp.com/login")
sleep(3)
element1 = driver.find_element(By.CSS_SELECTOR, "#username")
element1.send_keys("tomsmith")
sleep(3)
element2 = driver.find_element(By.CSS_SELECTOR, "#password")
element2.send_keys("SuperSecretPassword!")
sleep(3)
button = driver.find_element(By.CSS_SELECTOR, "button")
button.click()
sleep(3)
driver.quit()
