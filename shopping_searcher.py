import requests
import bs4
from selenium import webdriver
import time

item = input("Search up the item you want to shop (be as specific as possible): ")
item = item.replace(" ", "+")
print(item)
driver = webdriver.Chrome()
driver.get("https://www.google.com/search?tbm=shop&sxsrf=APq-WBsOYkD0SxliFLYTcFpPMsFczDBECw:1645561272028&q=" + item + "&spell=1&sa=X&ved=0ahUKEwjVqMy4kZT2AhX7oHIEHYJxD3AQBQjaCigA&biw=1536&bih=754&dpr=1.25")
