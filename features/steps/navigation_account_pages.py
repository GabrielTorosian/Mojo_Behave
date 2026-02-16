from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
#import time

use_step_matcher('parse')

def navi_account_pages(context, navi_button_xpath, expected_css_selector, assert_text_css_selector, expected_text):
    context.browser.find_element(By.XPATH, navi_button_xpath).click()
    context.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, expected_css_selector)))
    #Assert page is loaded
    account_page_title = context.browser.find_element(By.XPATH, '//div[@class="Generic_subtitle2__FY6pW"]').text
    text_account_page_css = context.browser.find_element(By.CSS_SELECTOR, assert_text_css_selector)
    assert expected_text in text_account_page_css.text, f"{account_page_title} account page Error(no title)"


@then('go to Account-Profile')
def go_to_acc_profile(context):
    #context.browser.find_element(By.CSS_SELECTOR, "div.AccountMenu_hoverContainer__RR9Zd").click()
    context.browser.find_element(By.XPATH,
                         '//img[@alt="Account"]').click()
    contact_info_title = context.browser.find_element(By.CSS_SELECTOR, "div.Generic_subtitle2__FY6pW")
    assert contact_info_title.text in "Contact Information", "Account-Profile page Error(title)"

@then('go to Account-Manage Payments')
def navi_acc_billing(context):
    navi_account_pages(context, '//a[@href="/account/billing/"]', "div.Generic_subtitle__FGJ6f", "div.Generic_subtitle2__FY6pW", "Manage Payments")

@then('go to Account-Agents')
def navi_acc_agents(context):
    navi_account_pages(context, '//a[@href="/account/agents/"]', "a.AccountAgentsView_userTypesLink__XeRDe", "div.AccountAgentsView_notice__pzxj9", "To delete an agent from")

@then('go to Account-Subscriptions')
def navi_subscriptions(context):
    navi_account_pages(context, '//a[@href="/account/subscriptions/"]', "div.SubscriptionsView_subscriptionInfo__FNYaa", "div.Generic_subtitle2__FY6pW", "Dialer Subscriptions")

@then('go to Account-Refer-A-Friend Invites')
def navi_account_refer_friends(context):
    navi_account_pages(context, '//a[@href="/account/refer-friend/"]', "table.AccountReferFriendView_table__U1d-u", "div.Generic_text1__aH3dk", "Referral invites stay active")