from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox(executable_path=r'./geckodriver')

# open wiki page
path = "https://en.wikipedia.org/wiki/Main_Page"
driver.get(path)

# find the search box 
elem = driver.find_element_by_id("searchInput")
driver.execute_script("document.getElementById('searchInput').style.background= 'yellow';") # paint search box yellow
elem.clear()

# search for selenium
query = "selenium software"
elem.send_keys(query)
time.sleep(3)

# click search
elem = driver.find_element_by_id("searchButton")
elem.click()
time.sleep(3)

# click the first of the results
elem = driver.find_elements_by_class_name("mw-search-results")
elem = driver.find_elements_by_xpath("//ul[contains(@class,'mw-search-results')]/li/div/a")[0]

elem.click()
time.sleep(20)
driver.close()
driver.quit()