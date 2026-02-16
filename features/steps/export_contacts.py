from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

import time
use_step_matcher('parse')

group_name="autotest_group"

@then('go to group "{group_name}"')
def go_to_group(context, group_name):
    context.browser.find_element(By.XPATH,
                                 '//button[@id="groups"]//img[@src="/static/media/menu-search-icon.8a26c4e62c8ed637da9cee5ff1be5a37.svg"]/..').click()
    context.browser.find_element(By.XPATH, '//input[@class="SelectField_searchBarSide__lBnji"]').send_keys(group_name)
    context.browser.find_element(By.XPATH, f'//div[@class="SelectFieldElement_name__RO3oK" and text()="{group_name}"]').click()
    #context.wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@class=" Checkbox_title__1isC4" and text()="Select All"]')))
    time.sleep(3)

@then('select all export contacts')
def select_all_export_contacts(context):
    #ActionChains(context.browser).move_to_element(context.browser.find_element(By.XPATH, '//div[@class="ContactTable_selectAllCheckboxContainer__3zGw4"]')).perform()
    # select all contacts
    context.browser.find_element(By.XPATH, '//div[@class="ContactTable_selectAllCheckboxContainer__FzQur"]').click()
    time.sleep(1)
    context.browser.find_element(By.XPATH, '//div[@class=" Checkbox_title__JDF6b" and text()="Select All"]').click()
    time.sleep(1)
    # press Export button
    context.browser.find_elements(By.XPATH, '//a[@class="IconButton_iconButton__zrc2u IconButton_transparent__DNCHe  IconButton_iconButtonWithText__A29vo ContactTable_transparentOnDark__1wZti ContactTable_bottomActionsBtn__dyObz"]')[2].click()
    context.wait.until(EC.element_to_be_clickable((By.XPATH, '//span[@class="IconButton_childrenContainer__pUIKl" and text()="Export"]')))
    context.browser.find_element(By.XPATH, '//button[@class="GenericModal_button__lmCtH  GenericModal_confirmButton__BAaWj" and text()="Export"]').click()
    context.wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="heavyTaskToastId"]//div[text()="File Successfully Generated"]')))
    assert "File Successfully Generated" in context.browser.find_element(By.XPATH, '//div[@id="heavyTaskToastId"]//div[text()="File Successfully Generated"]').text, "Export file did not imported!!"



