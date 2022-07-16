from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@when('Click on cart icon')
def access_cart(context):
    context.driver.find_element(By.XPATH, "//*[contains(@href, '/cart')]").click()

@then('Results for cart shown')
def verify_cart_results(context):
    expected_result = "https://www.amazon.com/gp/cart/view.html/ref=nav_bb_cart"
    actual_result = context.driver.current_url
    assert expected_result == actual_result, f'Expected {expected_result} but got {actual_result}'
