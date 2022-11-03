from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import random
import time
#ran = random.randrange(10000)
driver = webdriver.Firefox()
#driver.get("https://www.glassdoor.com")
#element = driver.find_element(By.CLASS_NAME,"link")
#element.click()
#driver.implicitly_wait(4)
driver.get("https://www.glassdoor.com/about/terms.htm")
driver.implicitly_wait(10)
iframe = driver.find_element_by_tag_name('iframe')

driver.switch_to_frame(iframe)
element = driver.find_element(By.CSS_SELECTOR, 'svg.Bz112c:nth-child(2) > path:nth-child(1)')
element.click()
driver.implicitly_wait(10)
driver.switch_to.default_content()
element = driver.find_element(By.CSS_SELECTOR,'div.d-none:nth-child(5) > button:nth-child(1)')
#element = webdriver(driver,20).until(EC.presence_of_element_located((By.CSS_SELECTOR,'svg.Bz112c:nth-child(2)')))
element.click()
element = driver.find_element(By.CSS_SELECTOR,'#modalUserEmail')
element.send_keys('parradojose77@gmail.com')
#elements = driver.find_elements(By.TAG_NAME,'svg')
element = driver.find_element(By.CSS_SELECTOR, 'button.gd-ui-button:nth-child(1) > span:nth-child(1)')
element.click()
element = driver.find_element(By.CSS_SELECTOR, '.e3i3eoo2')
element.click()
element = driver.find_element(By.CSS_SELECTOR,'#modalUserPassword')
element.send_keys('Z0013497BD3D9p3p')
element = driver.find_element(By.CSS_SELECTOR, 'button.gd-ui-button:nth-child(1)')
element.click()
#print(len(elements))
try:
    for i in elements:
        print(i)
        print(i.get_attribute('xmlns'))
except:
    pass





#element.send_keys("jluis.cordoba.cabanillas@gmail.com")
#element.click()
#all_options = element.find_elements(By.TAG_NAME,"option")
#for option in all_options:
   # print("Value is: %s" % option.get_attribute("value"))
    #option.click()
