from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
import os


def _dump_activities_html(context):
    """
    Saves the HTML of the Activities section to debug_activities.html
    so we can inspect the real class names used by the app.
    """
    try:
        html = context.browser.execute_script("""
            // Try to find the activities tab content by known anchor: "Information:" header
            var header = document.evaluate(
                '//*[contains(@class,"style_header") and contains(text(),"Information")]',
                document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null
            ).singleNodeValue;

            // Walk up to the nearest section container (up to 5 levels)
            var node = header;
            for (var i = 0; i < 5 && node; i++) {
                node = node.parentElement;
                if (node && node.innerHTML.length > 500) break;
            }
            return node ? node.outerHTML : document.body.innerHTML.substring(0, 30000);
        """)
        out_path = os.path.join(os.path.dirname(__file__), '..', '..', 'debug_activities.html')
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(html or '')
        print(f"\n[DEBUG] Activities HTML saved to: {os.path.abspath(out_path)}")
    except Exception as e:
        print(f"\n[DEBUG] Could not dump HTML: {e}")

use_step_matcher('parse')

# ── Activities tab ────────────────────────────────────────────────────────────
ACTIVITIES_TAB     = '//button[@id="activities"]'
INFORMATION_HEADER = '//div[@class="style_header__wTvSF" and text()="Information:"]'

# ── Mark As Contact modal ─────────────────────────────────────────────────────
MARK_AS_CONTACT_BTN   = '//button[@class="Button_btn__W1TTO Button_btnLightBlue__yjtPk" and text()="Mark As Contact"]'
MARK_AS_CONTACT_MODAL = 'div.GenericModal_mainContainer__Wy5u3'
NOTE_TEXTAREA         = '//textarea[@id="note"]'
MODAL_CONFIRM_BTN     = 'button.GenericModal_button__lmCtH.GenericModal_confirmButton__BAaWj'

# ── Call Attempts section ─────────────────────────────────────────────────────
# Selectors confirmed from debug_activities.html DOM dump:
#   Last Dial Date value lives in the <div class="ContactInformation_value__3GMzy">
#   that directly follows the matching label div.
LAST_DIAL_DATE_VALUE  = ('//div[@class="ContactInformation_label__dY8+b" '
                         'and text()="Last Dial Date:"]/following-sibling::div[1]')
#   Attempts counter is a <span class="ContactInformation_attempts__yHoCj">
ATTEMPTS_VALUE        = '//span[@class="ContactInformation_attempts__yHoCj"]'
#   "+"/"-" buttons have NO text — they contain <img> with descriptive src names
PLUS_BTN              = '//img[contains(@src,"increase-icon")]/parent::button'
MINUS_BTN             = '//img[contains(@src,"decrease-icon")]/parent::button'
RESET_BTN             = '//button[normalize-space(text())="Reset"]'

# Confirmation alert that may appear after pressing Reset (same pattern as other steps)
CONFIRM_ALERT_BTN     = 'button.confirmAlert_actionButton__gdvBM.confirmAlert_actionButtonConfirm__ARIc7'
CONFIRM_ALERT_BOX     = 'div.confirmAlert_confirmAlert__Dg54z'

#CS close button
CS_CLOSE_BTN = '//button[@class="ContactHeader_close__7YIL9"]'
CS_SELECTOR = '//div[@class="ContactView_contactContainer__g9F8M"]'


# ── Step: open Activities tab ─────────────────────────────────────────────────
@then('open CS Activities tab')
def open_activities_tab(context):
    """Click the Activities tab unconditionally so it is guaranteed to be open."""
    context.browser.find_element(By.XPATH, ACTIVITIES_TAB).click()
    context.wait.until(
        EC.visibility_of_element_located((By.XPATH, INFORMATION_HEADER))
    )
    # Wait for the Last Dial Date row to appear — confirms async data has fully loaded.
    # We do NOT wait for Mark As Contact to be clickable here because it may already
    # be disabled (e.g. the contact was previously marked and not yet reset).
    context.wait.until(
        EC.visibility_of_element_located((By.XPATH, LAST_DIAL_DATE_VALUE))
    )


# ── Step: Mark As Contact + verify Last Dial Date changed ─────────────────────
@then('click Mark as Contact and verify Last Dial Date changed')
def mark_as_contact_and_verify(context):
    # Wait until the button is enabled (not disabled) and not intercepted
    mark_btn = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, MARK_AS_CONTACT_BTN))
    )
    # Scroll the button to the center of the viewport to avoid
    # interception by the ContactInformation_value div
    context.browser.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});", mark_btn
    )
    time.sleep(0.5)
    mark_btn.click()
    context.wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, MARK_AS_CONTACT_MODAL))
    )

    # Fill in a note and confirm
    context.browser.find_element(By.XPATH, NOTE_TEXTAREA).send_keys(
        "autotest - Mark As Contact button pressed"
    )
    time.sleep(2)

    context.browser.find_element(By.CSS_SELECTOR, MODAL_CONFIRM_BTN).click()
    context.wait.until(
        EC.invisibility_of_element_located((By.CSS_SELECTOR, MARK_AS_CONTACT_MODAL))
    )
    time.sleep(2)

    # Dump DOM so we can find the real class names on first run
    _dump_activities_html(context)

    # Verify Last Dial Date is no longer "N/A"
    last_dial_date = context.browser.find_element(By.XPATH, LAST_DIAL_DATE_VALUE).text
    assert last_dial_date != "N/A", (
        f"Last Dial Date should have changed after Mark As Contact, "
        f"but it is still: '{last_dial_date}'"
    )


# ── Step: click "+" → Attempts == 2 ──────────────────────────────────────────
@then('click plus Attempts and verify Attempts is 2')
def click_plus_attempts(context):
    context.browser.find_element(By.XPATH, PLUS_BTN).click()
    time.sleep(1)

    context.browser.find_element(By.XPATH, NOTE_TEXTAREA).send_keys(
        "autotest - + attempts button pressed"
    )
    time.sleep(2)

    context.browser.find_element(By.CSS_SELECTOR, MODAL_CONFIRM_BTN).click()
    context.wait.until(
        EC.invisibility_of_element_located((By.CSS_SELECTOR, MARK_AS_CONTACT_MODAL))
    )
    time.sleep(2)

    attempts = context.browser.find_element(By.XPATH, ATTEMPTS_VALUE).text
    assert attempts == "2", (
        f"Expected Attempts = 2 after pressing '+', but got: '{attempts}'"
    )


# ── Step: click "−" → Attempts == 1 ──────────────────────────────────────────
@then('click minus Attempts and verify Attempts is 1')
def click_minus_attempts(context):
    context.browser.find_element(By.XPATH, MINUS_BTN).click()
    time.sleep(1)

    attempts = context.browser.find_element(By.XPATH, ATTEMPTS_VALUE).text
    assert attempts == "1", (
        f"Expected Attempts = 1 after pressing '-', but got: '{attempts}'"
    )


# ── Step: click Reset → Last Dial Date == N/A ────────────────────────────────
@then('click Reset and verify Last Dial Date is N/A')
def click_reset_and_verify(context):
    context.browser.find_element(By.XPATH, RESET_BTN).click()
    context.browser.find_element(By.XPATH, '//button[@class="Button_btn__W1TTO Button_btnSalmon__FDIZ+" and text()="Reset"]').click()

    # Handle optional confirmation alert (same pattern used in other step files)
    try:
        context.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, CONFIRM_ALERT_BTN))
        )
        context.browser.find_element(By.CSS_SELECTOR, CONFIRM_ALERT_BTN).click()
        context.wait.until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, CONFIRM_ALERT_BOX))
        )
    except TimeoutException:
        pass  # No confirmation dialog – Reset applied directly

    time.sleep(2)

    last_dial_date = context.browser.find_element(By.XPATH, LAST_DIAL_DATE_VALUE).text
    assert last_dial_date == "N/A", (
        f"Expected Last Dial Date = 'N/A' after Reset, but got: '{last_dial_date}'"
    )

@then('close CS')
def close_cs(context):
    context.browser.find_element(By.XPATH, CS_CLOSE_BTN).click()
    context.wait.until(
        EC.invisibility_of_element_located((By.XPATH, CS_SELECTOR))
    )


