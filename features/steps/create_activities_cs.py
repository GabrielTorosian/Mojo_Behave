from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

use_step_matcher('parse')

DATA_DIALER_BUTTON = '//button[@class="MainMenuButton_button__Wxat6 "]/img[@alt="Data & Dialer"]'
DATA_TABLE = "table.Table_tableFixed__3MyJT"
GLOBAL_SEARCH_FIELD_SELECTOR = "button.DummySidebarSearch_searchInputContainer__46fue"
ACTIVITY_CONTACT = "Knoxville2711"

APP_BUTTON_CS = '//img[@src="/static/media/add-appt-icon.3aeee97e.svg"]'
TASK_BUTTON_CS = '//img[@src="/static/media/add-task-icon.816cf495.svg"]'
FU_BUTTON_CS = '//img[@src="/static/media/add-f_call-icon.b35c81a6.svg"]'

ACTIVITY_POPUP_SELECTOR = "div.GenericModal_mainContainer__ecgLX"

APP_TITLE_FIELD = "input.AppointmentPopup_textInput__3Q_R4"
APP_DESCRIPTION_FIELD = "textarea.AppointmentPopup_descriptionTextarea__1zZTz"

TASK_TITLE_FIELD = "input.TaskPopup_textInput__2wRI9"
TASK_DESCRIPTION_FIELD = "textarea.TaskPopup_descriptionTextarea__28A6J"

FU_TITLE_FIELD = "input.FollowUpCallPopup_textInput__2BYvH"
FU_DESCRIPTION_FIELD = "textarea.FollowUpCallPopup_descriptionTextarea__3tsG1"


def activity_creation_cs(context, create_activity_button, title_field, description_field, activity_name):
    # go to Data Dialer
    context.browser.find_element(By.XPATH, DATA_DIALER_BUTTON).click()
    context.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, DATA_TABLE)))
    # search contact
    context.browser.find_element(By.CSS_SELECTOR, GLOBAL_SEARCH_FIELD_SELECTOR).click()
    context.browser.find_element(By.CSS_SELECTOR, "input.SidebarSearch_searchInput__33nNB").clear()
    context.browser.find_element(By.CSS_SELECTOR, "input.SidebarSearch_searchInput__33nNB").send_keys(ACTIVITY_CONTACT)
    time.sleep(3)
    context.wait.until(EC.presence_of_element_located((By.XPATH, '//button[@class="styles_btn__1cyQv"]')))
    context.browser.find_element(By.XPATH,
                                 '//button[@class="SidebarSearch_btnTransparent__P--MT ContactGroup_contactGroupHeader__23rSz"]').click()
    # open contact
    #context.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.SearchResults_resultField__1Mqdp.SearchResults_resultItemFullName__21KTL")))
    context.browser.find_element(By.XPATH,
                         '//div[@class="SearchResults_resultField__1Mqdp SearchResults_resultItemFullName__21KTL"]').click()
    # create activity
    context.browser.find_element(By.XPATH, create_activity_button).click()
    context.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ACTIVITY_POPUP_SELECTOR)))
    # input title, description
    context.browser.find_element(By.CSS_SELECTOR, title_field).send_keys(f"{activity_name} title autotest")
    context.browser.find_element(By.CSS_SELECTOR, description_field).send_keys(
        f"{activity_name} description autotest")
    time.sleep(3)
    context.browser.find_element(By.CSS_SELECTOR, "button.GenericModal_button__1wlPS.GenericModal_confirmButton__1VoK5").click()
    context.wait.until(EC.invisibility_of_element((By.CSS_SELECTOR, "div.GenericModal_mainContainer__ecgLX")))
    # click on Activities section in CS
    context.browser.find_element(By.CSS_SELECTOR, "#contactPopover div.SidebarLink_link__3AKAg#activities").click()
    # check activity's title
    assert context.browser.find_element(By.CSS_SELECTOR, "span.ContactActivity_title__1LxXW").text in f"{activity_name} title autotest", \
        f"{activity_name} was not created"

'''
def go_to_calendar(context):
    context.browser.find_element(By.XPATH, '//img[@src="/static/media/menu-calendar.a14c050d.svg"]').click()
    context.browser.find_element(By.CSS_SELECTOR,
                         "button.confirmAlert_actionButton__nRyS0.confirmAlert_actionButtonConfirm__2nOW7").click()
    context.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, DATA_TABLE)))
'''

def search_delete_activity_in_calendar(context):
    # search contact
    calendar_search = context.browser.find_element(By.CSS_SELECTOR, "input.CalendarTableView_searchInput__18SdX")
    calendar_search.clear()
    calendar_search.send_keys(ACTIVITY_CONTACT)
    context.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "tr.Table_tr__1tLPZ.Table_trClickable__1UdAH")))
    # delete contact
    context.browser.find_element(By.CSS_SELECTOR, "button.ContextMenu_contextButton__3LrLO").click()
    context.browser.find_elements(By.CSS_SELECTOR, "button.PopoverMenu_menuButton__2MQjV")[2].click()
    context.browser.find_element(By.CSS_SELECTOR,
                         "button.confirmAlert_actionButton__nRyS0.confirmAlert_actionButtonConfirm__2nOW7").click()
    context.wait.until(EC.invisibility_of_element((By.CSS_SELECTOR, "tr.Table_tr__1tLPZ.Table_trClickable__1UdAH")))

@when('create Appointment from CS')
def create_app(context):
    activity_creation_cs(context, APP_BUTTON_CS, APP_TITLE_FIELD, APP_DESCRIPTION_FIELD, "app")

@step('go to Calendar')
def go_to_calendar(context):
    context.browser.find_element(By.XPATH, '//img[@src="/static/media/menu-calendar.a14c050d.svg"]').click()
    context.browser.find_element(By.CSS_SELECTOR,
                         "button.confirmAlert_actionButton__nRyS0.confirmAlert_actionButtonConfirm__2nOW7").click()
    context.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, DATA_TABLE)))
    checkbox_all = context.browser.find_elements(By.XPATH, '//button[@class="Checkbox_Checkbox__2jpzA "]')[0]
    print(checkbox_all.is_selected)
    if not checkbox_all.is_selected():
        checkbox_all.click()

@then('search App and delete it')
def search_delete_app_in_calendar(context):
    search_delete_activity_in_calendar(context)

@when('create Task from CS')
def create_task(context):
    activity_creation_cs(context, TASK_BUTTON_CS, TASK_TITLE_FIELD, TASK_DESCRIPTION_FIELD, "task")

@then('search Task and delete it')
def search_delete_task_in_calendar(context):
    search_delete_activity_in_calendar(context)

@when('create FU call from CS')
def create_fu(context):
    activity_creation_cs(context, FU_BUTTON_CS, FU_TITLE_FIELD, FU_DESCRIPTION_FIELD, "FU call")


@then('search FU call and delete it')
def search_delete_fu_in_calendar(context):
    search_delete_activity_in_calendar(context)















