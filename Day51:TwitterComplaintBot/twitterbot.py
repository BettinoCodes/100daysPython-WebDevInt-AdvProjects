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

time.sleep(55)

x_out = driver.find_element(By.CSS_SELECTOR, '.notification-dismiss close-btn .svg-icon')
x_out.click()

download_speed = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[4]/div/div/div[2]/div/div/h3')
print(f'Download Speed: {download_speed.text}')

upload_speed = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
print(f'Upload Speed: {upload_speed.text}')

if float(download_speed) < 300:
    driver.get("https://x.com/i/flow/login")
    time.sleep(5)
    user_input = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/div[4]/label/div/div[2]/div/input')
    user_input.send_keys('username')

    time.sleep(5)

    pass_input = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[3]/div/label/div/div[2]/div[1]/input')
    pass_input.send_keys('password')

    message = f'Dear @{wifi_xpath}, I cant take it no more, you better improve ASAP'
    post_input = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
    post_input.send_keys(message)

else:
    print("Your Good")
