from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))


driver.get("http://the-internet.herokuapp.com/entry_ad")
button = driver.find_element(By.CSS_SELECTOR, "[class = modal-footer]")
button.click()

print(driver.title)
driver.quit()
