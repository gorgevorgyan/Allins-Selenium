from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
sleep_time=2
info={
"name":"Gvidon",
"surname":"Sahakyan",
"bday":"12.12.1990",
"phone":"+37477936314",
"email":"admin@alterprime.ml",
"username":"gvidonforever",
"password":"Armenia1234",
"pincode":19863
}
an_integer=info['pincode']
digit_string = str(an_integer)
digit_map = map(int, digit_string)
e = list(digit_map)
print(e)




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
	print('Clicking on Register Button....')
	registr_btn= driver.find_element_by_class_name("registr_btn")
	registr_btn.click()
	print('Done!')
except:
	print('Failed to click on register button!')
time.sleep(sleep_time)

try:
	print('Checking checkbox...')
	checkbox= driver.find_element_by_class_name("checkbox")
	checkbox.click()
	print('Done!')
except:
	print('Failed to check checkbox!')
time.sleep(sleep_time) 

try:
	print('Clicking on Tearms button...')
	tearms_button= driver.find_element_by_class_name("tearms_button")
	tearms_button.click()
	print('Done!')

except:
	print('Failed to click on tearms button!')
time.sleep(sleep_time)

try:
	print('Inserting name......')
	name= driver.find_element_by_name("GetWusersRegistr.NAME_A")
	name.clear()
	name.send_keys(info['name'])
	print('Done!')
except:
	print('Failed to insert name!')
time.sleep(sleep_time)

try:
	print('Inserting surname......')
	surname= driver.find_element_by_name("GetWusersRegistr.SNAME_A")
	surname.clear()
	surname.send_keys(info['surname'])
	print('Done!')

except:
	print('Failed to insert surname!')
time.sleep(sleep_time)

try:
	print('Inserting bday......')
	bday= driver.find_element_by_name("GetWusersRegistr.BIRTHDAY")
	bday.clear()
	bday.send_keys(info['bday'])
	print('Done!')

except:
	print('Failed to insert bday!')
time.sleep(sleep_time)

try:
	print('Inserting phone number......')
	phone= driver.find_element_by_name("GetWusersRegistr.PHONENUMBER")
	phone.clear()
	phone.send_keys(info['phone'])
	print('Done!')

except:
	print('Failed to insert phone number!')
time.sleep(sleep_time)

try:
	print('Inserting email......')
	email= driver.find_element_by_name("GetWusersRegistr.EMAIL")
	email.clear()
	email.send_keys(info['email'])
	print('Done!')

except:
	print('Failed to insert email!')
time.sleep(sleep_time)

try:
	print('Clicking on Register Button....')
	registr_btn= driver.find_element_by_class_name("registr_btn")
	registr_btn.click()
	print('Done!')
except:
	print('Failed to click on register button!')
time.sleep(sleep_time)

try:
	print('Waiting for Verification code......')
	code=input("Please insert the verification code:")
	codeinput= driver.find_element_by_class_name("only-numbers")
	codeinput.clear()
	codeinput.send_keys(code)
	print('Done!')
except:
	print('Failed to verificate!')
time.sleep(sleep_time)


try:
	print('Inserting username......')
	username= driver.find_element_by_name("NewUserName")
	username.clear()
	username.send_keys(info['username'])
	print('Done!')
except:
	print('Failed to insert username!')

time.sleep(sleep_time)
try:
	print('Inserting password......')
	password= driver.find_element_by_name("NewPassword")
	password.clear()
	password.send_keys(info['password'])
	print('Done!')
except:
	print('Failed to insert password!')
time.sleep(sleep_time)
try:
	print('Repeating password......')
	password1= driver.find_element_by_name("RepeadPassword")
	password1.clear()
	password1.send_keys(info['password'])
	print('Done!')
except:
	print('Failed to repeat password!')
time.sleep(sleep_time)
try:
	print('Clicking on Continue button...')
	tearms_button= driver.find_element_by_class_name("btn_usePass")
	tearms_button.click()
	print('Done!')

except:
	print('Failed to click on continue button!')
time.sleep(sleep_time)

try:
	print('Inserting pincode......')
	driver.find_element(By.CSS_SELECTOR, '[data-pin="1"]').send_keys(e[0])
	driver.find_element(By.CSS_SELECTOR, '[data-pin="2"]').send_keys(e[1])
	driver.find_element(By.CSS_SELECTOR, '[data-pin="3"]').send_keys(e[2])
	driver.find_element(By.CSS_SELECTOR, '[data-pin="4"]').send_keys(e[3])
	driver.find_element(By.CSS_SELECTOR, '[data-pin="5"]').send_keys(e[4])

	driver.find_element(By.CSS_SELECTOR, '[data-pin="1"][data-class="repeat"]').send_keys(e[0])
	driver.find_element(By.CSS_SELECTOR, '[data-pin="2"][data-class="repeat"]').send_keys(e[1])
	driver.find_element(By.CSS_SELECTOR, '[data-pin="3"][data-class="repeat"]').send_keys(e[2])
	driver.find_element(By.CSS_SELECTOR, '[data-pin="4"][data-class="repeat"]').send_keys(e[3])
	driver.find_element(By.CSS_SELECTOR, '[data-pin="5"][data-class="repeat"]').send_keys(e[4])
	print("Done!")
except:
	print('Failed to insert pincode!')
time.sleep(sleep_time)

try:
	print('Clicking on Login button...')
	tearms_button= driver.find_element_by_class_name("btn_pin")
	tearms_button.click()
	print('Done!')

except:
	print('Failed to click on Login button!')
time.sleep(sleep_time)
driver.close()