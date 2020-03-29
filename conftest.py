import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en", help="Choose your language.")
    parser.addoption("--browser", action="store", default="chrome", help="Choose your browser: chrome of firefox")

# Default values:
# Language: English
# Browser:  Chrome
@pytest.fixture(scope="function")
def browser(request):
    browser_language = request.config.getoption("language")
    browser_name = request.config.getoption("browser")
    if browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", browser_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        opt = Options()
        opt.add_experimental_option("prefs", {'intl.accept_languages': browser_language})
        browser = webdriver.Chrome(options=opt)
    yield browser
    browser.quit()
