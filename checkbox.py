from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
url = "https://demoqa.com/automation-practice-form"
driver.get(url)
driver.maximize_window()    
time.sleep(5)
#for scroll the page
driver.execute_script("window.scrollTo(0, 500);")
time.sleep(3)

driver.find_element(By.XPATH,"//div[@id='hobbiesWrapper']//div[@class='col-md-9 col-sm-12']//div[1]").click()
time.sleep(3)

driver.find_element(By.XPATH,"//div[@id='hobbiesWrapper']//div[@class='col-md-9 col-sm-12']//div[1]").click()
time.sleep(3)

driver.find_element(By.XPATH,"//div[@id='hobbiesWrapper']//div[@class='col-md-9 col-sm-12']//div[1]").click()
time.sleep(3)

driver.find_element(By.XPATH,"//div[@id='hobbiesWrapper']//div[@class='col-md-9 col-sm-12']//div[2]").click()

driver.execute_script("window.scrollTo(0, -500);") 
time.sleep(3)

input("Press enter to exit...")
driver.quit()