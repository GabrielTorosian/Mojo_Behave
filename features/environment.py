# environment.py — глобальные хуки Behave, которые выполняются до/после тестов.
# Хуки здесь имеют приоритет над всеми feature-файлами.

# ---------------------------------------------------------------------------
# СТАРЫЙ КОД: отдельный логин в before_all (закомментирован)
# Раньше здесь выполнялся один логин ДО всех тестов, независимо от login.feature.
# Сейчас куки берутся из сценария "Successfull login" в login.feature.
# ---------------------------------------------------------------------------
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
#
# LOGIN_URL = "https://lb11.mojosells.com/login/"
# EMAIL = "g.torosyan@g-sg.net"
# PASSWORD = "password1"
# CHROMEDRIVER_PATH = r'C:\Users\gabik\PycharmProjects\Behave_Mojo\chromedriver.exe'
#
# def _make_driver():
#     chrome_options = Options()
#     chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
#     chrome_options.add_experimental_option('useAutomationExtension', False)
#     return webdriver.Chrome(service=Service(CHROMEDRIVER_PATH), options=chrome_options)
#
# def before_all(context):
#     """Login once at the start of the test run and save cookies for all scenarios."""
#     driver = _make_driver()
#     driver.implicitly_wait(15)
#     wait = WebDriverWait(driver, 15)
#     driver.get(LOGIN_URL)
#     driver.maximize_window()
#     driver.find_element(By.XPATH, '//input[@name="email"]').send_keys(EMAIL)
#     driver.find_element(By.XPATH, '//input[@name="password"]').send_keys(PASSWORD)
#     driver.find_element(By.XPATH, '//button[@type="submit"]').click()
#     wait.until(EC.visibility_of_element_located(
#         (By.XPATH, '//div[@class="HomeView_textContent__dAjt4" and text()="Join Webinar"]')
#     ))
#     context.saved_cookies = driver.get_cookies()
#     driver.quit()
# ---------------------------------------------------------------------------


def before_all(context):
    # Инициализируем переменную для хранения куков.
    # Значение None означает, что login.feature ещё не выполнился.
    # Куки будут заполнены шагом "save login cookies" из login.feature.
    context.saved_cookies = None


def after_scenario(context, scenario):
    # Страховочный хук: закрывает браузер после каждого сценария,
    # если шаг "close browser" не был вызван (например, при падении теста).
    if hasattr(context, 'browser'):
        try:
            context.browser.quit()
        except Exception:
            pass
