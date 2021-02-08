from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep
#program by @Fluckych
driver = webdriver.Chrome('C:\programs\py\BOT\driver\chromedriver.exe')
driver.get('https://www.nike.com/ru/launch/t/womens-space-hippie-04-this-is-trash-cactus-flower') #url
button = driver.find_element_by_class_name('join-log-in')
button.click()
input_email = driver.find_element_by_name('emailAddress') #loginemail
input_email.send_keys('')
input_password = driver.find_element_by_name('password')#loginpass
input_password.send_keys('')
button = driver.find_element_by_css_selector('.nike-unite .nike-unite-component.nike-unite-submit-button input')#buttom for login
button.click()
sleep(4)

flag = 1
while flag != 0:
    flag = 0
    try:
        button = driver.find_element_by_xpath('//button[text()="US 9.5 (RU 42)"]')
    except NoSuchElementException:
        flag = 1
        print(flag)

button.click() #SIZE of pair
button = driver.find_element_by_xpath('//button[text()="Оформить заказ"]')
button.click() #offer

button = driver.find_element_by_xpath('//input[@class="textInput isInvalid ng-pristine ng-invalid ng-touched]')
button.send_keys('')
button = driver.find_element_by_xpath('//button[text()="Сохранить и продолжить"]')

button = driver.find_element_by_xpath('//div[text()="Номер карты *"]')
button.send_keys('')
button = driver.find_element_by_xpath('//div[text()="MM/YY *"]')
button.send_keys('')
button = driver.find_element_by_xpath('//div[text()="CVV *"]')
button.send_keys('')
button = driver.find_element_by_xpath('//button[text()="Продолжить"]')
button.click()
button = driver.find_element_by_xpath('//button[text()="Отправить заказ"')
button.click()