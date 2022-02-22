import requests
import bs4
from selenium import webdriver
import time

item = input("Search up the item you want to shop (be as specific as possible): ")
item = item.replace(" ", "+")
print(item)
driver = webdriver.Chrome()
driver2 = webdriver.Chrome()
driver.get("https://poshmark.ca/search?query=" + item + "&type=listings&src=dir")
driver2.get("https://www.depop.com/search/?q=" + item)

