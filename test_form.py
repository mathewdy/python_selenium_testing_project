from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

url = "https://demoqa.com/automation-practice-form"

first_name = "mathew"
last_name = "dalisay"
email = "mathewdalisay123@mema.com"
gender = "Male"
mobile_number = "09123456789"

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

driver.execute_script("window.scrollTo(0, 250);")
date_of_birth_input = driver.find_element(By.ID, "dateOfBirthInput")
date_of_birth_input.click()
time.sleep(1)

driver.execute_script("window.scrollTo(0, 250);")

date_of_birth_input = driver.find_element(By.XPATH, "//div[@aria-label='Choose Tuesday, November 10th, 2026']")
date_of_birth_input.click() 
driver.execute_script("window.scrollTo(0, 300);")
time.sleep(1)

driver.execute_script("window.scrollTo(0, 250);")
time.sleep(1)

hobbies_input = driver.find_element(By.XPATH, "//div[@id='hobbiesWrapper']//div[@class='col-md-9 col-sm-12']//div[2]")
hobbies_input.click()
time.sleep(1)

hobbies_input = driver.find_element(By.XPATH, "//div[@id='hobbiesWrapper']//div[@class='col-md-9 col-sm-12']//div[1]")
hobbies_input.click()
driver.execute_script("window.scrollTo(0, 400);")
time.sleep(1)

submit_button = driver.find_element(By.ID, "submit")
submit_button.click()

driver.execute_script("window.scrollTo(0, 400);")

input('Click enter to exit...')
driver.quit()