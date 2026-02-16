from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
#import time
'''
#BrowserStack settings
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def before_all(context):
    # BrowserStack credentials
    USERNAME = "gabrieltorosian_kJ8C4S"
    ACCESS_KEY = "9QwmEsToKHjHgpYXion5"

    desired_cap = {
        'os': 'Windows',
        'os_version': '10',
        'browser': 'Chrome',
        'browser_version': 'latest',
        'browserstack.local': 'false',
        'browserstack.selenium_version': '4.0.0',
        'name': 'Behave Regression Tests',  # название сессии
        'build': 'Build 1.0'  # для группировки запусков
    }

    context.browser = webdriver.Remote(
        command_executor=f'https://{USERNAME}:{ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub',
        desired_capabilities=desired_cap
    )

    context.browser.implicitly_wait(10)

def after_all(context):
    context.browser.quit()

# -----------BroeserStuck
'''

use_step_matcher('parse')

EMAIL_FIELD = '//input[@name="email"]'
PASSWORD_FIELD = '//input[@name="password"]'
SUBMIT_BUTTON = '//button[@type="submit"]'
HOME_TITLE = "Join Webinar"
INVALID_LOGIN_ELEMENT = '//div[@class="Form_NonFieldErrors__el6fn"]'
ACCOUNT_MENU_BUTTON = 'div.AccountMenu_hoverContainer__RR9Zd'
LOGOUT_BUTTON = 'div.AccountMenu_link__2RBsi'
EXPIRED_DATA_POPUP_BUTTON = "button.GenericModal_button__1wlPS.GenericModal_cancelButton__3Scfe"

@given('launch Chrome browser')
def launch_browser(context):
    #context.browser = webdriver.Chrome()
    # Создаем объект с опциями для Chrome
    chrome_options = Options()
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    # Инициализируем драйвер с использованием опций
    context.browser = webdriver.Chrome(service=Service(r'C:\Users\gabik\PycharmProjects\Behave_Mojo\chromedriver.exe'), options=chrome_options)

    context.browser.implicitly_wait(15)
    context.wait = WebDriverWait(context.browser, 15)

@when('go on page "{page}"')
def open_login_page(context, page):
    context.browser.get(page)
    context.browser.maximize_window()


@when('fill "{email}" in field "Email"')
def fill_email(context, email):
    try:
        email_input = context.browser.find_element(By.XPATH, EMAIL_FIELD)
        email_input.clear()
        email_input.send_keys(email)
        context.wait.until(EC.visibility_of_element_located((By.XPATH, PASSWORD_FIELD)))

    except NoSuchElementException:
        assert False, "Email input field not found!"

@when('fill "{password}" in field "Password"')
def fill_password(context, password):
    try:
        password_input = context.browser.find_element(By.XPATH, PASSWORD_FIELD)
        password_input.clear()
        password_input.send_keys(password)
    except NoSuchElementException:
        assert False, "Password input field not found!"

@when('click "Submit"')
def click_submit(context):
    context.browser.find_element(By.XPATH, '//button[@type="submit"]').click()

@when('close Expired Data popup if it present')
def close_expired_data_popup(context):
    try:
        context.browser.find_element(By.CSS_SELECTOR, EXPIRED_DATA_POPUP_BUTTON).click()
    except NoSuchElementException:
        pass

@then('wait until page be loaded in showing "Training Webinars" button')
def assert_home_page(context):
    join_webinar_button = context.wait.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="HomeView_textContent__dAjt4" and text()="Join Webinar"]'))
        )
    assert join_webinar_button.text in "Join Webinar", "Something wrong with Home page. Has not Join Webinar element"


@then('logout')
def click_logout(context):
    #context.browser.find_element(By.XPATH, '//div[@class="AccountMenu_hoverContainer__RR9Zd"]/img[@src="/static/media/account-menu-icon.e72ea934.svg"]').click()
    context.browser.find_element(By.XPATH, '//button[@data-tip="Logout"]').click()
    try:
        context.wait.until(EC.presence_of_element_located((By.XPATH, PASSWORD_FIELD)))
    except NoSuchElementException:
        assert False, "Has not logouted after press logout button"


@then('"Invalid login/password" should be displayed')
def assert_invalid_login(context):
    invalid_login_msg = context.wait.until(EC.presence_of_element_located((By.XPATH, INVALID_LOGIN_ELEMENT)))
    assert invalid_login_msg.text in "Invalid login/password", "No 'Invalid login/password' message"

@then('close browser')
def close_browse(context):
    context.browser.quit()




