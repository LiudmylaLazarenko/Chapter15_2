from selenium import webdriver

driver = webdriver.Chrome(executable_path='chromedriver')
driver.get("https://cleveronly.com/brainbucket/index.php?route=account/login")

driver.maximize_window()

logo = driver.find_element_by_xpath("//img[@title='Brainbucket']")

new_registrant_btn = driver.find_element_by_xpath("//a[contains(text(), 'Continue')]")
new_registrant_btn.click()

#Register Account
#Personal Details
#First Name
firstname_field = driver.find_element_by_xpath("//fieldset/div[2]")
firstname_field_class = firstname_field.get_attribute("class")
assert "required" in firstname_field_class

firstname_input = driver.find_element_by_id("input-firstname")
firstname_input.clear()
firstname_input.send_keys("Liudmyla")

#Last Name
lastname_field = driver.find_element_by_xpath("//fieldset/div[3]")
lastname_field_class = lastname_field.get_attribute("class")
assert "required" in lastname_field_class

lastname_input = driver.find_element_by_id("input-lastname")
lastname_input.clear()
lastname_input.send_keys("Lazarenko")

#E-Mail
email_field = driver.find_element_by_xpath("//fieldset/div[4]")
email_field_class = email_field.get_attribute("class")
assert "required" in email_field_class

email_input = driver.find_element_by_id("input-email")
email_input.clear()
email_input.send_keys("lazarenko.liudmyla@gmail.com")

#Telephone
telephone_field = driver.find_element_by_xpath("//fieldset/div[4]")
telephone_field_class = telephone_field.get_attribute("class")
assert "required" in telephone_field_class

telephone_input = driver.find_element_by_id("input-telephone")
telephone_input.clear()
telephone_input.send_keys("312-868-4811")

#Fax
fax_input = driver.find_element_by_id("input-fax")
fax_input.clear()
fax_input.send_keys("512-999-9999")


#Your Address
#Company
company_input = driver.find_element_by_id("input-company")
company_input.clear()
company_input.send_keys("QA")

#Address1
address1_field = driver.find_element_by_xpath("//fieldset[2]/div[2]")
address1_field_class = address1_field.get_attribute("class")
assert "required" in address1_field_class

address1_input = driver.find_element_by_id("input-address-1")
address1_input.clear()
address1_input.send_keys("4567 Normandy Ave")


#Address2
address2_input = driver.find_element_by_id("input-address-2")
address2_input.clear()
address2_input.send_keys("Apt 4")

city_field = driver.find_element_by_xpath("//fieldset[2]/div[4]")
city_field_class = city_field.get_attribute("class")
assert "required" in city_field_class
city_input = driver.find_element_by_id("input-city")
city_input.clear()
city_input.send_keys("Chicago")

postcode_input = driver.find_element_by_id("input-postcode")
postcode_input.clear()
postcode_input.send_keys("60133")

password_field = driver.find_element_by_xpath("//fieldset[3]/div[1]")
password_field_class = password_field.get_attribute("class")
assert "required" in password_field_class
password_input = driver.find_element_by_id("input-password")
password_input.clear()
password_input.send_keys("Viki")

confirm_field = driver.find_element_by_xpath("//fieldset[3]/div[2]")
confirm_field_class = confirm_field.get_attribute("class")
assert "required" in confirm_field_class
confirm_input = driver.find_element_by_id("input-confirm")
confirm_input.clear()
confirm_input.send_keys("Viki")

continue_btn = driver.find_element_by_xpath("//input[@value='Continue']")

