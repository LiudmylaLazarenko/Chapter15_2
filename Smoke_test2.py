from selenium import webdriver

driver = webdriver.Chrome(executable_path='chromedriver')
driver.get("https://cleveronly.com/brainbucket/index.php?route=account/login")

driver.maximize_window()

logo = driver.find_element_by_xpath("//img[@title='Brainbucket']")

#Returning Customer
#Password

email_input = driver.find_element_by_id("input-email")
email_input.clear()
email_input.send_keys("liudmyla.lazarenko@gmail.com")

password_input = driver.find_element_by_id("input-password")
password_input.clear()
password_input.send_keys("Viki")

returning_customer_btn = driver.find_element_by_xpath("//input[@value='Login']")
returning_customer_btn.click()