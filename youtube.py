from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import  Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options= chrome_options)

driver.get('https://www.youtube.com/shorts/')

time.sleep(4)
cookie = driver.find_element(by=By.CSS_SELECTOR, value='.lssxud button')
cookie.click()

time.sleep(2)
history = driver.find_element(by=By.CSS_SELECTOR, value='.jtCddb button')
history.click()


for i in range(5):
    time.sleep(5)
    actions = ActionChains(driver)
    actions.send_keys(Keys.ARROW_DOWN)
    actions.perform()

driver.quit()