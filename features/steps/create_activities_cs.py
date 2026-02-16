from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

use_step_matcher('parse')

DATA_DIALER_BUTTON = '//button[@id="menu-button-my-data"]'
DATA_TABLE = "table.Table_tableFixed__qZs5B"
GLOBAL_SEARCH_FIELD_SELECTOR = "button.DummySidebarSearch_searchInputContainer__uV8MF"
ACTIVITY_CONTACT = "Knoxville2711"

APP_BUTTON_CS = '//img[@src="/static/media/add-appt-icon.234ba54595b96cf8ccdbf070e8490726.svg"]'
TASK_BUTTON_CS = '//img[@src="/static/media/add-task-icon.07218b3bd865353f3b0cb03f245ead71.svg"]'
FU_BUTTON_CS = '//img[@src="/static/media/add-f_call-icon.7f902c41024728b3801ffee4d091aa93.svg"]'

ACTIVITY_POPUP_SELECTOR = "div.GenericModal_mainContainer__Wy5u3"

APP_TITLE_FIELD = "input.AppointmentPopup_textInput__5xi4k"
APP_DESCRIPTION_FIELD = "textarea.AppointmentPopup_descriptionTextarea__dNpWU"

TASK_TITLE_FIELD = "input.TaskPopup_textInput__6lWYN"
TASK_DESCRIPTION_FIELD = "textarea.TaskPopup_descriptionTextarea__gvOes"

FU_TITLE_FIELD = "input.FollowUpCallPopup_textInput__AMlxe"
FU_DESCRIPTION_FIELD = "textarea.FollowUpCallPopup_descriptionTextarea__f3aPG"


def activity_creation_cs(context, create_activity_button, title_field, description_field, activity_name):
    # go to Data Dialer
    context.browser.find_element(By.XPATH, DATA_DIALER_BUTTON).click()
    context.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, DATA_TABLE)))
    # search contact
    context.browser.find_element(By.CSS_SELECTOR, GLOBAL_SEARCH_FIELD_SELECTOR).click()
    context.browser.find_element(By.CSS_SELECTOR, "input.SidebarSearch_searchInput__TNhew").clear()
    context.browser.find_element(By.CSS_SELECTOR, "input.SidebarSearch_searchInput__TNhew").send_keys(ACTIVITY_CONTACT)

    context.browser.find_element(By.XPATH, '//button[@class="SidebarSearch_searchSubmitBtn__OLnSD "]').click()
    time.sleep(3)
    context.wait.until(EC.presence_of_element_located((By.XPATH, '//button[text()="View all results in table"]')))
    context.browser.find_element(By.XPATH,
                                 '//div[@class="ContactGroup_arrow__Cnq6b"]').click()
    # open contact
    #context.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.SearchResults_resultField__1Mqdp.SearchResults_resultItemFullName__21KTL")))
    context.browser.find_element(By.XPATH,
                         '//div[@class="SearchResults_resultField__EPRqp SearchResults_resultItemFullName__ZgABr"]').click()
    # close search bar
    context.browser.find_element(By.CSS_SELECTOR, "input.SidebarSearch_searchInput__TNhew").clear()
    context.browser.find_element(By.XPATH, '//div[@class="SidebarSearch_closeAnchor__hXp0+"]').click()
    # create activity
    context.browser.find_element(By.XPATH, create_activity_button).click()
    context.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ACTIVITY_POPUP_SELECTOR)))
    # input title, description
    context.browser.find_element(By.CSS_SELECTOR, title_field).send_keys(f"{activity_name} title autotest")
    context.browser.find_element(By.CSS_SELECTOR, description_field).send_keys(
        f"{activity_name} description autotest")
    time.sleep(3)
    context.browser.find_element(By.CSS_SELECTOR, "button.GenericModal_button__lmCtH.GenericModal_confirmButton__BAaWj").click()
    context.wait.until(EC.invisibility_of_element((By.CSS_SELECTOR, "div.GenericModal_mainContainer__Wy5u3")))
    # click on Activities section in CS
    context.browser.find_element(By.XPATH, "//button[@id='activities' and text()='Activities']").click()
    # check activity's title
    assert context.browser.find_element(By.CSS_SELECTOR, "span.ContactActivity_title__vMR3N").text in f"{activity_name} title autotest", \
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
    calendar_search = context.browser.find_element(By.CSS_SELECTOR, "input.CalendarTableView_searchInput__LKjjP")
    calendar_search.clear()
    calendar_search.send_keys(ACTIVITY_CONTACT)
    time.sleep(1)
    context.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "tbody.Table_tbody__WYAlK")))
    # delete contact
    context.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.ContextMenu_contextButton__hZpmC.false.false")))
    context.browser.find_element(By.CSS_SELECTOR, "button.ContextMenu_contextButton__hZpmC.false.false").click()
    context.wait.until(EC.presence_of_element_located((By.XPATH, '//button[@class="PopoverMenu_menuButton__Vmhae"]/div[text()="Delete"]')))
    context.browser.find_element(By.XPATH, '//button[@class="PopoverMenu_menuButton__Vmhae"][div[text()="Delete"]]').click()
    context.browser.find_element(By.CSS_SELECTOR,
                         "button.confirmAlert_actionButton__gdvBM.confirmAlert_actionButtonConfirm__ARIc7").click()
    context.wait.until(EC.invisibility_of_element((By.CSS_SELECTOR, 'div.confirmAlert_confirmAlert__Dg54z')))

@when('create Appointment from CS')
def create_app(context):
    activity_creation_cs(context, APP_BUTTON_CS, APP_TITLE_FIELD, APP_DESCRIPTION_FIELD, "app")

@step('go to Calendar')
def go_to_calendar(context):
    context.browser.find_element(By.XPATH, '//div[text()="Calendar"]').click()
    # Warning confirmation
    context.browser.find_element(By.CSS_SELECTOR,
                         "button.confirmAlert_actionButton__gdvBM.confirmAlert_actionButtonConfirm__ARIc7").click()
    context.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, DATA_TABLE)))
    '''
    checkbox_all = context.browser.find_elements(By.CSS_SELECTOR, '//div[@class="CalendarSidebar_filterContainer__qP9J4 CalendarSidebar_filterSelected__WFbPV" ]//button[@class="Checkbox_Checkbox__FWKJN "]')
    print(checkbox_all[0])
    print(checkbox_all[0].is_selected)
    if not checkbox_all[0].is_selected():
        checkbox_all.click()'''

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















