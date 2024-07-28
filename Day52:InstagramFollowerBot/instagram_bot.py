#WORK IN PROGRESS
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv, dotenv_values
import os
from selenium.webdriver.common.action_chains import ActionChains



load_dotenv()


class InstagramBot:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.action = ActionChains(self.driver)
    
    def bot_program(self):
        self.driver.get("https://www.instagram.com/accounts/login/?next=%2Flogin%2F&source=desktop_nav")
        time.sleep(3)
        login_fb = self.driver.find_element(By.CSS_SELECTOR, "button ._ab37")
        login_fb.click()
        fb_email = self.driver.find_element(By.ID, "email")
        fb_email.send_keys(os.getenv("MY_EMAIL"))
        fb_pass = self.driver.find_element(By.ID, "pass")
        fb_pass.send_keys(os.getenv("MY_PASSWORD"))
        fb_login_button = self.driver.find_element(By.ID, "loginbutton")
        fb_login_button.click()

        time.sleep(3)

        self.action.click().perform()
        time.sleep(1)
        continue_button = self.driver.find_element(By.CSS_SELECTOR, "._1-aa ._1-ac button")
        continue_button.click()
        time.sleep(5)

        # go_back_ig = self.driver.find_element(By.XPATH('//*[@id="mount_0_0_nN"]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div/div/span/a'))

        go_back_ig = self.driver.find_element(By.CSS_SELECTOR, "div div span a")
        go_back_ig.click()

        time.sleep(2)

        not_now = self.driver.find_elements(By.CSS_SELECTOR, "div div div button")
        not_now[-1].click()

        time.sleep(1)

        # search = self.driver.find_element(By.XPATH, '//*[@id="mount_0_0_p4"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div[2]/span/div/a/div')
        search = self.driver.find_elements(By.CSS_SELECTOR, 'div span span')
        search2 = []
        for i in search:
            if i.text == "Search":
                search2.append(i)

        for i in search2:
            print(i.text)

        search_button = search2[0]
        search_button.click()
        
        



ig_bot = InstagramBot()
ig_bot.bot_program()
