from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

import time
use_step_matcher('parse')

group_name="autotest_group"

@then('go to group "{group_name}"')
def go_to_group(context, group_name):
    # open the groups search dropdown
    context.wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//button[@id="groups"]//img[@src="/static/media/menu-search-icon.8a26c4e62c8ed637da9cee5ff1be5a37.svg"]/..'))).click()
    # type the group name in the search field
    context.wait.until(EC.visibility_of_element_located(
        (By.XPATH, '//input[@class="SelectField_searchBarSide__lBnji"]'))).send_keys(group_name)
    # click on the group in search results to navigate to it
    context.wait.until(EC.element_to_be_clickable(
        (By.XPATH, f'//div[@class="SelectFieldElement_name__RO3oK" and text()="{group_name}"]'))).click()
    # wait for contacts table to load after selecting the group
    context.wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "table.Table_tableFixed__qZs5B")))

def click_with_retry(context, locator, retries=3):
    """
    Find element and click it, retrying if the DOM re-renders between find and click.
    After selecting a group, the contacts table re-renders and elements go stale.
    This helper retries the entire find+click sequence to handle that.
    """
    for attempt in range(retries):
        try:
            context.wait.until(EC.element_to_be_clickable(locator)).click()
            return
        except StaleElementReferenceException:
            if attempt == retries - 1:
                raise

@then('select all export contacts')
def select_all_export_contacts(context):
    # click "Select All" checkbox area to reveal the "Select All" option.
    # Table may still be re-rendering after group selection — use retry to handle stale elements.
    click_with_retry(context,
        (By.XPATH, '//div[@class="ContactTable_selectAllCheckboxContainer__FzQur"]'))
    # click "Select All" text to select all contacts in the group
    context.wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//div[@class=" Checkbox_title__JDF6b" and text()="Select All"]'))).click()
    # click the "Export" button in the bottom action bar.
    # Use text-based selector instead of fragile index-based access to a long class name.
    context.wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//span[@class="IconButton_childrenContainer__pUIKl" and text()="Export"]/..'))).click()
    # A modal with a loading overlay appears while export options load.
    # Wait for the overlay to disappear before clicking the "Export" confirm button.
    context.wait.until(EC.invisibility_of_element_located(
        (By.CSS_SELECTOR, "div.GenericModal_loadingOverlay__veWvC")))
    # click "Export" in the confirmation modal
    context.wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//button[text()="Export"]'))).click()
    # wait for the success toast notification — use longer timeout (60s) since export may take time
    export_wait = WebDriverWait(context.browser, 60)
    assert export_wait.until(EC.presence_of_element_located(
        (By.XPATH, '//div[@id="heavyTaskToastId"]//div[text()="File Successfully Generated"]')
    )), "Export file was not generated!"
