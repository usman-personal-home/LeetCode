from selenium import webdriver
import time
"""
find_element_by_id
find_element_by_name
find_element_by_xpath
find_element_by_link_text
find_element_by_partial_link_text
find_element_by_tag_name
find_element_by_class_name
find_element_by_css_selector

To find multiple elements (these methods will return a list):

find_elements_by_name
find_elements_by_xpath
find_elements_by_link_text
find_elements_by_partial_link_text
find_elements_by_tag_name
find_elements_by_class_name
find_elements_by_css_selector
"""


# Google Chrome
driver = webdriver.Chrome()
# Navigate to the application home page
driver.get("http://www.google.com")


# get the search textbox
search_field = driver.find_element_by_name("q")

# enter search keyword and submit
search_field.send_keys("Selenium WebDriver Interview questions")
search_field.submit()


# get the list of elements which are displayed after the search
# currently on result page using find_elements_by_class_name method
lists = driver.find_elements_by_class_name("r")

# get the number of elements found
print ("Found " + str(len(lists)) + " searches:")

# iterate through each element and print the text that is
# name of the search

i = 0
for listitem in lists:
    print (listitem.get_attribute("innerHTML"))
    i += 1
    if i > 10:
        break

# close the browser window
time.sleep(15)
driver.quit()