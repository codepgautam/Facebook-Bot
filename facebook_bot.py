from selenium import webdriver
import time

from selenium.webdriver.chrome.options import Options

option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 1
})

driver = webdriver.Chrome(chrome_options=option, executable_path="C:\DRIVERS\Chrome_driver\chromedriver.exe")

driver.get("http://facebook.com")
time.sleep(3)
User_input = driver.find_element_by_xpath("//*[@id='email']")
pwd_input = driver.find_element_by_xpath("//*[@id='pass']")
User_input.send_keys("pgbraja005@gmail.com")
pwd_input.send_keys("Python@123")
driver.find_element_by_name("login").click()
driver.implicitly_wait(5)
driver.find_element_by_class_name("p361ku9c").click()
time.sleep(5)
driver.find_element_by_class_name("a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7").click()
driver.switch_to_active_element().send_keys("Hello")
driver.find_element_by_name("Post").click()

