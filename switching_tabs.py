from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url_1 = "https://the-internet.herokuapp.com/dropdown"
url_2 = "https://the-internet.herokuapp.com/context_menu"

driver = webdriver.Chrome()
driver.get(url_1)
driver.maximize_window()
time.sleep(3)
driver.switch_to.new_window()
driver.get(url_2)
time.sleep(3)
driver.switch_to.window(driver.window_handles[0])


input("press enter to exit...")
driver.quit()