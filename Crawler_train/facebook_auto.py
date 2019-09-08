from selenium.webdriver import Chrome
import time
driver = Chrome("./chromedriver")
# 跟你平常操作一模一樣
driver.get("https://www.facebook.com")
# find: find_element!!!!!t
# find_all: find_elements!!!!
driver.find_element_by_id("email").send_keys("請輸入帳號")
driver.find_element_by_id("pass").send_keys("請輸入密碼")
driver.find_element_by_id("loginbutton").click()

c = input("請輸入驗證碼")
driver.find_element_by_id("approvals_code").send_keys(c)
driver.find_element_by_id("checkpointSubmitButton").click()
# selenium: 把等待的時間寫進去
time.sleep(1)
driver.find_element_by_id("checkpointSubmitButton").click()

time.sleep(3)
content = driver.find_element_by_class_name("userContent")
# 一樣: 拿紙條就用.text
print("第一則貼文內容:", content.text)

# 這是習慣 在關閉前給三秒 讓他做完所有事情
time.sleep(3)
driver.close()