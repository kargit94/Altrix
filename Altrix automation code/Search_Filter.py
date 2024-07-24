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

# Set an implicit wait for general element presence
driver.implicitly_wait(10)

driver.get("https://betashop.alter.game/")

search_field = driver.find_element(By.ID,"auto-suggestion-search")
search_field.send_keys("MariBro")
search_field.send_keys(Keys.RETURN)
time.sleep(5)

drop_down = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'price-sort-select'))
)
drop_down.click()

# Select an option from the drop-down filter
desired_option = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//li[text()='Price High to Low']"))
)
desired_option.click()
time.sleep(5)

clear_button = driver.find_element(By.XPATH, '//*[@id="categories-container"]/div[1]/span')

clear_button.click()

slider=driver.find_element(By.XPATH,'//span[@data-testid="priceRangeSlide"]').click()
actions = ActionChains(driver)
time.sleep(5)
actions.click_and_hold(slider).move_by_offset(-20, 0).release().perform()
time.sleep(5)

driver.quit()