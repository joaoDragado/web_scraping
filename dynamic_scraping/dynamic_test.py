from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# instantiate a chrome options object so you can set the size and headless preference
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--window-size=1920x1080')
chrome_options.add_argument("--disable-notifications")
# directory of chrome driver
chrome_driver = '/archive/Studies/webdrivers/chromedriver'
# initialize/launch chrome
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)


# go to Reddit and click the I'm Feeling Lucky button
driver.get('https://www.reddit.com/')

# launch the user dropdown menu (top right)
driver.find_element_by_id('USER_DROPDOWN_ID').click()
#WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'USER_DROPDOWN_ID'))).click()

# select night mode
driver.find_element_by_class_name('egZVll').click()
#WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'egZVll'))).click()

# capture the screen
driver.get_screenshot_as_file('capture.png')
