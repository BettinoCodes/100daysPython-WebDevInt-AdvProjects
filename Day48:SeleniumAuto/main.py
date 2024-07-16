#POST THE CODE FOR SELENIUM
#still needs work
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value="cookie")
click_amount = driver.find_element(By.ID, "money")
buy_items = driver.find_elements(By.CSS_SELECTOR, value="#store div b")
cursor = driver.find_element(By.ID, value="buyCursor")
grandma = driver.find_element(By.ID, value="buyGrandma")
factory = driver.find_element(By.ID, value="buyFactory")
mine = driver.find_element(By.ID, value="buyMine")
shipment = driver.find_element(By.ID, value="buyShipment")
alchemylab = driver.find_element(By.ID, value="buyAlchemy lab")
portal = driver.find_element(By.ID, value="buyPortal")
time_machine = driver.find_element(By.ID, value="buyTime machine")
elder_pledge = driver.find_element(By.ID, value="buyElder Pledge")

def keep_going():
    timeout = time.time() + 10   # 5 minutes from now
    test = 0
    while True:
        cookie.click()
        if test == 5 or time.time() > timeout:
            elder_pledge.click()
            time_machine.click()
            portal.click()
            alchemylab.click()
            shipment.click()
            mine.click()
            factory.click()
            grandma.click()
            cursor.click()
            keep_going()
        test = test - 1

keep_going()
# list_prices = []
# for items in range(len(buy_items) - 1):
#     amount = ""
#     for letter in buy_items[items].text:
#         if letter.isdigit():
#             amount += letter
#     print(amount)
#     int_amount = int(amount)
#     list_prices.append(int_amount)
# print(click_amount.text)

# print(list_prices)
