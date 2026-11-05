from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

url = "http://10.106.1.220:7001/carms/login.xhtml"
driver = webdriver.Chrome()
driver.get(url)

username = "carms@customs.gov.ph"
password = "P@ssword12345"


driver.maximize_window()


