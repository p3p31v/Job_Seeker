from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import random
import time
def login_glassdoor():
    driver = webdriver.Firefox()
    driver.get("https://www.glassdoor.com/about/terms.htm")
    driver.implicitly_wait(10)
    iframe = driver.find_element_by_tag_name('iframe')

    driver.switch_to_frame(iframe)
    element = driver.find_element(By.CSS_SELECTOR, 'svg.Bz112c:nth-child(2) > path:nth-child(1)')
    element.click()
    driver.implicitly_wait(10)
    driver.switch_to.default_content()
    element = driver.find_element(By.CSS_SELECTOR,'div.d-none:nth-child(5) > button:nth-child(1)')
    element.click()
    element = driver.find_element(By.CSS_SELECTOR,'#modalUserEmail')
    element.send_keys('parradojose77@gmail.com')
    element = driver.find_element(By.CSS_SELECTOR, 'button.gd-ui-button:nth-child(1) > span:nth-child(1)')
    element.click()
    element = driver.find_element(By.CSS_SELECTOR, '.e3i3eoo2')
    element.click()
    element = driver.find_element(By.CSS_SELECTOR,'#modalUserPassword')
    element.send_keys('Z0013497BD3D9p3p')
    element = driver.find_element(By.CSS_SELECTOR, 'button.gd-ui-button:nth-child(1)')
    element.click()
    driver.implicitly_wait(10)
driver = webdriver.Firefox()
driver.get('https://www.glassdoor.com/Search/results.htm?keyword=data%20analyst&locId=2443166&locT=C&locName=Leipzig%20(Germany)')
element = driver.find_element(By.CSS_SELECTOR, '.mr-xxsm')
element.click()
driver.implicitly_wait(10)
element = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/section/article/div[1]/ul/li[2]/div[2]/a')
print(element.get_attribute('href'))

#element2 = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div/div[2]/section/article/div[1]/ul/li[3]/div[2]/a')

#element3 = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div/div[2]/section/article/div[1]/ul/li[30]/div[2]/a'
