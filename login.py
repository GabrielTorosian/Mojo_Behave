from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

import time

def test_login_home_page_logout():
    try:
        browser = webdriver.Chrome()
        browser.get("https://lb11.mojosells.com/login/")
        wait = WebDriverWait(browser, 15)
        browser.implicitly_wait(15)

        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.SignInData_Title__2zl3Q")))
        #login
        email_input = browser.find_element(By.XPATH, '//input[@name="email"]')
        email_input.clear()
        email_input.send_keys("g.torosyan@g-sg.net")

        password_input = browser.find_element(By.XPATH, '//input[@name="password"]')
        password_input.clear()
        password_input.send_keys("password1")

        browser.find_element(By.XPATH, '//button[@type="submit"]').click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.HomeView_newsTitle__VgBZL")))

        #Assert Home Page
        join_webinar_button = browser.find_element(By.CSS_SELECTOR, "div.HomeView_textContent__2L3mx")
        assert join_webinar_button.text in "Join Webinar", "something wrong with home page"

        try:
            #wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.GenericModal_title__34niQ")))
            #time.sleep(3)
            browser.find_element(By.CSS_SELECTOR, "button.GenericModal_button__1wlPS.GenericModal_cancelButton__3Scfe").click()
        except NoSuchElementException:
            pass

        #logout
        browser.find_element(By.CSS_SELECTOR, "div.AccountMenu_hoverContainer__RR9Zd").click()
        browser.find_element(By.CSS_SELECTOR, "div.AccountMenu_link__2RBsi").click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.SignInData_Title__2zl3Q")))
        #Assert login page
        login_title = browser.find_element(By.CSS_SELECTOR, "div.SignInData_Title__2zl3Q")
        assert login_title.text in "Sign In to Mojo", "something with login page"

    finally:
        #time.sleep(3)
        browser.quit()

test_login_home_page_logout()



