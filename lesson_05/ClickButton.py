from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
sleep(3)
for i in range(5):
    button = driver.find_element(By.CSS_SELECTOR, "button")
    button.click()

sleep(3)
list = driver.find_elements(By.CSS_SELECTOR, "button.added-manually")
print(len(list))

driver.quit()
