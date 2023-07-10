# Importing required libraries

# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Amazon.ca homepage
driver.get("https://flipp.com/")
time.sleep(3)

# Selecting a flyer
flipLink = driver.find_element("xpath","/html/body/div/main/section[1]/div/div/div/a")
# laptop_link = driver.find_element("By.CSS_SELECTOR","span[data-component-type='s-product-image'] a")
flipLink.click()
time.sleep(5)

ad_link = driver.find_element("xpath","/html/body/div[2]/flipp-listing-page/flipp-page/download-app-banner/div/button")
ad_link.click()
time.sleep(5)

# check the flyer
check_flyer = driver.find_element("xpath","/html/body/div[2]/flipp-listing-page/flipp-page/div/main/flipp-listing-page-content/div/div[2]/span[1]/flipp-flyer-listing-item/div/a")
check_flyer.click()
time.sleep(5)

checkout_fashion = driver.find_element("xpath","/html/body/div[2]/flipp-flyer-page/flipp-page/flipp-dialog/div/nav/div[2]/div[1]/div/div/a[13]/span[1]")
checkout_fashion.click()
time.sleep(5)

# Closing the webdriver
driver.close()
