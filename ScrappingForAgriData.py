from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://agmarknet.gov.in/')

user = driver.find_elements_by_xpath('//*[@id="gvCustomers_imgOrdersShow_3"]')
user[0].click()

time.sleep(15)
dataTag = driver.find_element_by_xpath('//*[@id="gvCustomers_gvOrders_3"]/tbody/tr[2]/td[3]')
data = dataTag.text
print(data)