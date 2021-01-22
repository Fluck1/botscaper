from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
#program by @Fluckych
driver = webdriver.Chrome('C:\programs\py\BOT\driver\chromedriver.exe')
driver.get('https://www.nike.com/ru/launch/t/killshot-coastal-blue') #url
button = driver.find_element_by_class_name('join-log-in')
button.click()
input_email = driver.find_element_by_name('emailAddress') #loginemail
input_email.send_keys('battleshkalnik@gmail.com')
input_password = driver.find_element_by_name('password')#loginpass
input_password.send_keys('Kuchin890')
button = driver.find_element_by_css_selector('.nike-unite .nike-unite-component.nike-unite-submit-button input')#buttom for login
button.click()
sleep(4)
driver.refresh()
sleep(2)
button = driver.find_element_by_xpath("//li[@class='size va-sm-m d-sm-ib va-sm-t ta-sm-c  '][12]/button[@class='size-grid-dropdown size-grid-button']")
button.click() #SIZE of pair

button = driver.find_element_by_xpath("//div[@class='mt2-sm mb6-sm prl0-lg fs14-sm']/button[@class='ncss-btn-primary-dark btn-lg']")
button.click() #offer

input_lastname = driver.find_element_by_name('lastname') #lastname
input_firstname = driver.find_element_by_name('firstname') #firstname
input_middlename = driver.find_element_by_name('middlename') #middlename
input_pcode = driver.find_element_by_name('pcode') #pcode
button_shippingregion = driver.find_element_by_name('shippingRegion') #region
input_shippingcity = driver.find_element_by_name('shippingCity') #City
input_street = driver.find_element_by_name('shippingAddress1') # street
input_house = driver.find_element_by_name('shippingAddress2')#house
input_phone_umber = driver.find_element_by_name('shippingPhoneNumber')#number
input_email = driver.find_element_by_name('shippingEmail')#email
button = driver.find_element_by_xpath("//span[@class=checkbox-checkmark]") # button for agreement

