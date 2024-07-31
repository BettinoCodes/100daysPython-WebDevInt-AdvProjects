#Using BeautifulSoup to scrape and using selenium to input into forms to input an excel sheet automatically
#can put into classes
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import requests
from pprint import pprint


response = requests.get(" https://appbrewery.github.io/Zillow-Clone/")
site_html = response.content

# print(site_html)

soup = BeautifulSoup(site_html, "html.parser")
# print(soup.prettify())
location_details = []
list_of_properties = soup.find_all(name="div", class_="StyledPropertyCardDataWrapper")
for i in list_of_properties:
    dict_price_link = {}
    price = i.find(name="span", class_="PropertyCardWrapper__StyledPriceLine")
    link_add = i.find(name='a', href=True)
    address = i.find(name="address")
    price = price.text
    i = 1
    prc = ""
    while price[i] != "+" and price[i] != "/":
        if price[i].isdigit():
            prc += price[i]
        i += 1
    location_details.append({
        "address": address.get_text().strip(),
        "price": float(prc),
        "link": link_add["href"]
    })

time.sleep(2)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfUhQq0TIv2APX7S2lRyq4w3by1hYoPuezPo86tcmJA9xmV7w/viewform?usp=sf_link")


for location in location_details:
    property_address = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    property_price = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    property_link = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    property_address.send_keys(location["address"])
    property_price.send_keys(location["price"])
    property_link.send_keys(location["link"])
    submit_button.click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "a").click()
    time.sleep(1)



