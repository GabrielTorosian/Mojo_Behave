# features/environment.py
#
# Этот файл управляет жизненным циклом браузера для Behave-тестов.
# Браузер запускается НЕ локально, а в облаке BrowserStack.
#
# КАК ЭТО РАБОТАЕТ:
#   1. before_all()       — открывает удалённый браузер в BrowserStack (один раз на весь прогон)
#   2. before_scenario()  — устанавливает имя текущего теста в BrowserStack Dashboard
#   3. after_scenario()   — сообщает BrowserStack результат теста (passed/failed)
#   4. after_all()        — закрывает браузер
#
# ОТКУДА БЕРУТСЯ CREDENTIALS:
#   - При запуске через GitHub Actions: из GitHub Secrets (настраиваются в Settings → Secrets)
#   - При запуске локально: из переменных окружения или из значений по умолчанию ниже
#
# ПЕРЕМЕННЫЕ ОКРУЖЕНИЯ:
#   BROWSERSTACK_USERNAME  — ваш логин BrowserStack
#   BROWSERSTACK_ACCESS_KEY — ваш ключ доступа BrowserStack

import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait


def before_all(context):
    """
    Выполняется ОДИН РАЗ перед всеми тестами.
    Создаёт подключение к удалённому браузеру в BrowserStack.
    """

    # --- BrowserStack credentials ---
    # Читаем из переменных окружения (GitHub Secrets попадают сюда автоматически).
    # Если переменных нет (локальный запуск) — используем значения по умолчанию.
    USERNAME = os.environ.get("BROWSERSTACK_USERNAME", "gabrieltorosian_kJ8C4S")
    ACCESS_KEY = os.environ.get("BROWSERSTACK_ACCESS_KEY", "9QwmEsToKHjHgpYXion5")

    # --- Настройки браузера для BrowserStack ---
    options = Options()
    options.set_capability('os', 'Windows')               # ОС на стороне BrowserStack
    options.set_capability('osVersion', '10')              # Версия Windows
    options.set_capability('browserVersion', 'latest')     # Последняя версия Chrome
    options.set_capability('browserName', 'Chrome')

    # browserstack.local = false — тестируем публичный сайт, не локальный
    options.set_capability('browserstack.local', 'false')

    # --- Имя билда для BrowserStack Dashboard ---
    # Формат: "Regression 2026-03-02 15:30" — чтобы легко найти нужный прогон
    build_name = os.environ.get(
        "BROWSERSTACK_BUILD_NAME",
        f"Regression {datetime.now().strftime('%Y-%m-%d %H:%M')}"
    )
    options.set_capability('build', build_name)

    # Имя проекта — группирует билды в Dashboard
    options.set_capability('project', 'Mojo Regression')

    # --- Подключение к BrowserStack ---
    # Selenium отправляет команды на удалённый сервер BrowserStack,
    # а тот управляет реальным браузером Chrome в облаке.
    context.browser = webdriver.Remote(
        command_executor=f'https://{USERNAME}:{ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub',
        options=options
    )

    # --- Таймауты ---
    # implicitly_wait — Selenium будет ждать до 15 сек при поиске элемента
    context.browser.implicitly_wait(15)
    # WebDriverWait — для явных ожиданий (wait.until(...))
    context.wait = WebDriverWait(context.browser, 15)


def before_scenario(context, scenario):
    """
    Выполняется ПЕРЕД КАЖДЫМ сценарием (тестом).
    Устанавливает имя теста в BrowserStack Dashboard,
    чтобы в отчёте было видно какой именно тест выполняется.
    """
    context.browser.execute_script(
        'browserstack_executor: {"action": "setSessionName", '
        f'"arguments": {{"name": "{scenario.name}"}}}}'
    )


def after_scenario(context, scenario):
    """
    Выполняется ПОСЛЕ КАЖДОГО сценария (теста).
    Отправляет результат теста (passed/failed) в BrowserStack Dashboard.
    Благодаря этому в Dashboard видно:
      - какие тесты прошли (зелёные)
      - какие упали (красные) + видео момента падения
    """
    if scenario.status == "passed":
        context.browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", '
            '"arguments": {"status": "passed", "reason": "Test passed"}}'
        )
    else:
        # Берём текст ошибки если есть, чтобы показать в BrowserStack Dashboard
        reason = "Test failed"
        if scenario.error_message:
            # Обрезаем длинные сообщения и убираем кавычки (чтобы не сломать JSON)
            reason = str(scenario.error_message)[:255].replace('"', "'")

        context.browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", '
            f'"arguments": {{"status": "failed", "reason": "{reason}"}}}}'
        )


def after_all(context):
    """
    Выполняется ОДИН РАЗ после всех тестов.
    Закрывает удалённый браузер в BrowserStack.
    """
    if hasattr(context, 'browser'):
        context.browser.quit()
