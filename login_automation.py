from selenium import webdriver
import time

# Please be sure that you appropriately add path of your geckodrive to environment variables.
browser = webdriver.Firefox(executable_path="C:/Users/oğuz/Desktop/geckodriver")

# Why do we need time module? We want to wait for websites to render completely and then
# take some actions further on them.

time.sleep(5)

browser.get("https://www.instagram.com")

time.sleep(5)

# Please be aware of the DOM elements, so, you can specify the method as you wish.
# Reach out to w3schools.com to fully understand the DOM elements.
username = browser.find_element_by_name("username")
password = browser.find_element_by_name("password")

# You will specify your username below between quotes.
username.send_keys("")

# You will specify your password below between quotes.
password.send_keys("")

login_button = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]")

login_button.click()

time.sleep(5)