from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value="cookie")
click_amount = driver.find_element(By.ID, "money")

buy_items = driver.find_elements(By.CSS_SELECTOR, value="#store div b")

#just to reduce exception errors
time.sleep(5)

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
                    print(f"clicking:{buy_items[i].text.split("-")[0]}")
                    buy_items[i].click()
                    # Re-fetch elements here to avoid errors
                    click_amount = driver.find_element(By.ID, "money")
                    buy_items = driver.find_elements(By.CSS_SELECTOR, value="#store div b")
                    time.sleep(.5)
        except StaleElementReferenceException:
            print("StaleElementReferenceException: Re-fetching elements...")
            # Re-fetch elements here to avoid errors
            click_amount = driver.find_element(By.ID, "money")
            buy_items = driver.find_elements(By.CSS_SELECTOR, value="#store div b")
            continue  # Continue the loop after re-fetching element
        
        

keep_going()
