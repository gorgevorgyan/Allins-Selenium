from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
sleep_time=2
info={
"username":"gvidonforever",
"password":"Armenia1234",
"pincode":19863
}
an_integer=info['pincode']
digit_string = str(an_integer)
digit_map = map(int, digit_string)
e = list(digit_map)

try:
	print('Geeting driver...')
	driver = webdriver.Chrome('./chromedriver')
	print('Done!')
except:
	print('Failed to get driver!')

time.sleep(sleep_time)

try:
	print('Opening app...')
	driver.get("https://allins.lite-group.org/")
	print('Done!')
except:
	print('Failed to open url!')
time.sleep(sleep_time)
try:
	print('Clicking on Login Button....')
	login_btn= driver.find_element_by_class_name("login_btn")
	login_btn.click()
	print('Done!')
except:
	print('Failed to click on register button!')
time.sleep(sleep_time)

try:
	print('Inserting username......')
	username= driver.find_element_by_name("UserName")
	username.clear()
	username.send_keys(info['username'])
	print('Done!')
except:
	print('Failed to insert surname!')
time.sleep(sleep_time)

try:
	print('Inserting password......')
	password= driver.find_element_by_name("Password")
	password.clear()
	password.send_keys(info['password'])
	print('Done!')
except:
	print('Failed to insert surname!')
time.sleep(sleep_time)
try:
	login= driver.find_element_by_class_name("mutq_hamakarg")
	login.click()
	print('Done!')
except:
	print('Failed to Login!')
time.sleep(sleep_time)