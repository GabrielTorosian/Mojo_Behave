from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import os
import time

use_step_matcher('parse')

@then('press Import file button')
def press_import_file_button(context):
    context.browser.find_element(By.CSS_SELECTOR, "button#import_file").click()
    context.wait.until(EC.presence_of_element_located((By.XPATH, '//img[@alt="data import video"]')))
    # assert availability Choose file button
    choose_file_button = context.browser.find_element(By.CSS_SELECTOR,
                                              "div.WelcomeView_section__2A-sM>button.Button_btn__1Lkv5")
    assert choose_file_button.text in "Choose File", "There in no Choose file button"

@then('choose file for import')
def choose_file(context):
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'scoreboard_good_excel_edited.csv')
    choose_file = context.browser.find_element(By.CSS_SELECTOR, "input#actual-btn")
    choose_file.send_keys(file_path)
    # press next button for Step 1
    context.browser.find_element(By.CSS_SELECTOR, "button.NextButton_button__1oH4w").click()

@then('Step2 create new list "0101 auto new1" for import')
def create_new_list_for_import(context):
    context.wait.until(EC.presence_of_element_located((By.XPATH, '//img[@alt="Import Step 2"]')))
    # assert lists groups container
    assert context.browser.find_element(By.CSS_SELECTOR, "div#select_list_or_group_container"), "Something with Import:Step 2 page"
    # creation new list for import
    context.browser.find_element(By.CSS_SELECTOR, "button#select_field_1_add_btn").click()
    context.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.GenericModal_title__34niQ")))
    context.browser.find_element(By.CSS_SELECTOR, "input.CreateElementModal_textInput__-5kex").send_keys("0101 auto new1")
    context.browser.find_element(By.CSS_SELECTOR, "button.GenericModal_button__1wlPS.GenericModal_confirmButton__1VoK5").click()
    context.wait.until(EC.invisibility_of_element((By.CSS_SELECTOR, "div.GenericModal_title__34niQ")))
    time.sleep(3)
    context.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.NextButton_button__1oH4w")))
    context.browser.find_element(By.CSS_SELECTOR, "button.NextButton_button__1oH4w").click()

@then('Step3 mapping fields')
def mapping_fields(context):
    context.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div#fields_mapper_container")))
    # assert step 3
    assert context.browser.find_elements(By.CSS_SELECTOR,
                                 "div.MappingView_stepDescription__2k0Pq"), "Something with Import:Step 3 page"
    duplicates_modes_list = context.browser.find_elements(By.CSS_SELECTOR, "div.Checkbox_title__1isC4")
    duplicates_modes_list[0].click()
    time.sleep(1)
    context.browser.find_element(By.CSS_SELECTOR, "button.NextButton_button__1oH4w").click()

@then('Step 4 finish import')
def finish_import(context):
    context.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.FinishImportView_videoThumbnail__1WMjp")))
    # assert step 4
    assert context.browser.find_element(By.CSS_SELECTOR,
                                "div.FinishImportView_mappedFieldsContainer__2TJUr"), "Something with Step 4 page"
    context.browser.find_element(By.CSS_SELECTOR, "button.FinishImportView_genericButton__3NMuh").click()

@then('search imported contacts')
def search_imported_contacts(context):
    context.wait.until(EC.invisibility_of_element((By.XPATH, '//div[@class="HeavyTaskContainer_heavyTaskOverlay__3oPeK"]')))
    context.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.DummySidebarSearch_searchInput__r-3bx")))
    context.browser.find_element(By.CSS_SELECTOR, "div.DummySidebarSearch_searchInput__r-3bx").click()
    context.browser.find_element(By.CSS_SELECTOR, "input.SidebarSearch_searchInput__33nNB").send_keys("Autotest Knoxville")
    time.sleep(2)
    context.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.styles_btn__1cyQv")))
    view_all_results_button = context.browser.find_element(By.CSS_SELECTOR, "button.styles_btn__1cyQv")

    assert view_all_results_button.text in "View All Results In Table", "there is no imported contact in data"
    time.sleep(2)
    context.browser.find_element(By.CSS_SELECTOR, "div.SidebarSearch_closeAnchorArrow__4Gvt6").click()

@then('delete list "0101 auto new1" created during import')
def delete_list_for_import(context):
    context.browser.find_element(By.XPATH, '//img[@src="/static/media/menu-callingLists-icon.e3784ea3.svg"]').click()
    context.browser.find_element(By.CSS_SELECTOR, "input.SelectField_searchBarSide__1MlwY").send_keys("0101 auto new1")
    assert context.browser.find_element(By.CSS_SELECTOR, "div.SelectFieldElement_name__hX6bR").text in \
           "0101 auto new1", "no searched list created during import 0101 auto new1"
    # deleting list created during import 0101 auto new1
    context.browser.find_element(By.CSS_SELECTOR, "div.SelectFieldElement_manageWrapper__2-hy9").click()
    context.browser.find_elements(By.CSS_SELECTOR, "div.SelectFieldElement_menuItem__3GbRz")[4].click()
    context.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.GenericModal_title__34niQ")))
    context.browser.find_element(By.CSS_SELECTOR, "button.GenericModal_button__1wlPS.GenericModal_confirmButton__1VoK5").click()
    context.wait.until(EC.invisibility_of_element((By.CSS_SELECTOR, "div.GenericModal_title__34niQ")))



