from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

use_step_matcher('parse')

GLOBAL_SEARCH_FIELD_SELECTOR = "button.DummySidebarSearch_searchInputContainer__uV8MF"


@given('launch Chrome browser with saved session')
def launch_browser_saved_session(context):
    context.browser.get("https://lb11.mojosells.com/")
    context.browser.maximize_window()
    context.wait.until(EC.presence_of_element_located(
        (By.XPATH, '//div[@class="HomeView_textContent__dAjt4" and text()="Join Webinar"]')
    ))


@then('search contact "{contact_name}"')
def search_contact(context, contact_name):
    context.browser.find_element(By.CSS_SELECTOR, GLOBAL_SEARCH_FIELD_SELECTOR).click()
    context.browser.find_element(By.CSS_SELECTOR, "input.SidebarSearch_searchInput__TNhew").clear()
    context.browser.find_element(By.CSS_SELECTOR, "input.SidebarSearch_searchInput__TNhew").send_keys(contact_name)

    context.browser.find_element(By.XPATH, '//button[@class="SidebarSearch_searchSubmitBtn__OLnSD "]').click()
    time.sleep(3)
    context.wait.until(EC.presence_of_element_located(
        (By.XPATH, '//button[text()="View all results in table"]')
    ))
    context.browser.find_element(By.XPATH, '//div[@class="ContactGroup_arrow__Cnq6b"]').click()
    # open contact
    context.browser.find_element(By.XPATH,
        '//div[@class="SearchResults_resultField__EPRqp SearchResults_resultItemFullName__ZgABr"]').click()
    # close search bar
    context.browser.find_element(By.CSS_SELECTOR, "input.SidebarSearch_searchInput__TNhew").clear()
    context.browser.find_element(By.XPATH, '//div[@class="SidebarSearch_closeAnchor__hXp0+"]').click()


@then('cs activities section')
def cs_activities_test(context):
    MARK_AS_CONTACT_BUTTON = '//button[@class="Button_btn__W1TTO Button_btnLightBlue__yjtPk" and text()="Mark As Contact"]'
    CALL_ATTEMPT_POPUP = '//div[@class="GenericModal_mainContainer__Wy5u3"]'
    CONFIRM_BUTTON = "button.GenericModal_button__lmCtH.GenericModal_confirmButton__BAaWj"

    # open Activities tab
    context.browser.find_element(By.XPATH, '//button[@id="activities"]').click()
    context.wait.until(EC.visibility_of_element_located(
        (By.XPATH, '//div[@class="style_header__wTvSF" and text()="Information:"]')
    ))

    # click Mark As Contact
    context.browser.find_element(By.XPATH, MARK_AS_CONTACT_BUTTON).click()
    context.wait.until(EC.visibility_of_element_located((By.XPATH, CALL_ATTEMPT_POPUP)))

    # input note and confirm
    context.browser.find_element(By.XPATH, '//textarea[@id="note"]').send_keys(
        "autotest Mark As Contact button pressed"
    )
    time.sleep(4)
    context.browser.find_element(By.CSS_SELECTOR, CONFIRM_BUTTON).click()
    context.wait.until(EC.invisibility_of_element(
        (By.CSS_SELECTOR, "div.GenericModal_mainContainer__Wy5u3")
    ))

    # add call attempt (+1)
    context.browser.find_element(By.XPATH, '//button[text()="+1"]').click()
    time.sleep(1)

    # remove call attempt (-1)
    context.browser.find_element(By.XPATH, '//button[text()="-1"]').click()
    time.sleep(1)

    # reset call attempts
    context.browser.find_element(By.XPATH, '//button[text()="Reset"]').click()
    time.sleep(1)
    context.wait.until(EC.invisibility_of_element(
        (By.CSS_SELECTOR, "div.GenericModal_mainContainer__Wy5u3")
    ))