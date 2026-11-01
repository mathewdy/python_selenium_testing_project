from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()
url = "https://the-internet.herokuapp.com/dropdown"
driver.maximize_window()
driver.get(url)

dropdown_element = driver.find_element(By.ID,"dropdown")
    
select = Select(dropdown_element)

#can select 3 ways to select an option in the dropdown
#1. select by index
#2. select by value
#3 select by visible text

select.select_by_index(1)
time.sleep(3)

select.select_by_value("2")
time.sleep(3)

select.select_by_visible_text("Option 1")

input("Press enter to exit...")
driver.quit()