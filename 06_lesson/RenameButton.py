from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

driver.implicitly_wait(20)
driver.get("http://uitestingplayground.com/textinput")
element = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
element.send_keys("SkyPro")
button = driver.find_element(By.CSS_SELECTOR, "button#updatingButton")
button.click()
txt = driver.find_element(By.CSS_SELECTOR, "button#updatingButton").text
print(txt)
driver.quit()
