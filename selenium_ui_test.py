from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://example.com')

assert 'Example Domain' in driver.title

element = driver.find_element(By.TAG_NAME, 'h1')
print(element.text)

driver.quit()