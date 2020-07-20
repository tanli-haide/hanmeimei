from selenium import webdriver
import time
driver = webdriver.Chrome()#
driver.maximize_window()


driver.get("http://www.taobao.com")
driver.find_elemnt_by_xpatn('//input[@id="q"]').send_keys("凉拖鞋")