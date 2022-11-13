from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
import random
import time
import requests

#proxies = {'http': 'http://209.146.105.241:80'}
#response = requests.get('http://httpbin.org/ip', proxies=proxies)
#print(response.json()['origin']) # 190.64.18.162

options = Options()
ua = UserAgent()
userAgent = ua.random
print(userAgent)
options.add_argument(f'user-agent={userAgent}')

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
    element.send_keys('********')
    element = driver.find_element(By.CSS_SELECTOR, 'button.gd-ui-button:nth-child(1)')
    element.click()
    driver.implicitly_wait(10)
driver = webdriver.Firefox()
driver.get('https://www.glassdoor.com/Search/results.htm?keyword=data%20analyst&locId=2443166&locT=C&locName=Leipzig%20(Germany)')
element = driver.find_element(By.CSS_SELECTOR, '.mr-xxsm')
element.click()
driver.implicitly_wait(10)
element = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/section/article/div[1]/ul/li[2]/div[2]/a')

links = []

for i in range(1,31):
    element2 = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div/div[2]/section/article/div[1]/ul/li['+str(i)+']/div[2]/a')
    element3 = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div/div[2]/section/article/div[1]/ul/li['+str(i)+']')
    if element3.get_attribute('data-is-easy-apply')=='true':
        links.append(element2.get_attribute('href'))

for link in links:
    print(link)
    driver.get(link)
    try:

        iframe = driver.find_element(By.CSS_SELECTOR, '#credential_picker_container > iframe:nth-child(1)')
        print(iframe.get_attribute('src'))
        driver.switch_to.frame(iframe)
        driver.implicitly_wait(10)
        time.sleep(10)
        element = driver.find_element(By.CSS_SELECTOR,'svg.Bz112c:nth-child(2) > path:nth-child(1)')
        element.click()
        driver.implicitly_wait(10)
        time.sleep(10)
        driver.switch_to.default_content()
    except:
        print('No hay popup')
    driver.implicitly_wait(20)
    time.sleep(10)
    element = driver.find_element(By.CSS_SELECTOR, '.applyButton')
    element.click()
    driver.implicitly_wait(10)
    time.sleep(10)
    try:
        iframe = driver.find_element(By.XPATH, '//iframe[@title = "Job application form container"]')
        print(iframe.get_attribute('src'))
        driver.switch_to.frame(iframe)
        time.sleep(10)
        iframe2 = driver.find_element(By.XPATH, '//iframe[@title="Job application form"]')
        driver.switch_to.frame(iframe2)
        time.sleep(10)
        element = driver.find_element(By.ID, "input-applicant.firstName")
   # element = driver.find_element(By.NAME,'application_form')
   # driver.switch_to.frame(element)
        element.send_keys('Jose Luis')
        element = driver.find_element(By.ID, "input-applicant.lastName")
        element.send_keys('Cordoba Cabanillas')
        element = driver.find_element(By.ID,"input-applicant.email")
        element.send_keys('parradojose77@gmail.com')
        element = driver.find_element(By.ID,"input-applicant.phoneNumber")
        element.send_keys('17642934122')
        element = driver.find_element(By.ID,"ia-CustomFilePicker-resume")
        element.send_keys("/home/jose/Downloads/MODIF_CV_JoseLuisCordobaCabanillas inglés(1).pdf")
        element = driver.find_element(By.ID, "form-action-continue")
        element.click()
        try:
            select = Select(driver.find_element_by_id('select-0'))
            select.select_by_value('DE')
        except:
            print('oh, sielos')
        try:
            element = driver.find_element(By.ID, 'form-action-continue')
            element.click()
        except:
            print('No se ha encontrado')
        time.sleep(20)
    except:
        #iframe = driver.find_element(By.XPATH, '//iframe[@title = "Job application form container"]')
       # print(iframe.get_attribute('src'))
        #driver.switch_to.frame(iframe)
       # time.sleep(10)
        #iframe2 = driver.find_element(By.XPATH, '//iframe[@title="Job application form"]')
       # driver.switch_to.frame(iframe2)
       # time.sleep(10)
        element = driver.find_element(By.ID, 'input-applicant.name')
        element.send_keys('Jose Luis Cordoba Cabanillas')
        element = driver.find_element(By.ID,'input-applicant.email')
        element.send_keys('jluis.cordoba.cabanillas@gmail.com')
        element = driver.find_element(By.ID, 'input-applicant.phoneNumber')
        element.send_keys('017642934122')
        element = driver.find_element(By.NAME, 'applicant.fileUpload')
        element.send_keys("/home/jose/Downloads/MODIF_CV_JoseLuisCordobaCabanillas inglés(1).pdf")
       # element = driver.find_element(By.CSS_SELECTOR,'.icl-Button--transparent')
## el elemento es de hacer click y luego escribir.
        #element.send_keys("/home/jose/Downloads/Job_Application_Cover_letter_junior_software_devv.pdf")

        element = driver.find_element(By.ID,'form-action-continue')
        element.click()
        time.sleep(5)
        try:
            element.find_element(By.ID,'form-action-continue')
            element.click()
        except:
            print('No se ha encontrado numero')

   # driver.switch_to.default_content()
   # element = driver.find_element(By.CSS_SELECTOR, 'html body.is-white div#ia-container div.ia-FlexContainer div#ia-ApplyFormScreen.ia-ApplyFormScreen div form div div div.ia-ApplyFormScreen-userFields div.ia-UserFields div.ia-UserFields-secondary div.ia-UserFields-fragment div div.UserField-Name div.ia-TextInput div.icl-TextInput div.icl-TextInput-wrapper')
   # element.send_keys('Jose Luis')

