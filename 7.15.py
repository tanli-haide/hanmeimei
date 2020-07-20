from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
'''

import os
for i in range(1,16):
    if i >= 18:
        name = './0000' + str(i)+'.py'
    else:
        name = './0000' + str(1)+'.py'
    if not os.path.exists(name):
        os.remove(name)
    else:
        pass
'''