# features/environment.py

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

def before_all(context):
    """
    Выполняется один раз перед всеми тестами
    Создает подключение к BrowserStack
    """
    # BrowserStack credentials
    USERNAME = "gabrieltorosian_kJ8C4S"
    ACCESS_KEY = "9QwmEsToKHjHgpYXion5"

    # Используем Options вместо desired_capabilities
    options = Options()
    options.set_capability('os', 'Windows')
    options.set_capability('osVersion', '10')
    options.set_capability('browserVersion', 'latest')
    options.set_capability('browserName', 'Chrome')
    options.set_capability('browserstack.local', 'false')
    options.set_capability('name', 'Behave Regression Tests')
    options.set_capability('build', 'Build 1.0')

    context.browser = webdriver.Remote(
        command_executor=f'https://{USERNAME}:{ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub',
        options=options
    )

    context.browser.implicitly_wait(15)
    context.wait = WebDriverWait(context.browser, 15)


def after_all(context):
    """
    Выполняется один раз после всех тестов
    Закрывает браузер
    """
    if hasattr(context, 'browser'):
        context.browser.quit()