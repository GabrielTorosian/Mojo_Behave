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
PAGES_HEADER = '//div[@class="Generic_subtitle2__FY6pW"]'
LEADSTORE_BUTTON = '//img[@alt="Leadstore"]'

SETTINGS_BUTTON = '//img[@alt="Settings"]'
SETTING_VIEW_CONTAINER = '//div[@class="SettingsView_container__+jzFZ"]'
INTEGRATION_DESCRIPTION = '//div[@class="Generic_text1__aH3dk"]'


def navigate_to_page(context, navi_button_xpath, expeсted_xpath_selector, expected_text):
    context.browser.find_element(By.XPATH, navi_button_xpath).click()
    context.wait.until(EC.presence_of_element_located((By.XPATH, expeсted_xpath_selector)))
    # Assert page is loaded
    header = context.browser.find_element(By.XPATH, PAGES_HEADER)
    assert header.text in expected_text, f"{expected_text} page Error(header)"

@then('go to Data Dialer page')
def navi_data_dieler(context):
    navigate_to_page(context, DATA_DIALER_BUTTON, '//div[@class="Table_bottomActionsAndPaginationContainer__UxAWQ"]', "All Contacts")
    context.wait.until(EC.presence_of_element_located((By.XPATH, '//table[@class="Table_tableFixed__qZs5B"]')))


@then('go to Calendar page')
def navi_calendar(context):
    navigate_to_page(context, CALENDAR_BUTTON, '//div[@class="CalendarTableView_bottomActionBar__VzqlC"]', "Calendar")


@then('go to Reports page')
def navi_call_detail_report(context):
    navigate_to_page(context, REPORTS_BUTTON, '//div[@class="ReportFiltersView_filtersContainer__hynQm "]', "Call Detail Report")

@then('go to Session Report')
def navi_session_report(context):
    navigate_to_page(context, '//a[@href="/reports/session-report/"]', '//div[@class="ReportFiltersView_filtersContainer__hynQm "]', "Session Report")

@then('go to Call Recording Report')
def navi_call_recordings_report(context):
    navigate_to_page(context, '//a[@href="/reports/call-recordings-report/"]', '//div[@class="ReportFiltersView_filtersContainer__hynQm "]', "Call Recording Report")

@then('go to Recurring Events Report')
def navi_recurring_events(context):
    navigate_to_page(context, '//a[@href="/reports/recurring-events-report/"]', '//div[@class="RecurringEventsReportView_tableContainer__KhdOb RecurringEventsReportView_tableWidthLimit__7Ld24"]', "Recurring Events Report")

@then('go to Posting Report')
def navi_posting_report(context):
    navigate_to_page(context, '//a[@href="/reports/posting-report/"]', '//table[@class="Table_table__YUzYe"]', "Posting Report")

# was removed
'''
@then('go to Mojo Voice Report')
def navi_mojo_voice_report(context):
    navigate_to_page(context, '//a[@href="/reports/mojo-voice-report/"]', '//button[@class="MojoVoiceReportView_showReportButton__2BImd"]', "Mojo Voice Report")
'''

@then('go to Agent Timesheet Report')
def navi_agent_time_sheet_report(context):
    navigate_to_page(context, '//a[@href="/reports/agent-time-sheet-report/"]', '//div[@class="ReportFiltersView_filtersContainer__hynQm "]', "Agent Timesheet")

@then('go to Email Status Report')
def navi_email_status_report(context):
    navigate_to_page(context, '//a[@href="/reports/email-status-report/"]', '//div[@class="ReportFiltersView_filtersContainer__hynQm "]', "Email Status Report")

@then('go to Neighborhood Search Update Report')
def navi_nhs_update(context):
    navigate_to_page(context, '//a[@href="/reports/ns-report/"]', '//button[@class="ReportFiltersView_headerButton__JY+ci "]', "Neighborhood Search Updates")

@then('go to Leadstore page')
def navi_leadstore(context):
    navigate_to_page(context, LEADSTORE_BUTTON, '//div[@class="LeadstoreHomeMainView_servicesContainer__doCYA"]', "Welcome To The Leadstore")

@then('go to AI Tools page')
def navigate_to_ai_tools_page(context):
    context.browser.find_element(By.XPATH, '//img[@alt="AI Tools"]').click()
    context.wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="AIToolsView_AIBlocksGrid__MkOB8"]')))
    # Assert page is loaded
    header = context.browser.find_element(By.XPATH, '//div[@class="AIToolsView_AIToolsHeader__8vwLH"]')
    expected_text = "AI Tools"
    assert header.text in expected_text, f"{expected_text} page Error(header)"



@then('go to Settings page')
def navi_settings(context):
    navigate_to_page(context, SETTINGS_BUTTON,
                     '//div[@class="CallerIDMojoVoiceView_whitelistingLegendContainer__CbfXq"]',
                     "Caller ID / Mojo Caller ID")

@then('go to Settings Callback')
def navi_settings_callback(context):
    navigate_to_page(context, '//button[text()="Optional Messages"]',
                     SETTING_VIEW_CONTAINER,
                     "Callback Prompt")

@then('go to Settings Voicemail')
def navi_settings_voicemail(context):
    navigate_to_page(context, '//button[text()="Voicemail Message Drop"]',
                     SETTING_VIEW_CONTAINER,
                     "Voicemail Message Drop")

@then('go to Dialer Settings')
def navi_settings_dialer(context):
    navigate_to_page(context, '//button[text()="Dialer Settings"]',
                     SETTING_VIEW_CONTAINER,
                     "Dialer Settings")

@then('go to Settings Email')
def navi_settings_email(context):
    navigate_to_page(context, '//button[text()="Email"]',
                     SETTING_VIEW_CONTAINER,
                     "General")

@then('go to Settings Email Templates')
def navi_settings_email_templates(context):
    navigate_to_page(context, '//button[text()="Templates"]',
                     SETTING_VIEW_CONTAINER,
                     "Email Templates")

@then('go to Settings Email Notifications')
def navi_settings_email_notifications(context):
    navigate_to_page(context, '//button[text()="Notifications"]',
                     SETTING_VIEW_CONTAINER,
                     "Notifications")

@then('go to Settings Email Connect To Gmail')
def navi_settings_email_gmail(context):
    navigate_to_page(context, '//button[text()="Connect To Gmail"]',
                     SETTING_VIEW_CONTAINER,
                     "Gmail")

@then('go to Settings Email SMTP')
def navi_settings_email_smtp(context):
    navigate_to_page(context, '//button[text()="SMTP"]',
                     SETTING_VIEW_CONTAINER,
                     "SMTP Settings")

@then('go to Settings Letter')
def navi_settings_letter(context):
    navigate_to_page(context, '//button[text()="Letter"]',
                     SETTING_VIEW_CONTAINER,
                     "Letter Templates")

@then('go to Settings Action Plan')
def navi_settings_ap(context):
    navigate_to_page(context, '//button[text()="Action Plan"]',
                     SETTING_VIEW_CONTAINER,
                     "Action Plans")

@then('go to Settings Calling Scripts')
def navi_settings_calling_scripts(context):
    navigate_to_page(context, '//button[text()="Calling Scripts"]',
                     SETTING_VIEW_CONTAINER,
                     "Calling Scripts")

@then('go to Settings Lead Sheet')
def navi_settings_lead_sheet(context):
    navigate_to_page(context, '//button[text()="Lead Sheet"]',
                     SETTING_VIEW_CONTAINER,
                     "Lead Sheet")

@then('go to Settings Lead Capture Forms')
def navi_settings_lead_capture_forms(context):
    navigate_to_page(context, '//button[text()="Lead Capture Forms"]',
                     SETTING_VIEW_CONTAINER,
                     "Lead Capture Forms")

@then('go to Settings Checklists')
def navi_settings_checklists(context):
    navigate_to_page(context, '//button[text()="Checklists"]',
                     SETTING_VIEW_CONTAINER,
                     "Checklists")

@then('go to Settings Do Not Call')
def navi_settings_dnc(context):
    navigate_to_page(context, '//button[text()="Do Not Call"]',
                     SETTING_VIEW_CONTAINER,
                     "DNC Scrubbing")

@then('go to Settings Do Not Call-DNC export')
def navi_settings_dnc_export(context):
    navigate_to_page(context, '//button[text()="DNC Export"]',
                     SETTING_VIEW_CONTAINER,
                     "DNC Export")

@then('go to Settings Do Not Call-DNC History')
def navi_settings_dnc_history(context):
    navigate_to_page(context, '//button[text()="DNC History"]',
                     SETTING_VIEW_CONTAINER,
                     "DNC History")

@then('go to Settings Misc Fields')
def navi_settings_misc(context):
    navigate_to_page(context, '//button[text()="Misc Fields"]',
                     SETTING_VIEW_CONTAINER,
                     "Misc Fields")

@then('go to Settings Data Management')
def navi_settings_data_management(context):
    navigate_to_page(context, '//button[text()="Data Management"]',
                     SETTING_VIEW_CONTAINER,
                     "Import History")

@then('go to Settings Export History')
def navi_settings_export_history(context):
    navigate_to_page(context, '//button[text()="Export History"]',
                     SETTING_VIEW_CONTAINER,
                     "Export History")

@then('go to Settings Contact Source')
def navi_settings_contact_source(context):
    navigate_to_page(context, '//button[text()="Contact Source"]',
                     SETTING_VIEW_CONTAINER,
                     "Contact Source")

@then('go to Settings Restore Deleted Data')
def navi_settings_restore_data(context):
    navigate_to_page(context, '//button[text()="Restore Deleted Data"]',
                     SETTING_VIEW_CONTAINER,
                     "Restore Deleted Data")

@then('go to Settings Appearance')
def navi_settings_appearance(context):
    navigate_to_page(context, '//button[text()="Appearance"]',
                     SETTING_VIEW_CONTAINER,
                     "Appearance")

@then('go to Integrations-Boomtown')
def go_to_int_boomtowm(context):
    context.browser.find_element(By.XPATH, '//button[text()="Integrations"]').click()
    assert "The Boomtown integration allows" in context.browser.find_element(By.XPATH, INTEGRATION_DESCRIPTION).text

@then('go to Integrations-CINC')
def go_to_int_cinc(context):
    context.browser.find_element(By.XPATH, '//button[text()="CINC (Commissions INC)"]').click()
    assert "The CINC (Commissions INC) integration" in context.browser.find_element(By.XPATH, INTEGRATION_DESCRIPTION).text

@then('go to Integrations-Constant Contact')
def go_to_int_constant_contact(context):
    context.browser.find_element(By.XPATH, '//button[text()="ConstantContact"]').click()
    assert "The Constant Contact integration connects" in context.browser.find_element(By.XPATH, INTEGRATION_DESCRIPTION).text

@then('go to Integrations-Follow up boss')
def go_to_int_fub(context):
    context.browser.find_element(By.XPATH, '//button[text()="ConstantContact"]').click()
    assert "The Constant Contact integration connects" in context.browser.find_element(By.XPATH, INTEGRATION_DESCRIPTION).text

@then('go to Integrations-Google')
def go_to_int_google(context):
    context.browser.find_element(By.XPATH, '//button[text()="Google"]').click()
    assert "To allow sending emails through Mojo" in context.browser.find_element(By.XPATH, '//div[@class="GoogleView_desc__Aop+p" and text()="To allow sending emails through Mojo with your Gmail account please turn on the Use Gmail API."]').text

@then('go to Integrations-Mailchimp')
def go_to_int_mailchimp(context):
    context.browser.find_element(By.XPATH, '//button[text()="MailChimp"]').click()
    assert "The Mail Chimp integration" in context.browser.find_element(By.XPATH, INTEGRATION_DESCRIPTION).text

@then('go to Integrations-Middleware-API Nation')
def go_to_int_api_nation(context):
    context.browser.find_element(By.XPATH, '//button[text()="Middleware"]').click()
    assert "To connect your Mojo account" in context.browser.find_element(By.XPATH, INTEGRATION_DESCRIPTION).text

@then('go to Integrations-Middleware-CRM HQ')
def go_to_int_crm_hq(context):
    context.browser.find_element(By.XPATH, '//button[text()="CRM HQ"]').click()
    assert "CRM HQ helps agents quickly" in context.browser.find_element(By.XPATH, INTEGRATION_DESCRIPTION).text

@then('go to Integrations-Middleware-Zapier')
def go_to_int_zapier(context):
    context.browser.find_element(By.XPATH, '//button[text()="Zapier"]').click()
    assert context.browser.find_element(By.XPATH, '//div[@class="ZapierView_title__0qVO3" and text()="Please Follow The Link Below To Start The Process."]')

@then('go to Integrations-Posting services')
def go_to_int_post_serv(context):
    context.browser.find_element(By.XPATH, '//button[text()="Posting Services"]').click()
    assert "Our posting service allows" in context.browser.find_element(By.XPATH, INTEGRATION_DESCRIPTION).text

@then('go to Integrations-Realgeeks')
def go_to_int_realgeeks(context):
    context.browser.find_element(By.XPATH, '//button[text()="Realgeeks"]').click()
    assert "The Real Geeks integration allows" in context.browser.find_element(By.XPATH, INTEGRATION_DESCRIPTION).text

@then('go to Integrations-Top producer')
def go_to_int_top_producer(context):
    context.browser.find_element(By.XPATH, '//button[text()="Top Producer"]').click()
    assert "Top Producer Set Up" in context.browser.find_element(By.XPATH, INTEGRATION_DESCRIPTION).text

@then('go to Integrations-Wise Agent')
def go_to_int_wise_agent(context):
    context.browser.find_element(By.XPATH, '//button[text()="Wise Agent"]').click()
    assert "The Wise Agent integration allows" in context.browser.find_element(By.XPATH, INTEGRATION_DESCRIPTION).text

@then('go to Integrations-Zillow')
def go_to_int_realgeeks(context):
    context.browser.find_element(By.XPATH, '//button[text()="Zillow"]').click()
    assert "The Zillow Integration connects" in context.browser.find_element(By.XPATH, INTEGRATION_DESCRIPTION).text

