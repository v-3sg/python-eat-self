# 1) Create a test case that will open amazon bestsellers page
# and verify there are 5 links

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


# init driver
driver = webdriver.Chrome(executable_path='C:/Users/v33ja/Desktop/Careerist/Automation_Course/code/python-selenium-automation/chromedriver.exe')
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')

# count the number of href tags via find_methods
expected_links = 5

actual_links = driver.find_elements(By.XPATH, "//*[contains(@href, 'ref=zg_bs_tab')]")
counted_links = len(actual_links)

# verify the links found
assert expected_links == counted_links, f'Expected {expected_links} links but got {counted_links}'

print('Test case passed')

driver.quit()



# 2) Create test case to add any product into the cart
# make sure it's there
# check number of items in cart OR open cart and verify it's there

# init driver
driver = webdriver.Chrome(executable_path='C:/Users/v33ja/Desktop/Careerist/Automation_Course/code/python-selenium-automation/chromedriver.exe')
driver.maximize_window()

# open the url
sleep(4)
driver.get('https://www.amazon.com')

# search for product I want
driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('freenove big hexapod raspberry pi 4')
driver.find_element(By.ID, 'nav-search-submit-button').click()

# select product from results
driver.find_element(By.XPATH, "//*[contains(@href, 'Freenove-Big-Hexapod-Robot-Kit-Raspberry-Pi')]").click()

# add product to cart and deny computer protection plan
driver.find_element(By.XPATH, "//input[@id='add-to-cart-button' and @value='Add to Cart']").click()
sleep(4)
driver.find_element(By.XPATH, "//input[@class='a-button-input' and @aria-labelledby='attachSiNoCoverage-announce']").click()
sleep(4)

expected_items = 1
actual_items = driver.find_elements(By.XPATH, "//*[contains(@class, 'nav-cart-1')]")
counted_items = len(actual_items)

# verify the links found
assert expected_items == counted_items, f'Expected {expected_items} links but got {counted_items}'

print('Test case passed')

driver.quit()


