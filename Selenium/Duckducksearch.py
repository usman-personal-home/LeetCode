#!/usr / bin / env python
from selenium import webdriver
import time

# set webdriver path here it may vary


# Load the page
driver = webdriver.Chrome()
website_URL = "https://duckduckgo.com/"
driver.get(website_URL)

# Enter search phrase
search_input = driver.find_element_by_name("q")
# Click the search button
search_input.send_keys("giant panda")
search_button = driver.find_element_by_id("search_button_homepage")
search_button.click()




# wait for the results to appear

# make sure each word contains "panda"

lists = driver.find_elements_by_class_name("r")
i = 0
for listitem in lists:
    print (listitem)
    i += 1


# search by xpath
si = driver.find_element_by_xpath("//form/input[@id='search_form_input']")
print(type(si))
si.clear()
si.send_keys("merry christmas")
sb = driver.find_element_by_xpath("//form/input[@id='search_button']")
sb.click()

# search by css selector
si = driver.find_element_by_css_selector("#search_form_input")
si.clear()
si.send_keys("happy birthday")
sb = driver.find_element_by_css_selector("#search_button")
sb.click()











time.sleep(10)

driver.quit()