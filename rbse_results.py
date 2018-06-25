# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 10:13:47 2018

@author: Lenovo
"""
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup as bs

url="http://rajresults.nic.in/resbserx18.htm"

browser=webdriver.Chrome("C:/Users/Lenovo/Downloads/chromedriver_win32/chromedriver.exe")
browser.get(url)


sleep(2)

roll_no=browser.find_element_by_name("roll_no")
roll="0123456"
roll_no.send_keys(roll)

sleep(2)
get=browser.find_element_by_name("B1")

get.click()
