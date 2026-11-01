from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

user_name = "standard_user"
password = "secret_sauce"

user_name = driver.find_element(By.ID, "user-name")
user_name.send_keys("standard_user")

password = driver.find_element(By.ID, "password")
password.send_keys("secret_sauce")

time.sleep(3)

login_button = driver.find_element(By.ID,"login-button")
login_button.click()



input("Press enter to exit...")
driver.quit()