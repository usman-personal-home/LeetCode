#!/usr / bin / env python 
from selenium import webdriver
import time

# set webdriver path here it may vary 
driver = webdriver.Chrome()
website_URL = "https://www.google.co.in/"
driver.get(website_URL)

# After how many seconds you want to refresh the webpage 
# Few website count view if you stay there 
# for a particular time 
# you have to figure that out 
refreshrate = int(5)

# This would keep running until you stop the compiler.
i = 0
while True:
    time.sleep(refreshrate)
    driver.refresh()
    i += 1

    if i > 5:
        break

driver.quit()
