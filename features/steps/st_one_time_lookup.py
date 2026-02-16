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


@then('create list "{list_name}"')
def create_list(context, list_name):
    context.browser.find_element(By.XPATH,
                                 '//button[@id="calling_list"]//div[@class="SelectField_manageWrapper__T1oJh" and contains(@style, "opacity")]').click()
    context.browser.find_element(By.XPATH, '//div[text()="Create List"]').click()
    context.browser.find_element(By.XPATH, '//input[@class="CreateElementModal_textInput__hZ21o"]').send_keys(list_name)
    context.browser.find_element(By.XPATH, '//button[@class="GenericModal_button__lmCtH  GenericModal_confirmButton__BAaWj"]').click()
    time.sleep(3)
    # close share popup if it present
    try:
        context.wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="GenericModal_mainContainer__Wy5u3"]')))
        context.browser.find_element(By.XPATH, '//button[@class="GenericModal_button__lmCtH  GenericModal_cancelButton__lnpHr" and text()="Cancel"]').click()
    except NoSuchElementException:
        pass

@then('press ST one time lookup with "{st_address}" in "{list_name}"')
def st_one_time_lookup(context, st_address, list_name):
    context.browser.find_element(By.XPATH, '//button[@class="Button_btn__W1TTO Button_btnBlue__DoHY2 MainView_btn__2WK2S" and text()="Skip Tracer"]').click()
    context.browser.find_element(By.XPATH, '//button[text()="One Time Lookup"]').click()
    context.browser.find_element(By.XPATH, '//input[@class="SkipTracerModalStyles_addressInput__0fzDv pac-target-input"]').send_keys(st_address)
    context.browser.find_element(By.XPATH,
                                 '//div[@class="pac-item"]').click()
    # wait until address will be founded
    try:
        context.wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="SkipTracerModalStyles_resultGrid__Cxryj"]')))
    except TimeoutException:
        print('Address has not been founded by ST')
    time.sleep(1)
    # press Continue button after address founded by ST
    context.browser.find_element(By.XPATH, '//button[@class="GenericModal_button__lmCtH  GenericModal_confirmButton__BAaWj" and text()="Continue"]').click()
    # input, select list name
    context.browser.find_element(By.XPATH,
                                 '//div[@class="SelectField_headerTitle__K6ZfG" and text()="Calling Lists"]/../..//img[@src="/static/media/menu-search-icon.8a26c4e62c8ed637da9cee5ff1be5a37.svg"]').click()
    context.browser.find_element(By.XPATH, '//input[@class="SelectField_searchBar__XhSCM"]').send_keys(list_name)

    context.browser.find_element(By.XPATH, f'//div[@class="SelectField_selectFieldContentWrapperWhite__Ffxz5"]//div[ text()="{list_name}"]').click()


    # choose keep new and old logic
    try:
        context.browser.find_element(By.XPATH, '//div[@class=" css-hhp87y"]').click()
        context.browser.find_element(By.XPATH, '//div[@id="react-select-2-option-2" and text()="Keep Both"]').click()
    except NoSuchElementException:
        pass
    # click save button
    context.browser.find_element(By.XPATH, '//button[@class="GenericModal_button__lmCtH  GenericModal_confirmButton__BAaWj" and text()="Save"]').click()

    #chech address in CS
    assert context.browser.find_element(By.XPATH, '//div[@class="ContactTitle_addressValue__Zm+1B"]').text in st_address, "ST didn't work. the address didn't match"
    time.sleep(2)
    # Delete searched contact from CS
    context.browser.find_element(By.XPATH, '//button[@class="Button_btn__W1TTO Button_btnBlue__DoHY2" and text()="Actions"]').click()
    context.browser.find_element(By.XPATH, '//div[@class="PopoverMenu_buttonContent__2N3TD" and text()="Delete Contact"]/..').click()
    context.wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="react-confirm-alert"]')))
    context.browser.find_element(By.XPATH, '//div[@class="react-confirm-alert"]//button[@class="confirmAlert_actionButton__gdvBM confirmAlert_actionButtonConfirm__ARIc7" and text()="Delete"]').click()
    context.wait.until(EC.invisibility_of_element_located((By.XPATH, '//div[@class="ContactView_contactContainer__g9F8M"]')))

@then('delete list "{list_name}" from DataDialer')
def delete_list_from_data_dialer(context, list_name):
    # input list name in lists search
    search_lists_button = '//button[@id="calling_list"]//div[@class="SelectField_manageWrapper__T1oJh"]/img[@alt="search-icon"]'
    context.browser.find_element(By.XPATH, search_lists_button).click()
    context.browser.find_element(By.XPATH, '//input[@class="SelectField_searchBarSide__lBnji"]').send_keys(
        list_name)
    # deleting list
    context.browser.find_element(By.CSS_SELECTOR, "div.SelectFieldElement_buttonsContainer__Mi5mD").click()
    context.browser.find_element(By.XPATH,
                                 '//div[@class="SelectFieldElement_menuItem__AcM75" and text()="Delete"]').click()
    context.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.GenericModal_mainContainer__Wy5u3")))
    context.browser.find_element(By.CSS_SELECTOR,
                                 "button.GenericModal_button__lmCtH.GenericModal_confirmButton__BAaWj").click()
    context.wait.until(EC.invisibility_of_element((By.CSS_SELECTOR, "div.GenericModal_mainContainer__Wy5u3")))




