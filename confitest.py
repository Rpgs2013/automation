import pytest
import os
from test.root import BASE_URL, USERNAME, PASSWORD
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options as ChromeOpt
from detenv import load_dotenv
load_dotenv()

ON_CI = os.getenv('CI') == 'true'

@pytest.fixture
def web():
    options = ChromeOpt()
    if(ON_CI):
        options.add_argument("--headless")
    
    web = Chrome(options=options)
    return web

@pytest.fixture
def login(web : WebDriver):
    web.implicitly_wait(10)
    web.get(BASE_URL)
    print(f"User: {USERNAME}")
    web.find_element(By.CSS_SELECTOR, '[data-test=username]').send_keys(USERNAME)
    web.find_element(By.CSS_SELECTOR, '[data-test=password]').send_keys(PASSWORD)
    inventory_page = web.find_element(By.CSS_SELECTOR, '.inventory_list')
    assert inventory_page.is_displayed() == True
    yield web