from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


@then('click Create Contact button')
def click_create_contact_button(context):
    # wait for the "Create Contact" button to be clickable, then click it
    context.wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//a[@data-tip="Create Contact"]'))).click()
    # wait for the contact form to fully load — check that input fields are present.
    # Old selector (SelectField_selectFieldContainer__2R3j0) is outdated (CSS module hash changed).
    # Input fields are a reliable indicator that the form is ready for filling.
    assert context.wait.until(EC.presence_of_all_elements_located(
        (By.XPATH, '//input[@class="InputRow_inputElement__A3E9s"]')
    )), "Create Contact page has not loaded"

@then('fill fields and create group for a new contact')
def fill_fields_new_conatact(context):
    # wait for all input fields to be present before filling them
    input_fields = context.wait.until(EC.presence_of_all_elements_located(
        (By.XPATH, '//input[@class="InputRow_inputElement__A3E9s"]')))
    input_fields[0].send_keys('Autocreate Contact01')
    input_fields[1].send_keys('test_email@op.net')
    input_fields[2].send_keys('9991111111')
    input_fields[3].send_keys('123 Test Street')
    input_fields[4].send_keys('Los Angeles')
    input_fields[5].send_keys('CA')
    input_fields[6].send_keys('90001')
    # open "Add group" dialog and create a new group
    context.wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//button[@id="select_field_3_add_btn"]'))).click()
    context.wait.until(EC.visibility_of_element_located(
        (By.XPATH, '//input[@placeholder="Enter Name"]'))).send_keys('Autotest CrContact group')
    context.wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//button[text()="Save"]'))).click()
    # After clicking "Save", a modal overlay appears while the group is being saved.
    # Wait for the overlay to disappear before clicking "Create Contact",
    # otherwise the click lands on the overlay and fails with ElementClickInterceptedException.
    context.wait.until(EC.invisibility_of_element_located(
        (By.CSS_SELECTOR, "div.ReactModal__Overlay")))
    # click "Create Contact" button to submit the form
    context.wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//button[text()="Create Contact"]'))).click()
    # verify the contact was created — its name must appear on the page
    assert context.wait.until(EC.presence_of_element_located(
        (By.XPATH, '//div[text()="Autocreate Contact01"]')
    )), "Contact Autocreate Contact01 has not been created"

@then('create note "{note_text}"')
def create_note(context, note_text):
    # wait for the note textarea to be visible, then type the note
    note_input = context.wait.until(EC.visibility_of_element_located(
        (By.XPATH, '//textarea[@class="ContactNotes_noteTextarea__Y6FTC"]')))
    note_input.send_keys(note_text)
    # click "Post" button to save the note
    context.wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//button[@class="ContactNotes_postNote__1VKsb ContactNotes_btnWhiteBlue__JG2Re" and text()="Post"]'))).click()
    # wait for the saved note text to appear and verify it matches what we typed
    saved_note = context.wait.until(EC.visibility_of_element_located(
        (By.XPATH, '//span[@style="white-space: pre-wrap; word-break: break-word;"]')))
    assert note_text in saved_note.text, "Note is not created!"

'''
@then('edit created note')
def edit_created_note(context):
    #ActionChains(context.browser).move_to_element(By.XPATH, '//div[@class="ContactNote_innerContainer__gkgB8 "]').perform()
    context.browser.find_element(By.XPATH, '//button[@class="Button_btn__1Lkv5 Button_btnTransparent__2Z_qD Button_icononly__KBa2O"]/img[@src="/static/media/edit-icon.e3113363.svg"]').click()
    context.browser.find_element(By.XPATH, '//textarea[@class="ContactNotes_noteTextarea__moyQ3" and @placeholder="Can not be empty..."]').clear()
    context.browser.find_element(By.XPATH,
                                 '//textarea[@class="ContactNotes_noteTextarea__moyQ3" and @placeholder="Can not be empty..."]').send_keys("this is an auto note_edited")
    context.browser.find_element(By.XPATH, '//button[@class="Button_btn__1Lkv5 Button_btnLightBlue__ziG13" and text()="Save"]').click()
    time.sleep(1)
    saved_edited_note = context.browser.find_element(By.XPATH, '//span[@style="white-space: pre-wrap; word-break: break-word;"]')
    assert saved_edited_note.text in "this is an auto note_edited", "Note is not edited!"

@then('delete created note')
def delete_created_note(context):
    #element = context.wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="ContactNote_innerContainer__gkgB8 "]'))
    #ActionChains(context.browser).move_to_element(element).perform()
    context.browser.find_elements(By.XPATH, '//div[@class="ContactNote_controls__mRZ5G "]/button[@class="Button_btn__1Lkv5 Button_btnTransparent__2Z_qD Button_icononly__KBa2O"]')[2].click()
    context.browser.find_element(By.XPATH, '//div[@class="PopoverConfirm_controls__3pO39"]/button[@class="Button_btn__1Lkv5 Button_btnSalmon__2k6WX" and text()="Delete"]').click()
    saved_edited_note = context.browser.find_element(By.XPATH,
                                                     '//span[@style="white-space: pre-wrap; word-break: break-word;"]')
    try:
        context.wait.until(EC.invisibility_of_element_located((By.XPATH, saved_edited_note)))
        print("Note has been deleted")
    except:
        print("Note has NOT been deleted!")
'''


@then('delete contact Autocreate Contact01')
def delete_created_contact(context):
    # click "Actions" button in the contact sheet
    context.wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//button[@class="Button_btn__W1TTO Button_btnBlue__DoHY2" and text()="Actions"]'))).click()
    # click "Delete Contact" in the dropdown menu
    context.wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//div[@class="PopoverMenu_buttonContent__2N3TD" and text()="Delete Contact"]'))).click()
    # wait for the confirmation dialog to appear — assert so test fails if it doesn't
    assert context.wait.until(EC.presence_of_element_located(
        (By.XPATH, '//div[@class="confirmAlert_message__JGnt1" and text()="Are you sure you want to delete this contact?"]')
    )), "Delete contact confirmation popup did not appear"
    # click "Delete" in the confirmation dialog
    context.wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//button[@class="confirmAlert_actionButton__gdvBM confirmAlert_actionButtonConfirm__ARIc7" and text()="Delete"]'))).click()
    # verify the contact has been removed from the page
    assert context.wait.until_not(EC.presence_of_element_located(
        (By.XPATH, '//div[text()="Autocreate Contact01"]')
    )), "Contact Autocreate Contact01 was not deleted"

@then('delete created group Autotest CrContact group')
def delete_group(context):
    # open the groups search dropdown
    context.wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//button[@id="groups"]//img[@src="/static/media/menu-search-icon.8a26c4e62c8ed637da9cee5ff1be5a37.svg"]/..'))).click()
    # search for the group by name
    context.wait.until(EC.visibility_of_element_located(
        (By.XPATH, '//input[@class="SelectField_searchBarSide__lBnji"]'))).send_keys("Autotest CrContact group")
    # click the manage (three dots) icon next to the group
    context.wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//div[@class="SelectFieldElement_name__RO3oK" and text()="Autotest CrContact group"]/..//div[@class="SelectFieldElement_manageWrapper__eP6VG"]'))).click()
    # click "Delete" in the manage menu
    context.wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//div[@class="SelectFieldElement_menuItem__AcM75" and text()="Delete"]'))).click()
    # confirm deletion in the modal dialog
    context.wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//button[@class="GenericModal_button__lmCtH  GenericModal_confirmButton__BAaWj" and text()="Delete"]'))).click()
    # verify the group has been removed from the list
    assert context.wait.until_not(EC.presence_of_element_located(
        (By.XPATH, '//div[@class="SelectFieldElement_name__RO3oK" and text()="Autotest CrContact group"]')
    )), "Group 'Autotest CrContact group' was not deleted"
