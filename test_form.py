from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "https://demoqa.com/automation-practice-form"

first_name = "mathew"
last_name = "dalisay"
email = "mathewdalisay123@mema.com"
gender = "Male"
mobile_number = "09123456789"
date_of_birth = "01 Jan 1990"

driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

time.sleep(3)

first_name_input = driver.find_element(By.ID, "firstName")
first_name_input.send_keys(first_name)
time.sleep(1)
last_name_input = driver.find_element(By.ID,"lastName")
last_name_input.send_keys(last_name)
time.sleep(1)
email_input = driver.find_element(By.ID,"userEmail")
email_input.send_keys(email)
time.sleep(1)
gender_input = driver.find_element(By.ID, "gender-radio-1")
gender_input.click()
time.sleep(1)
mobile_number_input = driver.find_element(By.ID, "userNumber")
mobile_number_input.send_keys(mobile_number)
time.sleep(1)

date_of_birth_input = driver.find_element(By.ID, "dateOfBirth")
date_of_birth_input.send_keys(date_of_birth)
time.sleep(1)



input('Click enter to exit...')
driver.quit()