from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest
import selenium

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_items(browser):
    browser.get(link)
    # time.sleep(30)
    button = WDW(browser, 5).until(EC.visibility_of_all_elements_located( (By.CSS_SELECTOR, ".btn-add-to-basket") ))
    assert 1 == len(button), "Button 'Add to basket' is not found or is not unique button."
