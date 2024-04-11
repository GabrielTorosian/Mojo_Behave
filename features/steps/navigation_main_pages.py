from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
#import time

use_step_matcher('parse')

DATA_DIALER_BUTTON = '//img[@alt="Data & Dialer"]'
CALENDAR_BUTTON = '//img[@alt="Calendar"]'
REPORTS_BUTTON = '//img[@alt="Reports"]'
PAGES_HEADER = 'div.Generic_subtitle2__3FiOt'
LEADSTORE_BUTTON = '//img[@alt="Leadstore"]'

def navigate_to_page(context, navi_button_xpath, expexted_xpath_selector, expected_text):
    context.browser.find_element(By.XPATH, navi_button_xpath).click()
    context.wait.until(EC.presence_of_element_located((By.XPATH, expexted_xpath_selector)))
    # Assert page is loaded
    header = context.browser.find_element(By.CSS_SELECTOR, PAGES_HEADER)
    assert header.text in expected_text, f"{expected_text} page Error(header)"

@then('go to Data Dialer page')
def navi_data_dieler(context):
    navigate_to_page(context, DATA_DIALER_BUTTON, '//div[@class="Table_bottomActionsAndPaginationContainer__2LZDu"]', "All Contacts")


@then('go to Calendar page')
def navi_calendar(context):
    navigate_to_page(context, CALENDAR_BUTTON, '//div[@class="CalendarTableView_bottomActionBar__2TkCO"]', "Calendar")


@then('go to Reports page')
def navi_call_detail_report(context):
    navigate_to_page(context, REPORTS_BUTTON, '//div[@class="CallDetailReportView_reportButtonsContainer__2_6Xg"]', "Call Detail Report")

@then('go to Session Report')
def navi_session_report(context):
    navigate_to_page(context, '//a[@href="/reports/session-report/"]', '//div[@class="SessionReportView_reportButtonsContainer__2XbpC"]', "Session Report")

@then('go to Call Recording Report')
def navi_call_recordings_report(context):
    navigate_to_page(context, '//a[@href="/reports/call-recordings-report/"]', '//div[@class="CallRecordingsReportView_reportButtonsContainer__15duc"]', "Call Recording Report")

@then('go to Recurring Events Report')
def navi_recurring_events(context):
    navigate_to_page(context, '//a[@href="/reports/recurring-events-report/"]', '//button[@class="RecurringEventsReportView_exportButton__3e8zQ"]', "Recurring Events Report")

@then('go to Posting Report')
def navi_posting_report(context):
    navigate_to_page(context, '//a[@href="/reports/posting-report/"]', '//table[@class="Table_table__2OuB7"]', "Posting Report")

@then('go to Mojo Voice Report')
def navi_mojo_voice_report(context):
    navigate_to_page(context, '//a[@href="/reports/mojo-voice-report/"]', '//button[@class="MojoVoiceReportView_showReportButton__2BImd"]', "Mojo Voice Report")

@then('go to Agent Timesheet Report')
def navi_agent_time_sheet_report(context):
    navigate_to_page(context, '//a[@href="/reports/agent-time-sheet-report/"]', '//div[@class="AgentTimesheetReportView_reportButtonsContainer__eT6o0"]', "Agent Timesheet")

@then('go to Email Status Report')
def navi_email_status_report(context):
    navigate_to_page(context, '//a[@href="/reports/email-status-report/"]', '//div[@class="EmailStatusReportView_reportButtonsContainer__2eQ9q"]', "Email Status Report")

@then('go to Neighborhood Search Update Report')
def navi_nhs_update(context):
    navigate_to_page(context, '//a[@href="/reports/ns-report/"]', '//button[@class="NeighbourhoodSearchReportView_showReportButton__2hW1s"]', "Neighborhood Search Update Report")

@then('go to Leadstore page')
def navi_leadstore(context):
    navigate_to_page(context, LEADSTORE_BUTTON, '//button[@class="LeadstoreHomeMainView_btnLicenseTerms__2PtKx"]', "Welcome To The Leadstore")

