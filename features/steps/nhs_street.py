from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import time
use_step_matcher('parse')

@then('go to NHS  search address "{nhs_street_address}"')
def nhs_street(context, nhs_street_address):
    # press NHS button
    context.browser.find_element(By.XPATH,
                                 '//button[text()="Neighborhood Search"]').click()

    # check is map legend present
    #beassert context.browser.find_element(By.XPATH, '//div[@class="NeighbourhoodSearchView_mapOptionsHeader__2v7_0"]'), "map legend is not present"
    # check is filer present
    assert context.browser.find_element(By.XPATH, '//div[text()="Display property pins on map"]'), "filter is not present, side bar error"

    # press Street Search button
    context.browser.find_element(By.XPATH,
                                 '//button[text()="Street Search"]').click()
    context.browser.find_element(By.XPATH,
                                 '//input[@class="NeighbourhoodSearchView_searchBar__BOLUk pac-target-input"]').send_keys(nhs_street_address + Keys.ENTER)
    # wait until Import button will be clickable
    context.wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="LeadstoreFooter_importButton__AGPNQ false" and text()="Import"]')))
    # click Import button
    context.browser.find_element(By.XPATH, '//button[@class="LeadstoreFooter_importButton__AGPNQ false" and text()="Import"]').click()
    # wait alert
    context.wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="confirmAlert_message__JGnt1"]')))
    # press next understand on alert
    context.browser.find_element(By.XPATH, '//button[@class="confirmAlert_actionButton__gdvBM confirmAlert_actionButtonConfirm__ARIc7"]').click()

    # choose list 01_nhs_autotest
    context.browser.find_element(By.XPATH, '//div[@class="SidebarPropertyList_headerTitle__GRn2p" and text()="Calling Lists"]/..').click()
    context.browser.find_element(By.XPATH, '//div[@title="01_nhs_autotest"]/../../button[@class="Checkbox_Checkbox__FWKJN "]').click()
    time.sleep(2)
    #close calling lists
    context.browser.find_element(By.XPATH, '//div[@class="SidebarPropertyList_headerTitle__GRn2p" and text()="Calling Lists"]/..').click()
    context.browser.find_element(By.XPATH, '//div[@class=" Checkbox_title__JDF6b" and text()="Keep New and Old"]/..').click()
    context.browser.find_element(By.XPATH, '//button[@class="LeadstoreImportSection_importButton__N7U2f " and text()="Finish Import"]').click()
    try:
        context.wait.until(EC.visibility_of_element_located((By.XPATH, '//div[text()="Successfully"]')))
    except NoSuchElementException:
        assert False, "Import did not occur!"

    imported_contacts = int(context.browser.find_element(By.XPATH, '//div[@class="ReactModal__Content ReactModal__Content--after-open"]//div[text()="imported"]/span').text)
    if imported_contacts == 0:
        raise AssertionError("0 contact imported!")
    else:
        pass
    context.browser.find_element(By.XPATH, '//button[text()="Back To Map"]').click()





