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
input_email.send_keys('')
input_password = driver.find_element_by_name('password')#loginpass
input_password.send_keys('')
button = driver.find_element_by_css_selector('.nike-unite .nike-unite-component.nike-unite-submit-button input')#buttom for login
button.click()
sleep(4)
driver.refresh()
sleep(2)
button = driver.find_element_by_xpath("//li[@class='size va-sm-m d-sm-ib va-sm-t ta-sm-c  '][12]/button[@class='size-grid-dropdown size-grid-button']")
button.click() #SIZE of pair

button = driver.find_element_by_xpath("//div[@class='mt2-sm mb6-sm prl0-lg fs14-sm']/button[@class='ncss-btn-primary-dark btn-lg']")
button.click() #offer


