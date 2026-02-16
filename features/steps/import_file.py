from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import os
import time

use_step_matcher('parse')

import_next_button = '//button[@class="Button_btn__W1TTO Button_btnBlue__DoHY2" and text()="Next"]'

@then('press Import file button')
def press_import_file_button(context):
    context.browser.find_element(By.CSS_SELECTOR, "button#import_file").click()
    context.wait.until(EC.presence_of_element_located((By.XPATH, '//img[@alt="data import video 1"]')))
    # assert availability Choose file button
    choose_file_button = context.browser.find_element(By.XPATH, '//button[@class="Button_btn__W1TTO Button_btnLightBlue__yjtPk"]')
    assert choose_file_button.text in "Choose File", "There in no Choose file button"

@then('choose file for import')
def choose_file(context):
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'scoreboard_good_excel_edited.csv')
    choose_file = context.browser.find_element(By.CSS_SELECTOR, "input#actual-btn")
    choose_file.send_keys(file_path)
    # press next button for Step 1
    context.browser.find_element(By.XPATH, import_next_button).click()

@then('Step2 create new list "0101 auto new1" for import')
def create_new_list_for_import(context):
    time.sleep(2)
    context.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div#select_list_or_group_container')))
    # assert lists groups container
    assert context.browser.find_element(By.CSS_SELECTOR, "div#select_list_or_group_container"), "Something with Import:Step 2 page"
    # creation new list for import
    context.browser.find_element(By.CSS_SELECTOR, "button#select_field_1_add_btn").click()
    context.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.GenericModal_mainContainer__Wy5u3")))
    context.browser.find_element(By.CSS_SELECTOR, "input.CreateElementModal_textInput__apHfP").send_keys("0101 auto new1")
    time.sleep(1)
    context.browser.find_element(By.CSS_SELECTOR, "button.GenericModal_button__lmCtH.GenericModal_confirmButton__BAaWj").click()
    context.wait.until(EC.invisibility_of_element((By.CSS_SELECTOR, "div.GenericModal_mainContainer__Wy5u3")))
    time.sleep(4)
    context.wait.until(EC.element_to_be_clickable((By.XPATH, import_next_button)))
    context.browser.find_element(By.XPATH, import_next_button).click()
    #context.browser.execute_script("arguments[0].scrollIntoView();", "button.NextButton_button__1oH4w")
    #context.browser.execute_script("arguments[0].click();", "button.NextButton_button__1oH4w")

@then('Step3 mapping fields')
def mapping_fields(context):
    time.sleep(2)
    context.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div#fields_mapper_container")))
    # assert step 3 spreadsheet table
    assert context.browser.find_elements(By.CSS_SELECTOR,
                                 "table.Table_table__YUzYe"), "Something with Import:Step 3 page"
    #context.browser.find_element(By.XPATH, '//button[@class="Checkbox_Checkbox__2jpzA "]/img[@src="/static/media/checkbox-icon-green-on.787fc9dd.svg"]').click()
    #duplicates_modes_list[0].click()
    time.sleep(1)


    context.browser.find_element(By.XPATH, import_next_button).click()
    try:
        context.wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="confirmAlert_title__faBoy"]')))
        context.browser.find_element(By.XPATH,
                                     '//button[@class="confirmAlert_actionButton__gdvBM confirmAlert_actionButtonConfirm__ARIc7" and text()="Continue Anyway"]').click()
    except NoSuchElementException:
        pass

@then('Step 4 check for duplicates')
def check_for_duplicates(context):
    context.wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="ImportVideoThumbnail_container__qLU8D"]')))
    context.browser.find_element(By.XPATH, '//button[@class="Checkbox_Checkbox__FWKJN "]/div[text()="Entire Database"]').click()
    context.browser.find_element(By.XPATH, '//button[@class="Checkbox_Checkbox__FWKJN "]/div[text()="File Import"]').click()
    context.browser.find_element(By.XPATH, import_next_button).click()

@then('Step 5 finish import')
def finish_import(context):
    time.sleep(2)
    context.wait.until(EC.presence_of_element_located((By.XPATH, '//button[text()="Finish Import"]')))
    # assert step 4
    assert context.browser.find_element(By.XPATH,
                                '//div[@class="FinishImportView_fieldsContainer__G2vpN"]'), "Something with Step 4 page"
    context.browser.find_element(By.XPATH, '//button[text()="Finish Import"]').click()
    #context.wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="GenericModal_contentContainer__2PwLa"]//div[text()="Would you like to skip trace the"]')))
    #context.browser.find_element(By.XPATH, '//button[@class="GenericModal_button__1wlPS  GenericModal_cancelButton__3Scfe" and text()="No"]').click()

@then('close Share agent popup if it present')
def close_st_popup(context):
    try:
        context.browser.find_element(By.XPATH, '//div[@class="GenericModal_buttonsContainer__4CfS5 "]/button[text()="Cancel"]').click()
    except NoSuchElementException:
        pass

@then('close Skip Tracer popup if it present')
def close_st_popup(context):
    try:
        context.browser.find_element(By.XPATH, '//div[@class="GenericModal_buttonsContainer__4CfS5 "]/button[@class="GenericModal_button__lmCtH  GenericModal_cancelButton__lnpHr" and text()="No"]').click()
    except NoSuchElementException:
        pass

@then('search imported contacts')
def search_imported_contacts(context):
    context.wait.until(EC.invisibility_of_element((By.XPATH, '//div[@class="HeavyTaskContainer_heavyTaskOverlay__3oPeK"]')))
    context.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.DummySidebarSearch_searchInput__vPt0P")))
    context.browser.find_element(By.CSS_SELECTOR, "div.DummySidebarSearch_searchInput__vPt0P").click()
    context.browser.find_element(By.CSS_SELECTOR, "input.SidebarSearch_searchInput__TNhew").send_keys("Autotest Knoxville")
    context.browser.find_element(By.XPATH, '//button[@class="SidebarSearch_searchSubmitBtn__OLnSD "]').click()
    time.sleep(2)
    view_all_results_button = context.browser.find_element(By.XPATH, '//button[@class="ResultsActionBtns_btn__OgwPz ResultsActionBtns_btnInactive__Es-5J" and text()="View all results in table"]')
    context.wait.until(EC.presence_of_element_located((By.XPATH, '//button[@class="ResultsActionBtns_btn__OgwPz ResultsActionBtns_btnInactive__Es-5J" and text()="View all results in table"]')))
    time.sleep(2)
    assert view_all_results_button.text in "View All Results In Table", "there is no imported contact in data"
    #context.browser.find_element(By.XPATH, '//div[@class="ContactGroup_arrow__tSmCX"]').click()
    context.browser.find_element(By.XPATH, '//div[@class="SidebarSearch_closeAnchor__hXp0+"]').click()


@then('delete list "0101 auto new1" created during import')
def delete_list_for_import(context):
    search_lists_button = '//button[@id="calling_list"]//div[@class="SelectField_manageWrapper__T1oJh"]/img[@alt="search-icon"]'
    context.browser.find_element(By.XPATH, search_lists_button).click()
    context.browser.find_element(By.XPATH, '//input[@class="SelectField_searchBarSide__lBnji"]').send_keys("0101 auto new1")
    assert context.browser.find_element(By.XPATH, '//div[@class="SelectFieldElement_name__RO3oK"]').text in \
           "0101 auto new1", "no searched list created during import 0101 auto new1"
    # deleting list created during import 0101 auto new1
    context.browser.find_element(By.CSS_SELECTOR, "div.SelectFieldElement_buttonsContainer__Mi5mD").click()
    context.browser.find_element(By.XPATH, '//div[@class="SelectFieldElement_menuItem__AcM75" and text()="Delete"]').click()
    context.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.GenericModal_mainContainer__Wy5u3")))
    context.browser.find_element(By.CSS_SELECTOR, "button.GenericModal_button__lmCtH.GenericModal_confirmButton__BAaWj").click()
    context.wait.until(EC.invisibility_of_element((By.CSS_SELECTOR, "div.GenericModal_mainContainer__Wy5u3")))



