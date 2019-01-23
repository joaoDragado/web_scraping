import requests, bs4
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException



browser = webdriver.PhantomJS('/archive/Leisure/geckodriver')
print('got browser')
browser.get('https://www.python.org/')
print('got login_page')
mainnav = browser.find_element_by_id('mainnav')
print(nav.text)

# assert browser.current_url == 'https://www.tumblr.com/login'

# email = browser.find_element_by_id('signup_determine_email')
# email.clear()
# email.send_keys(usermail)
# email.send_keys(Keys.RETURN)

# pwlogin = browser.find_element_by_class_name('forgot_password_link')
# pwlogin.click()

# signup = browser.find_element_by_id('signup_password')
# signup.clear()
# signup.send_keys(pwd)
# signup.send_keys(Keys.RETURN)


# # wait = WebDriverWait( browser, 1 )

# # try:
# #     page_loaded = wait.until_not(lambda browser: browser.current_url == login_page)
# # except TimeoutException:
# #     self.fail( "Loading timeout expired" )

# if browser.current_url == landing_page :
#     print('Login Sucessful!')

