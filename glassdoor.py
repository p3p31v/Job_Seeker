from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random
ran = random.randrange(10000)
driver = webdriver.Firefox()
driver.get("https://www.glassdoor.com")
#link = driver.find_element_by_xpath('/html/body/header/div/div/div/a[3]/span[2]')
#link.click()
element = driver.find_element(By.CSS_SELECTOR, "#inlineUserEmail")
element.send_keys("jluis.cordoba.cabanillas@gmail.com")
element = driver.find_element(By.CSS_SELECTOR, ".facebookWhite > span:nth-child(2)")
element.click()
driver.get("https://www.facebook.com/login.php?skip_api_login=1&api_key=129253937150340&kid_directed_site=0&app_id=129253937150340&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fv5.0%2Fdialog%2Foauth%3Fapp_id%3D129253937150340%26cbt%3D1666874718951%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfa16ce74b0cc8e%2526domain%253Dwww.glassdoor.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.glassdoor.com%25252Ff16882c97c96e88%2526relation%253Dopener%26client_id%3D129253937150340%26display%3Dpopup%26domain%3Dwww.glassdoor.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.glassdoor.com%252Findex.htm%26locale%3Den_US%26logger_id%3Df2850979c5d0172%26origin%3D1%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3a455f780beee6%2526domain%253Dwww.glassdoor.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.glassdoor.com%25252Ff16882c97c96e88%2526relation%253Dopener%2526frame%253Df33dd11c07c6f8c%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26scope%3Demail%252Cuser_location%252Cuser_birthday%26sdk%3Djoey%26version%3Dv5.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df3a455f780beee6%26domain%3Dwww.glassdoor.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.glassdoor.com%252Ff16882c97c96e88%26relation%3Dopener%26frame%3Df33dd11c07c6f8c%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=popup&locale=en_US&pl_dbl=0")
driver.implicitly_wait(3)
driver.find_element_by_class_name("_4t2a")
#element = driver.find_element(By.CSS_SELECTOR,"#identifierId")
#element.send_keys("jluis.cordoba.cabanillas@gmail.com")
#element.click()
#all_options = element.find_elements(By.TAG_NAME,"option")
#for option in all_options:
   # print("Value is: %s" % option.get_attribute("value"))
    #option.click()
