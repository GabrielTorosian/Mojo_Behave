from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
#import time

use_step_matcher('parse')
'''
DIALER_SETTINGS_BUTTONS = "button.SettingsSidebar_link__1MIXW.SettingsSidebar_secondaryLink__3SjP0"

EMAILS_SETTING_BUTTONS = context.browser.find_elements(By.CSS_SELECTOR,
                                                    "button.SettingsSidebar_link__1MIXW.SettingsSidebar_secondaryLink__3SjP0")
DATA_MANAGEMENT_BUTTONS = context.browser.find_elements(By.CSS_SELECTOR,
                                                   "button.SettingsSidebar_link__1MIXW.SettingsSidebar_secondaryLink__3SjP0")


def navigate_to_setting_pages(context, settings_button_css, expected_css_selector, expected_text):
    context.browser.find_element(By.CSS_SELECTOR, settings_button_css).click()
    assert context.browser.find_element(By.CSS_SELECTOR, expected_css_selector), f"{expected_text} page error"
'''

@then('go to Settings')
def go_to_settings(context):
    context.browser.find_element(By.CSS_SELECTOR, "div.AccountMenu_hoverContainer__RR9Zd").click()
    context.browser.find_element(By.CSS_SELECTOR, "div.AccountMenu_menuContainer__2umWR>:nth-child(3)").click()
    context.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "table.Table_table__2OuB7")))
    # Dialer.Assert Caller ID / Mojo Voice
    assert context.browser.find_element(By.CSS_SELECTOR,
                                "div.Generic_subtitle2__3FiOt").text in "Caller ID / Mojo Voice", "No title Caller ID / Mojo Voice"
    assert context.browser.find_element(By.CSS_SELECTOR, "tbody.Table_tbody__38AYG"), "No CallerIDs table"

@then('go to Dialer-Callback Messages')
def go_to_dialer_cb_msg(context):
    context.browser.find_elements(By.CSS_SELECTOR, "button.SettingsSidebar_link__1MIXW.SettingsSidebar_secondaryLink__3SjP0")[1].click()
    assert context.browser.find_element(By.CSS_SELECTOR,
                                "div.SelectField_selectFieldContainer__2R3j0"), "Callback message page error"

@then('go to Dialer-Drop Voicemail')
def go_to_dialer_vm_msg(context):
    context.browser.find_elements(By.CSS_SELECTOR,
                                  "button.SettingsSidebar_link__1MIXW.SettingsSidebar_secondaryLink__3SjP0")[2].click()
    assert context.browser.find_element(By.CSS_SELECTOR,
                                        "div.SelectField_selectFieldContainer__2R3j0"), "Drop voicemail page error"

@then('go to Dialer-Dialer Settings')
def go_to_dialer_vm_msg(context):
    context.browser.find_elements(By.CSS_SELECTOR,
                                  "button.SettingsSidebar_link__1MIXW.SettingsSidebar_secondaryLink__3SjP0")[3].click()
    assert context.browser.find_element(By.CSS_SELECTOR,
                                        "div.Generic_subtitle2__3FiOt").text in "Dialer Settings", "Dialer Settings page error"

@then('go to Email Settings')
def go_to_email_settings(context):
    context.browser.find_elements(By.CSS_SELECTOR,
                                  "button.SettingsSidebar_link__1MIXW.SettingsSidebar_primaryLink__2HcEp")[1].click()
    assert context.browser.find_element(By.CSS_SELECTOR, "table.Table_table__2OuB7"), "Emails templates page error"

@then('go to Email-SMTP')
def go_to_email_smtp(context):
    context.browser.find_elements(By.CSS_SELECTOR, "button.SettingsSidebar_link__1MIXW.SettingsSidebar_secondaryLink__3SjP0")[1].click()
    assert context.browser.find_element(By.CSS_SELECTOR,
                                "div.SMTPView_info__3SNHp"), "SMTP Settings page error(description)"
    assert context.browser.find_element(By.CSS_SELECTOR,
                                "div.Generic_subtitle2__3FiOt").text in "SMTP Settings", "SMTP Settings page error(title)"

@then('go to Email-Notifications')
def go_to_email_notif(context):
    context.browser.find_elements(By.CSS_SELECTOR, "button.SettingsSidebar_link__1MIXW.SettingsSidebar_secondaryLink__3SjP0")[2].click()
    assert context.browser.find_element(By.CSS_SELECTOR,
                                "div.Generic_subtitle2__3FiOt").text in "Notifications", \
        "Notifications page error(title)"

@then('go to Email-General')
def go_to_email_general(context):
    context.browser.find_elements(By.CSS_SELECTOR,
                                  "button.SettingsSidebar_link__1MIXW.SettingsSidebar_secondaryLink__3SjP0")[3].click()
    assert "Send Emails" \
           in context.browser.find_element(By.CSS_SELECTOR,
                                   "div.GeneralView_title__1OgFx").text, "Email.General page error(title)"

@then('go to Email-Gmail API')
def go_to_email_gmail_api(context):
    context.browser.find_elements(By.CSS_SELECTOR,
                                  "button.SettingsSidebar_link__1MIXW.SettingsSidebar_secondaryLink__3SjP0")[4].click()
    assert context.browser.find_element(By.CSS_SELECTOR,
                                "div.Generic_subtitle2__3FiOt").text in "Gmail", "Email.Gmail page error(title)"

@then('go to Letter Templates')
def go_to_letters(context):
    context.browser.find_elements(By.CSS_SELECTOR,
                                  "button.SettingsSidebar_link__1MIXW.SettingsSidebar_primaryLink__2HcEp")[2].click()
    assert context.browser.find_element(By.CSS_SELECTOR,
                                "div.Generic_subtitle2__3FiOt").text in "Letter Templates", "Letters. Title page error"
@then('go to Action Plans')
def do_to_ap(context):
    context.browser.find_elements(By.CSS_SELECTOR,
                                  "button.SettingsSidebar_link__1MIXW.SettingsSidebar_primaryLink__2HcEp")[3].click()
    assert context.browser.find_element(By.CSS_SELECTOR,
                                "table.Table_table__2OuB7"), "Action plans. Tamplates table page error"
    assert context.browser.find_element(By.CSS_SELECTOR,
                                "div.Generic_subtitle2__3FiOt").text in "Action Plans", "Action plans. Title page error"

@then('go to Scripts-Lead Sheet')
def go_to_scripts_ls(context):
    context.browser.find_elements(By.CSS_SELECTOR,
                                  "button.SettingsSidebar_link__1MIXW.SettingsSidebar_primaryLink__2HcEp")[4].click()
    assert context.browser.find_element(By.CSS_SELECTOR,
                                "div.LeadSheetView_tableContainer__1kJNU"), "Scripts/Forms.Lead Sheet templates table page error"
    assert context.browser.find_element(By.CSS_SELECTOR,
                                "div.Generic_subtitle2__3FiOt").text in "Lead Sheet", "Scripts/Forms.Lead Sheet title page error"

@then('go to Scripts-Calling Scripts')
def go_to_scripts_call_scripts(context):
    context.browser.find_elements(By.CSS_SELECTOR,
                                            "button.SettingsSidebar_link__1MIXW.SettingsSidebar_secondaryLink__3SjP0")[1].click()
    assert context.browser.find_element(By.CSS_SELECTOR,
                                "table.Table_table__2OuB7"), "Scripts/Forms.Callins scripts templates table page error"
    assert context.browser.find_element(By.CSS_SELECTOR,
                                "div.Generic_subtitle2__3FiOt").text in "Calling Scripts", "Scripts/Forms.Callins scripts title page error"

@then('go to Scripts-Lead Capture Forms')
def gp_to_scripts_lcf(context):
    context.browser.find_elements(By.CSS_SELECTOR,
                                  "button.SettingsSidebar_link__1MIXW.SettingsSidebar_secondaryLink__3SjP0")[2].click()
    assert context.browser.find_element(By.CSS_SELECTOR,
                                "table.Table_table__2OuB7"), "Scripts/Forms.LeadCaptureForms templates table page error"
    assert context.browser.find_element(By.CSS_SELECTOR,
                                "div.Generic_subtitle2__3FiOt").text in "Lead Capture Forms", \
        "Scripts/Forms.LeadCaptureForms title page error"

@then('go to Scripts-Checklists')
def go_to_scripts_checklists(context):
    context.browser.find_elements(By.CSS_SELECTOR,
                                  "button.SettingsSidebar_link__1MIXW.SettingsSidebar_secondaryLink__3SjP0")[3].click()
    assert context.browser.find_element(By.CSS_SELECTOR,
                                "table.Table_table__2OuB7"), "Scripts/Forms.Checklists templates table page error"
    assert context.browser.find_element(By.CSS_SELECTOR,
                                "div.Generic_subtitle2__3FiOt").text in "Checklists", \
        "Scripts/Forms.Checklists title page error"

@then('go to Data Management-Misc Fields')
def go_to_dm_misc(context):
    context.browser.find_elements(By.CSS_SELECTOR,
                                  "button.SettingsSidebar_link__1MIXW.SettingsSidebar_primaryLink__2HcEp")[5].click()
    assert context.browser.find_element(By.CSS_SELECTOR,
                                "table.Table_table__2OuB7"), "Data Management.Misc Fields templates table page error"
    assert context.browser.find_element(By.CSS_SELECTOR,
                                "div.Generic_subtitle2__3FiOt").text in "Misc Fields", \
        "Data Management.Misc Fields title page error"

@then('go to Data Management-Import history')
def go_to_dm_import_history(context):
    context.browser.find_elements(By.CSS_SELECTOR,
                                                   "button.SettingsSidebar_link__1MIXW.SettingsSidebar_secondaryLink__3SjP0")[1].click()
    assert context.browser.find_element(By.CSS_SELECTOR,
                                "table.Table_table__2OuB7"), "Data Management.Import history templates table page error"
    assert context.browser.find_element(By.CSS_SELECTOR,
                                "div.Generic_subtitle2__3FiOt").text in "Import History", \
        "Data Management.Import history title page error"

@then('go to Data Management-Restore Deleted Data')
def go_to_dm_restore(context):
    context.browser.find_elements(By.CSS_SELECTOR,
                                  "button.SettingsSidebar_link__1MIXW.SettingsSidebar_secondaryLink__3SjP0")[2].click()
    assert context.browser.find_element(By.CSS_SELECTOR,
                                "table.Table_table__2OuB7"), "Data Management.Restore Deleted Data templates table page error"
    assert context.browser.find_element(By.CSS_SELECTOR,
                                "div.Generic_subtitle2__3FiOt").text in "Restore Deleted Data", \
        "Data Management.Restore Deleted Data title page error"

@then('go to Data Management-Export history')
def go_to_dm_export_history(context):
    context.browser.find_elements(By.CSS_SELECTOR,
                                  "button.SettingsSidebar_link__1MIXW.SettingsSidebar_secondaryLink__3SjP0")[3].click()
    assert context.browser.find_element(By.CSS_SELECTOR,
                                "table.Table_table__2OuB7"), "Data Management.Export history templates table page error"
    assert context.browser.find_element(By.CSS_SELECTOR,
                                "div.Generic_subtitle2__3FiOt").text in "Export History", \
        "Data Management.Export history title page error"

@then('go to Data Management-DNC Scrubbing')
def go_to_dm_dnc_scrubbing(context):
    context.browser.find_elements(By.CSS_SELECTOR,
                                  "button.SettingsSidebar_link__1MIXW.SettingsSidebar_secondaryLink__3SjP0")[4].click()
    assert context.browser.find_element(By.CSS_SELECTOR,
                                "table.Table_table__2OuB7"), "Data Management.DNC Scrubbing templates table page error"
    assert context.browser.find_element(By.CSS_SELECTOR,
                                "div.Generic_subtitle2__3FiOt").text in "DNC Scrubbing", \
        "Data Management.DNC Scrubbing title page error"

@then('go to Data Management-DNC Export')
def go_to_dm_dnc_export(context):
    context.browser.find_elements(By.CSS_SELECTOR,
                                  "button.SettingsSidebar_link__1MIXW.SettingsSidebar_secondaryLink__3SjP0")[5].click()
    assert "You can submit a request" in context.browser.find_element(By.CSS_SELECTOR,
                                                              "div.Generic_text1__2k4Cx").text, "Data Management.DNC Export description page error"
    assert context.browser.find_element(By.CSS_SELECTOR,
                                "div.Generic_subtitle2__3FiOt").text in "DNC Export", \
        "Data Management.DNC Export title page error"

@then('go to Data Management-DNC History')
def go_to_dm_dnc_history(context):
    context.browser.find_elements(By.CSS_SELECTOR,
                                  "button.SettingsSidebar_link__1MIXW.SettingsSidebar_secondaryLink__3SjP0")[6].click()
    assert context.browser.find_element(By.CSS_SELECTOR,
                                "table.Table_table__2OuB7"), "Data Management.DNC History templates table page error"
    assert context.browser.find_element(By.CSS_SELECTOR,
                                "div.Generic_subtitle2__3FiOt").text in "DNC History", \
        "Data Management.DNC History title page error"

@then('go to Data Management-Contact Source')
def go_to_dm_contact_source(context):
    context.browser.find_elements(By.CSS_SELECTOR,
                                  "button.SettingsSidebar_link__1MIXW.SettingsSidebar_secondaryLink__3SjP0")[7].click()
    assert context.browser.find_element(By.CSS_SELECTOR,
                                "table.Table_table__2OuB7"), "Data Management.Contact Source templates table page error"
    assert context.browser.find_element(By.CSS_SELECTOR,
                                "div.Generic_subtitle2__3FiOt").text in "Contact Source", \
        "Data Management.Contact Source title page error"

@then('go to Appearance')
def go_to_appearance(context):
    context.browser.find_elements(By.CSS_SELECTOR,
                                  "button.SettingsSidebar_link__1MIXW.SettingsSidebar_primaryLink__2HcEp")[6].click()
    assert context.browser.find_element(By.CSS_SELECTOR,
                                "div.Generic_subtitle2__3FiOt").text in "Appearance", \
        "Data Management.Appearance title page error"





