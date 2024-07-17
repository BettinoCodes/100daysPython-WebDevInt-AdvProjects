from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC

import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value="cookie")
click_amount = driver.find_element(By.ID, "money")

buy_items = driver.find_elements(By.CSS_SELECTOR, value="#store div b")

# for i in range(len(buy_items) - 1, -1, -1):
#     print(f"item{i + 1}: {buy_items[i].text} \n\n")

print(click_amount.text)

def click_cookie(duration=10):
    print("Clicking the cookie")
    end_time = time.time() + duration
    while time.time() < end_time:
        cookie.click()
        



def keep_going():
    global click_amount, buy_items
    while True:
        click_cookie()
        time.sleep(.5)
        click_amount = driver.find_element(By.ID, "money")
        int_cookie_amount = int(click_amount.text)
        buy_items = driver.find_elements(By.CSS_SELECTOR, value="#store div b")
        try:
            for i in range(len(buy_items) - 2, -1, -1):
                split_text = buy_items[i].text.split("-")[1].split(" ")[1]
                new_split_number = int(split_text.replace(',', ''))
                int_cookie_amount = int(click_amount.text)
                if new_split_number <= int_cookie_amount:
                    print(f"{new_split_number} <= {int_cookie_amount}")
                    buy_items[i].click()  # Click the buy item if conditions are met
        except StaleElementReferenceException:
            print("StaleElementReferenceException: Re-fetching elements...")
            # Re-fetch elements here (assuming how buy_items and click_amount are fetched)
            click_amount = driver.find_element(By.ID, "money")
            buy_items = driver.find_elements(By.CSS_SELECTOR, value="#store div b")
            continue  # Continue the loop after re-fetching elements
        
        

keep_going()


