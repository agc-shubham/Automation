from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://web.whatsapp.com')



name = "WhatsApp Bot"
msg = "Hii, This is A whatsapp Chat Bot"



time.sleep(15)
#locate span using inspect element that store Contact name
user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()


for i in range (10):
    #locate div using inspect element that contains message box 
    msg_box = driver.find_element_by_xpath('//div[@class="_3uMse"]')
    msg_box.send_keys(msg)
    #locate button using inspect element that contains send button
    button = driver.find_element_by_xpath('//button[@class="_1U1xa"]')
    button.click()
print("task completed")