'''
1) Find optimal locators for Amazon Create Account page elements

Amazon logo, by class, "a-icon a-icon-logo"
Create account, by class, "a-spacing-small"
Your name field, by css selector, "input#ap_customer_name"
Mobile number or email field, by css selector, "input#ap_email"
Password field, by css selector, "input#ap_password"
Password requirement text, by class, "a-alert-content"
Re-enter password field, by css selector, "input#ap_password_check"
Continue button, by css selector, "input.a-button-input"
Conditions of Use hyperlink, by XPATH, //*[contains(@href, '/ref=ap_register_notification_condition_of_use')]
Privacy Notice hyperlink, by XPATH, //*[contains(@href, '/ref=ap_register_notification_privacy_notice')]
Sign-In hyperlink, by XPATH, //*[contains(@href, '/ap/signin')]
'''

# 2) Update a test case
# verify logged out user sees sign in menu
# when clicking on Returns and Orders

from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path='C:/Users/v33ja/Desktop/Careerist/Automation_Course/code/python-selenium-automation/chromedriver.exe')
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

# click Orders link
driver.find_element(By.XPATH, "//*[contains(@href, '/order-history')]").click()

expected_result = "Amazon Sign-In"
actual_result = driver.title

assert expected_result == actual_result, f'Expected {expected_result} but got {actual_result}'

print('Test case passed')

driver.quit()
