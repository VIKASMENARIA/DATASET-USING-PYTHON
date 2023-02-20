from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
path="F:/python/chromedriver.exe"
s=Service(path)
driver=webdriver.Chrome(service = s)
driver.get("https://google.com/ ")

box=driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
box.send_keys("avatar")
time.sleep(2)
box.send_keys(Keys.ENTER)
time.sleep
driver.find_element_by_xpath("""//*[@id="kp-wp-tab-overview"]/div[6]/div/div/div/div/div/div[1]/div/a""").click()
time.sleep(2)
driver.save_screenshot("F:/python/d1.png")