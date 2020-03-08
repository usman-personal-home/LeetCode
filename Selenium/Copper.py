#!/usr / bin / env python
from selenium import webdriver
import time

# set webdriver path here it may vary
driver = webdriver.Chrome()
website_URL = "https://copper.com"
driver.get(website_URL)

res_link = driver.find_element_by_xpath("//li[@dropdown-type='resources-nav']")
res_link.click()


elem = driver.find_element_by_link_xpath("//nav[@class='c-nav']//a[@href='https://support.copper.com']")
elem.click()


time.sleep(10)

driver.quit()