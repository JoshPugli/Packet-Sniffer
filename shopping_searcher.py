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
page = requests.get("https://poshmark.ca/search?query=" + item + "&type=listings&src=dir")
page2 = requests.get("https://www.depop.com/search/?q=" + item)
soup = bs4.BeautifulSoup(page.content, 'html.parser')
soup2 = bs4.BeautifulSoup(page2.content, 'html.parser')
#for i in soup.find_all('li', {'class': "styles__ProductCardContainer"}):
match = soup2.find('li', class_="styles__ProductCardContainer-sc-__sc-13q41bc-8 cAJcNu")
print(match)
