from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import os
import time

use_step_matcher('parse')

import_next_button = '//button[@class="Button_btn__W1TTO Button_btnBlue__DoHY2" and text()="Next"]'

@then('press Import file button')
def press_import_file_button(context):
    # click the Import file button and wait for the import page to load
    context.wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button#import_file"))).click()
    context.wait.until(EC.presence_of_element_located(
        (By.XPATH, '//img[@alt="data import video 1"]')))
    # verify the "Choose File" button is present
    choose_file_button = context.wait.until(EC.visibility_of_element_located(
        (By.XPATH, '//button[@class="Button_btn__W1TTO Button_btnLightBlue__yjtPk"]')))
    assert "Choose File" in choose_file_button.text, "There is no Choose File button"

@then('choose file for import')
def choose_file(context):
    # send the file path directly to the hidden file input (no click needed)
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'scoreboard_good_excel_edited.csv')
    choose_file = context.browser.find_element(By.CSS_SELECTOR, "input#actual-btn")
    choose_file.send_keys(file_path)
    # press "Next" button to proceed to Step 2
    context.wait.until(EC.element_to_be_clickable(
        (By.XPATH, import_next_button))).click()

@then('Step2 create new list "0101 auto new1" for import')
def create_new_list_for_import(context):
    # wait for Step 2 page to load (lists/groups selection container)
    context.wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div#select_list_or_group_container')))
    assert context.browser.find_element(
        By.CSS_SELECTOR, "div#select_list_or_group_container"), "Something with Import: Step 2 page"
    # click "Add new list" button and wait for the creation modal
    context.wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button#select_field_1_add_btn"))).click()
    context.wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "div.GenericModal_mainContainer__Wy5u3")))
    # type the new list name and confirm
    context.wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "input.CreateElementModal_textInput__apHfP"))).send_keys("0101 auto new1")
    # Wait for the form to process the input before clicking confirm.
    # No visible DOM change to wait for — short sleep is necessary.
    time.sleep(1)
    context.wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button.GenericModal_button__lmCtH.GenericModal_confirmButton__BAaWj"))).click()
    context.wait.until(EC.invisibility_of_element(
        (By.CSS_SELECTOR, "div.GenericModal_mainContainer__Wy5u3")))
    # press "Next" to proceed to Step 3
    context.wait.until(EC.element_to_be_clickable(
        (By.XPATH, import_next_button))).click()
    #context.browser.execute_script("arguments[0].scrollIntoView();", "button.NextButton_button__1oH4w")
    #context.browser.execute_script("arguments[0].click();", "button.NextButton_button__1oH4w")

@then('Step3 mapping fields')
def mapping_fields(context):
    # wait for Step 3 mapping page to load
    context.wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "div#fields_mapper_container")))
    assert context.browser.find_elements(
        By.CSS_SELECTOR, "table.Table_table__YUzYe"), "Something with Import: Step 3 page"
    #context.browser.find_element(By.XPATH, '//button[@class="Checkbox_Checkbox__2jpzA "]/img[@src="/static/media/checkbox-icon-green-on.787fc9dd.svg"]').click()
    #duplicates_modes_list[0].click()
    # press "Next" to proceed
    next_btn = context.wait.until(EC.element_to_be_clickable(
        (By.XPATH, import_next_button)))
    context.browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", next_btn)
    time.sleep(0.5)
    next_btn.click()
    # An alert "Continue Anyway" may appear if there are mapping warnings.
    # Use text-based selector instead of class-based — CSS module hashes differ
    # between local Chrome and BrowserStack, causing the alert to go undetected.
    # Wait up to full 15s — locally the alert can take longer to appear.
    try:
        context.wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//button[text()="Continue Anyway"]'))).click()
    except TimeoutException:
        pass  # No mapping warning alert — proceed normally

@then('Step 4 check for duplicates')
def check_for_duplicates(context):
    # Wait for Step 4 page to fully load by waiting for the "Entire Database" checkbox.
    # Don't use ImportVideoThumbnail_container — it also exists on Step 3, making it unreliable.
    # Use text-based selectors to avoid CSS module hash differences between Chrome versions.
    context.wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//div[text()="Entire Database"]/parent::button'))).click()
    context.wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//div[text()="File Import"]/parent::button'))).click()
    # press "Next" to proceed
    context.wait.until(EC.element_to_be_clickable(
        (By.XPATH, import_next_button))).click()

@then('Step 5 finish import')
def finish_import(context):
    # wait for the final review page to load
    context.wait.until(EC.presence_of_element_located(
        (By.XPATH, '//button[text()="Finish Import"]')))
    assert context.browser.find_element(
        By.XPATH, '//div[@class="FinishImportView_fieldsContainer__G2vpN"]'), "Something with Step 5 page"
    # click "Finish Import" to start the import process
    context.wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//button[text()="Finish Import"]'))).click()
    #context.wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="GenericModal_contentContainer__2PwLa"]//div[text()="Would you like to skip trace the"]')))
    #context.browser.find_element(By.XPATH, '//button[@class="GenericModal_button__1wlPS  GenericModal_cancelButton__3Scfe" and text()="No"]').click()

@then('close Share agent popup if it present')
def close_share_agent_popup(context):
    """Close the 'Share agent' popup if it appears after import. Uses find_elements to avoid exception."""
    popups = context.browser.find_elements(
        By.XPATH, '//div[@class="GenericModal_buttonsContainer__4CfS5 "]/button[text()="Cancel"]')
    if popups:
        popups[0].click()

@then('close Skip Tracer popup if it present')
def close_skip_tracer_popup(context):
    """Close the 'Skip Tracer' popup if it appears after import. Uses find_elements to avoid exception."""
    popups = context.browser.find_elements(
        By.XPATH, '//div[@class="GenericModal_buttonsContainer__4CfS5 "]/button[@class="GenericModal_button__lmCtH  GenericModal_cancelButton__lnpHr" and text()="No"]')
    if popups:
        popups[0].click()

@then('search imported contacts')
def search_imported_contacts(context):
    # wait for the heavy task overlay (import progress) to disappear
    context.wait.until(EC.invisibility_of_element(
        (By.XPATH, '//div[@class="HeavyTaskContainer_heavyTaskOverlay__3oPeK"]')))
    # open global search and type imported contact name
    context.wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "div.DummySidebarSearch_searchInput__vPt0P"))).click()
    context.wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "input.SidebarSearch_searchInput__TNhew"))).send_keys("Autotest Knoxville")
    context.browser.find_element(
        By.XPATH, '//button[@class="SidebarSearch_searchSubmitBtn__OLnSD "]').click()
    # wait for the "View all results" button to confirm contacts were found
    view_all_btn = context.wait.until(EC.presence_of_element_located(
        (By.XPATH, '//button[contains(@class,"ResultsActionBtns_btn") and text()="View all results in table"]')))
    assert view_all_btn.text, "There are no imported contacts in data"
    # close the search sidebar
    context.browser.find_element(
        By.XPATH, '//div[@class="SidebarSearch_closeAnchor__hXp0+"]').click()


@then('delete list "0101 auto new1" created during import')
def delete_list_for_import(context):
    # open the lists search dropdown
    search_lists_button = '//button[@id="calling_list"]//div[@class="SelectField_manageWrapper__T1oJh"]/img[@alt="search-icon"]'
    context.wait.until(EC.element_to_be_clickable(
        (By.XPATH, search_lists_button))).click()
    # search for the imported list by name
    context.wait.until(EC.visibility_of_element_located(
        (By.XPATH, '//input[@class="SelectField_searchBarSide__lBnji"]'))).send_keys("0101 auto new1")
    # verify the list was found
    list_element = context.wait.until(EC.visibility_of_element_located(
        (By.XPATH, '//div[@class="SelectFieldElement_name__RO3oK"]')))
    assert "0101 auto new1" in list_element.text, \
        "No searched list created during import: 0101 auto new1"
    # click the manage (three dots) button next to the list
    context.wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "div.SelectFieldElement_buttonsContainer__Mi5mD"))).click()
    # click "Delete" in the manage menu
    context.wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//div[@class="SelectFieldElement_menuItem__AcM75" and text()="Delete"]'))).click()
    # confirm deletion in the modal dialog
    context.wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button.GenericModal_button__lmCtH.GenericModal_confirmButton__BAaWj"))).click()
    context.wait.until(EC.invisibility_of_element(
        (By.CSS_SELECTOR, "div.GenericModal_mainContainer__Wy5u3")))
