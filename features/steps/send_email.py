from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import time

use_step_matcher('parse')

@then('search and open contact "{contact_name}"')
def search_open_contact(context, contact_name):
    context.wait.until(EC.invisibility_of_element((By.XPATH, '//div[@class="HeavyTaskContainer_heavyTaskOverlay__3oPeK"]')))
    context.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.DummySidebarSearch_searchInput__vPt0P")))
    context.browser.find_element(By.CSS_SELECTOR, "div.DummySidebarSearch_searchInput__vPt0P").click()
    context.browser.find_element(By.CSS_SELECTOR, "input.SidebarSearch_searchInput__TNhew").send_keys(contact_name)
    context.browser.find_element(By.XPATH, '//button[@class="SidebarSearch_searchSubmitBtn__OLnSD "]').click()

    '''context.browser.find_element(By.CSS_SELECTOR, "button.DummySidebarSearch_searchInputContainer__46fue").click()
    context.browser.find_element(By.CSS_SELECTOR, "input.SidebarSearch_searchInput__33nNB").clear()
    context.browser.find_element(By.CSS_SELECTOR, "input.SidebarSearch_searchInput__33nNB").send_keys(contact_name)
    context.browser.find_element(By.XPATH, '//button[@class="SidebarSearch_searchSubmitBtn__2b0wj "]').click()'''
    time.sleep(3)

    context.wait.until(EC.presence_of_element_located((By.XPATH, '//button[text()="View all results in table"]')))
    context.browser.find_element(By.XPATH,
                                 '//div[@class="ContactGroup_arrow__Cnq6b"]').click()
    # open contact
    context.browser.find_element(By.XPATH,
                                 '//div[@class="SearchResults_resultField__EPRqp SearchResults_resultItemFullName__ZgABr"]').click()

@then('send manual CS email')
def send_manual_cs_email(context):
    context.wait.until(EC.element_to_be_clickable((By.XPATH, '//img[@src="/static/media/email-blue.4435cb49b51ebef93d2c2fc93ea2f23f.svg"]/..')))
    context.browser.find_element(By.XPATH, '//img[@src="/static/media/email-blue.4435cb49b51ebef93d2c2fc93ea2f23f.svg"]/..').click()
    context.wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="GenericModal_mainContainer__Wy5u3"]')))
    # Choose Existing Template
    #context.browser.find_element(By.XPATH, '//div[@class=" css-hhp87y"]').click()
    context.browser.find_element(By.XPATH,
                                 '//div[@class="GenericModal_contentContainer__Pkxd5"]//input[contains(@id, "react-select-") and contains(@id, "-input")]').send_keys('autotest email template')
    context.browser.find_element(By.XPATH,
                                 '//div[@class="GenericModal_contentContainer__Pkxd5"]//input[contains(@id, "react-select-") and contains(@id, "-input")]').send_keys(Keys.ENTER)
    time.sleep(3)
    # press button Send Email
    context.browser.find_element(By.XPATH, '//button[text()="Send Email"]').click()
    context.wait.until(EC.invisibility_of_element((By.XPATH, '//div[@class="GenericModal_mainContainer__Wy5u3"]')))
    try:
        context.wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="Toastify__toast Toastify__toast--success"]')))
        #context.browser.find_element(By.XPATH, '//div[@class="Toastify__toast Toastify__toast--success"]')
        #context.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".Toastify__toast--success")))
    except TimeoutException:
        print("No popup that email was successfully sent")
    time.sleep(5)
    context.browser.find_element(By.XPATH, '//button[@class="ContactHeader_close__7YIL9"]').click()
    #context.wait.until(EC.invisibility_of_element((By.XPATH, '//div[@class="Toastify__toast Toastify__toast--success"]')))
    #time.sleep(3)



