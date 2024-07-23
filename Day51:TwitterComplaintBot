#WORK IN PROGRESS
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv, dotenv_values
import os
load_dotenv()


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.speedtest.net/")

time.sleep(4)

wifi_xpath = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[4]/div/div[2]/div/div/div/div[2]')
print(wifi_xpath.text)

go_button = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
go_button.click()

time.sleep(50)

download_speed = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[4]/div/div/div[2]/div/div/h3')
print(f'Download Speed: {download_speed}')

upload_speed = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
print(f'Upload Speed: {upload_speed}')
