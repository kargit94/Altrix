import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

# Initialize the Chrome driver
driver = webdriver.Chrome()
driver.maximize_window()

# Wait
driver.implicitly_wait(10)

# Open the web page
driver.get("https://betashop.alter.game/")

connect = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div/span')
connect.click()

driver.switch_to.window(driver.window_handles[1])

discord = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div/div/div[2]/span[1]'))
)

# Click the 'Discord' button
discord.click()
time.sleep(3)

# Create an account
register = driver.find_element(By.XPATH,'//div[text()="Register"]')
register.click()
time.sleep(3)

# email = driver.find_element(By.XPATH,'//input[@name="email"]')
# email.send_keys("karthiga@gmail.com")
# time.sleep(3)
#
# DisplayName = driver.find_element(By.XPATH,'//input[@name="global_name"]')
# DisplayName.click()
# DisplayName.send_keys("karthi")
# time.sleep(3)
#
# UserName = driver.find_element(By.XPATH,'//input[@name="username"]')
# UserName.send_keys("Test_Member123")
# time.sleep(3)
#
# Password = driver.find_element(By.XPATH,'//input[@name="password"]')
# Password.send_keys("karthiga123#")
# time.sleep(3)

Month=driver.find_element(By.XPATH,'//div[@class="month_a57e6a"]')
time.sleep(3)
webdriver.ActionChains(driver).send_keys_to_element(Month,'November',Keys.ENTER).perform()
time.sleep(3)

Day=driver.find_element(By.XPATH,'//div[@class="day_a57e6a"]')
time.sleep(3)
webdriver.ActionChains(driver).send_keys_to_element(Day,'24',Keys.ENTER).perform()
time.sleep(3)

Year=driver.find_element(By.XPATH,'//div[@class="year_a57e6a"]')
webdriver.ActionChains(driver).send_keys_to_element(Year,'1998',Keys.ENTER).perform()
time.sleep(3)

# ClickBtn=driver.find_element(By.XPATH,'//button[@type="submit"]').click()
# time.sleep(5)

#Login
# email/PhNo = driver.find_element(By.XPATH,'//input[@name="email"]')
# email/PhNo.send_keys("karthiga@gmail.com")
# time.sleep(3)

# Password = driver.find_element(By.XPATH,'//input[@name="password"]')
# Password.send_keys("karthiga123#")
# time.sleep(3)

#LoginBtn=driver.find_element(By.XPATH,'//button[@type="submit"]').click()

#Create Assets

# Upload=driver.find_element(By.XPATH,'//button[@id="upload"]').click()
# time.sleep(3)
# Body=driver.find_element(By.XPATH,'//div[@id="category1"]').click()
# time.sleep(3)
# ChooseBody=driver.find_element(By.XPATH,'//button[@id="upload"]').click()
# time.sleep(3)
#
#
# Upload3DAsset=driver.find_element(By.XPATH,'//span[text()=" + Upload 3D Asset"]').send_keys('')
# time.sleep(3)
# Name=driver.find_element(By.XPATH,'//button[@id="upload"]').send_keys('Smart Watch')
# time.sleep(3)
# Description=driver.find_element(By.XPATH,'//button[@id="upload"]').send_keys('Lorem ipsum posuere lobortis est risus nam imperdiet molestie neque, diam eget lobortis purus porta aliquam maecenas in cras sed, cubilia arcu iaculis luctus purus ligula commodo varius. Ac porta lacinia nulla sociosqu fusce non urna aenean, etiam tincidunt curabitur id morbi habitasse.')
# time.sleep(3)
# TandC=driver.find_element(By.XPATH,'//input[@id="agreement"]').click()
# time.sleep(3)
# SubmitForReview=driver.find_element(By.XPATH,'//span[text()="Submit for Review"]').is_enabled()
# time.sleep(3)
# SubmitForReview=driver.find_element(By.XPATH,'//span[text()="Submit for Review"]').click()
# time.sleep(3)