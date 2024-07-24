import time
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the Chrome driver
driver = webdriver.Chrome()
driver.maximize_window()

# Set an implicit wait for general element presence
driver.implicitly_wait(10)

driver.get("https://betashop.alter.game/")

try:
    element_to_hover = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, r"#__next > div > div.bg-pattern.min-h-\[calc\(100vh-7rem\)\].bg-opacity-40.bg-cover.bg-fixed.bg-no-repeat.pb-12.md\:pb-24 > div.fixed.w-full.bg-modelBg.backdrop-blur-lg > div.ml-auto.hidden.h-12.border-b-2.border-gray-800.md\:grid > div > div.col-start-1.col-end-4.flex.flex-row.items-center > div > button > div > span"))
    )
except Exception as e:
    print(f"Element not found with CSS Selector. Error: {e}")

actions = ActionChains(driver)

if element_to_hover:
    actions.move_to_element(element_to_hover).perform()
    try:
        outdoor_assets = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, r"#__next > div > div > div.fixed.w-full.bg-modelBg.backdrop-blur-lg > div.ml-auto.hidden.h-12.border-b-2.border-gray-800.md\:grid > div > div.col-start-1.col-end-4.flex.flex-row.items-center > div > div > div:nth-child(5)"))
        )
        outdoor_assets.click()
        # Get the page title
        page_title = driver.title
        print(f"Page Title: {page_title}")

        # Get the current URL
        current_url = driver.current_url
        print(f"Current URL: {current_url}")
    except Exception as e:
        print(f"Outdoor assets element not found. Error: {e}")

time.sleep(5)
OutdoorAsset=driver.find_element(By.XPATH,'//span[text()="Grass"]').click()
time.sleep(5)
# Close the browser
driver.quit()


# search_field = driver.find_element(By.ID,"auto-suggestion-search")
# search_field.send_keys("MariBro")
# search_field.send_keys(Keys.RETURN)
# time.sleep(2)