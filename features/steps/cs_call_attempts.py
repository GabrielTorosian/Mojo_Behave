from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import os
import time

use_step_matcher('parse')

GLOBAL_SEARCH_FIELD_SELECTOR = "button.DummySidebarSearch_searchInputContainer__uV8MF"

@then('search contact "{contact_name}"')
def search_contact(context, contact_name):
    context.browser.find_element(By.CSS_SELECTOR, GLOBAL_SEARCH_FIELD_SELECTOR).click()
    context.browser.find_element(By.CSS_SELECTOR, "input.SidebarSearch_searchInput__TNhew").clear()
    context.browser.find_element(By.CSS_SELECTOR, "input.SidebarSearch_searchInput__TNhew").send_keys(contact_name)

    context.browser.find_element(By.XPATH, '//button[@class="SidebarSearch_searchSubmitBtn__OLnSD "]').click()
    time.sleep(3)
    context.wait.until(EC.presence_of_element_located((By.XPATH, '//button[text()="View all results in table"]')))
    context.browser.find_element(By.XPATH,
                                 '//div[@class="ContactGroup_arrow__Cnq6b"]').click()
    # open contact
    context.browser.find_element(By.XPATH,
                                 '//div[@class="SearchResults_resultField__EPRqp SearchResults_resultItemFullName__ZgABr"]').click()
    # close search bar
    context.browser.find_element(By.CSS_SELECTOR, "input.SidebarSearch_searchInput__TNhew").clear()
    context.browser.find_element(By.XPATH, '//div[@class="SidebarSearch_closeAnchor__hXp0+"]').click()

@then('cs activities section')
def cs_activities_test(context):
    MARK_AS_CONTACT_BUTTON = '//button[@class="Button_btn__W1TTO Button_btnLightBlue__yjtPk" and text()="Mark As Contact"]'
    CREATE_CALL_ATTEMPT_POPUP = '//div[@class="GenericModal_mainContainer__Wy5u3"]'
    context.browser.find_element(By.XPATH, '//button[@id="activities"]').click()
    context.wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="style_header__wTvSF" and text()="Information:"]')))
    # mark as contact
    context.browser.find_element(By.XPATH, MARK_AS_CONTACT_BUTTON).click()
    context.wait.until(EC.visibility_of_element_located((By.XPATH, CREATE_CALL_ATTEMPT_POPUP)))
    # input note
    context.browser.find_element(By.XPATH, '//textarea[@id="note"]').send_keys("autotest Mark As Contact button pressed")
    time.sleep(4)