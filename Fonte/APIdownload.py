#Imports Packages
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
#Opens up web driver and goes to Google Images
driver = webdriver.Edge('C:/msedgedriver.exe')
driver.get('https://www.google.com')