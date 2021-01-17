from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
#program by @Fluckych
url = ''
cvv = ''
ncard = ''
name = ''
sname = ''
number = ''
driver = webdriver.Chrome('C:\programs\py\BOT\driver\chromedriver.exe')
driver.get('https://www.nike.com/ru/launch/t/womens-air-jordan-4-starfish')
button = driver.find_element_by_class_name('join-log-in')
button.click()
input_email = driver.find_element_by_name('emailAddress')
input_email.send_keys('')
input_password = driver.find_element_by_name('password')
input_password.send_keys('')
button = driver.find_element_by_css_selector('.nike-unite .nike-unite-component.nike-unite-submit-button input')
button.click()
