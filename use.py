#!/usr/bin/env python
# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import settings
import time

# Launch browser
driver = webdriver.Chrome()

# Maximize browser
#driver.maximize_window()

# Access site
url = "https://twitter.com/login"
driver.get(url)

# Get title
print(driver.title)

# Input email and password
screen_name = driver.find_element_by_class_name("js-username-field")
password = driver.find_element_by_class_name("js-password-field")
screen_name.send_keys(settings.my_name)
password.send_keys(settings.passwd)

# Submit
password.submit()

time.sleep(1)

# Tweet
tweet = driver.find_element_by_id("tweet-box-home-timeline")
tweet.send_keys("進捗ダメです！")
post = driver.find_element_by_css_selector("button.tweet-action")
print(post)
post.click()
