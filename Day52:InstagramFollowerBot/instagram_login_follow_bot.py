#WORK IN PROGRESS
#Only Works For The First 10

# login_buttton = self.driver.find_element(By.CSS_SELECTOR, "div div a")
        # login_buttton.click()
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv, dotenv_values
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

load_dotenv()

class InstagramBot:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.action = ActionChains(self.driver)
    
    def bot_program(self):
        self.driver.get("https://www.instagram.com")

        time.sleep(2)
        
        username = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        username.send_keys(os.getenv("MY_EMAIL"))

        password = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(os.getenv("MY_PASSWORD"))

        login_button = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]')
        login_button.click()

        time.sleep(3)

        self.driver.get("https://www.instagram.com/{IG_ACCOUNT}/")
        time.sleep(3)

        followers_button = self.driver.find_element(By.CSS_SELECTOR, 'header section:nth-of-type(3) ul li:nth-of-type(2) div a')
        followers_button.click()

        time.sleep(2)
        
        # scrollable_container = self.driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')
        # self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", scrollable_container)
        scrollable_container = self.driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')
        self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", scrollable_container)
        
        follower_buttons = self.driver.find_elements(By.XPATH, f'/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div/div/div/div/div/div/button')
        
        print(len(follower_buttons))
        for j in follower_buttons:
                j.click()
                time.sleep(2)
        self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", scrollable_container)


ig_bot = InstagramBot()
ig_bot.bot_program()
