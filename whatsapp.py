from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 
 
driver = webdriver.Firefox(executable_path = r'C:\Users\Vaibhav\Downloads\Compressed\geckodriver.exe') 
  
driver.get("https://web.whatsapp.com")
wait = WebDriverWait(driver, 600) 
driver.implicitly_wait(600)
target = input("Enter exact name : ")
string = input("Enter Message :")
click = driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[2]').click()
search = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/span/div/span/div/div[1]/div/label/div/div[2]')
search.send_keys(target)
user = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div[2]/div[1]/div/div/div[2]/div/div/div[2]')
user.click()
msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
msg_box.send_keys(string)
driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]').click()
driver.implicitly_wait(600)
q = driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[3]').click()
q1 = driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[3]/span/div/ul/li[6]').click()
driver.close()
driver.quit()
