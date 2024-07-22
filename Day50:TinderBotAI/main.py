from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv, dotenv_values
import os
from selenium.webdriver.common.action_chains import ActionChains


load_dotenv()


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://tinder.onelink.me/9K8a/3d4abb81")
time.sleep(3)

login_button= driver.find_element(By.XPATH, value='//*[@id="q-225181968"]/div/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
login_button.click()

time.sleep(3)

# driver_facebook = driver.get("https://www.facebook.com/login.php?skip_api_login=1&api_key=464891386855067&kid_directed_site=0&app_id=464891386855067&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fv2.8%2Fdialog%2Foauth%3Fapp_id%3D464891386855067%26cbt%3D1721577223499%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfed04b9c9dca0dde6%2526domain%253Dtinder.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Ftinder.com%25252Ffb17bfbea61470a89%2526relation%253Dopener%26client_id%3D464891386855067%26display%3Dpopup%26domain%3Dtinder.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Ftinder.com%252F%26locale%3Den_US%26logger_id%3Dfb118167a2929c73d%26origin%3D1%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df282621cd4535c1b1%2526domain%253Dtinder.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Ftinder.com%25252Ffb17bfbea61470a89%2526relation%253Dopener%2526frame%253Df6852544afbbd9514%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Duser_birthday%252Cuser_photos%252Cemail%252Cuser_likes%26sdk%3Djoey%26version%3Dv2.8%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df282621cd4535c1b1%26domain%3Dtinder.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Ftinder.com%252Ffb17bfbea61470a89%26relation%3Dopener%26frame%3Df6852544afbbd9514%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=popup&locale=en_US&pl_dbl=0")

driver.window_handles[0]
popup = driver.window_handles[1]
driver.switch_to.window(popup)
email_input = driver.find_element(By.XPATH, value='//*[@id="email"]')
password_input = driver.find_element(By.ID, value="pass")

email_input.send_keys(os.getenv("MY_EMAIL"))
password_input.send_keys(os.getenv("MY_PASSWORD"))

login_fb = driver.find_element(By.ID, value="loginbutton")
login_fb.click()

time.sleep(7)
print(driver.window_handles)

# Switch to the popup window (assuming it is the second window opened)
#//*[@id="mount_0_0_0n"]/div/div/div/div/div/div/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div/div/div/div[1]
continue_button = driver.find_element(By.CSS_SELECTOR, value='div span span')
print(continue_button.text)
continue_button.click()

time.sleep(5)
driver.switch_to.window(driver.window_handles[0])
first_one = driver.find_element(By.XPATH, value='//*[@id="q-225181968"]/div/div[1]/div/div/div[3]/button[1]/div[2]/div[2]')
first_one.click()

time.sleep(2)
element_to_hover_over = driver.find_elements(By.CSS_SELECTOR, value='.w1u9t036 .c9iqosj .lxn9zzn')
actions = ActionChains(driver)
# Move to the element and perform the hover action
actions.move_to_element(element_to_hover_over[1]).perform()

# time.sleep(5)
# #driver.find_element(By.XPATH, value='//*[@id="q-225181968"]/div/div/div/div/div[3]/button[2]').click()
buttons = driver.find_element(By.CSS_SELECTOR, value='.w1u9t036 .c9iqosj .lxn9zzn')
buttons.click()

time.sleep(2)

# acc_cookie = driver.find_element(By.XPATH, value='//*[@id="q1503199108"]/div/div[1]/div/div/div/main/div/div/div[1]/div/div[4]/div/div[2]/button')
# acc_cookie.click()

time.sleep(1)

acc_cookie2 = driver.find_element(By.CSS_SELECTOR, value='.w1u9t036')
acc_cookie2.click()

time.sleep(1)

buttonsl = driver.find_elements(By.CSS_SELECTOR, value="button span span")
for i in buttonsl:
    print(i.text)

time.sleep(3)
nope_button = buttonsl[1]

x = 0
while x < 4:
    nope_button.click()
    time.sleep(4)
    x += 1

