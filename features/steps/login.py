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


@given('launch Chrome browser with saved session')
def launch_browser_with_session(context):
    # Новый шаг: запускает браузер и использует куки из login.feature вместо логина.
    # Используется в Background всех feature-файлов, кроме login.feature.
    chrome_options = Options()
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    context.browser = webdriver.Chrome(
        service=Service(r'C:\Users\gabik\PycharmProjects\Behave_Mojo\chromedriver.exe'),
        options=chrome_options
    )
    context.browser.implicitly_wait(15)
    context.wait = WebDriverWait(context.browser, 15)

    # Сначала открываем любую страницу домена — без этого браузер не примет куки.
    # Куки можно добавить только для домена, который уже открыт в браузере.
    context.browser.get("https://lb11.mojosells.com/login/")
    context.browser.maximize_window()

    if context.saved_cookies:
        # ПУТЬ 1: куки есть (login.feature уже отработал) — инжектируем их в браузер.
        # Браузер передаст эти куки серверу при следующем запросе,
        # и сервер посчитает нас залогиненными без ввода пароля.
        for cookie in context.saved_cookies:
            # Убираем поле sameSite — оно иногда вызывает ошибку при add_cookie()
            cookie.pop('sameSite', None)
            try:
                context.browser.add_cookie(cookie)
            except Exception:
                pass
        # Переходим на главную страницу — куки уже установлены, логин произойдёт автоматически
        context.browser.get("https://lb11.mojosells.com/")
    else:
        # ПУТЬ 2: куки ещё не сохранены (login.feature не запускался или запускается отдельно).
        # Делаем обычный логин как запасной вариант.
        context.browser.find_element(By.XPATH, EMAIL_FIELD).send_keys("g.torosyan@g-sg.net")
        context.browser.find_element(By.XPATH, PASSWORD_FIELD).send_keys("password1")
        context.browser.find_element(By.XPATH, SUBMIT_BUTTON).click()
        context.wait.until(EC.visibility_of_element_located(
            (By.XPATH, '//div[@class="HomeView_textContent__dAjt4" and text()="Join Webinar"]')
        ))

    # Закрываем popup "Expired Data" если он появился (не всегда присутствует)
    try:
        context.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, EXPIRED_DATA_POPUP_BUTTON)
        )).click()
    except Exception:
        pass


@then('save login cookies')
def save_login_cookies(context):
    # Новый шаг: сохраняет куки текущей сессии в context.saved_cookies.
    # Вызывается в login.feature ПОСЛЕ успешного логина, НО ДО logout.
    # После logout сессия на сервере инвалидируется и куки станут недействительными.
    # context — общий объект Behave, доступный во всех feature-файлах в рамках одного запуска.
    context.saved_cookies = context.browser.get_cookies()


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




