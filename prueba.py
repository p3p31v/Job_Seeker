from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.google.com/intl/es-419/gmail/about/")
link = driver.find_element_by_xpath('/html/body/header/div/div/div/a[3]/span[2]')
link.click()
