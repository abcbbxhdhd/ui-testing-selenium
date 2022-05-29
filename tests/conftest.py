import pytest
from selenium import webdriver

@pytest.fixture()
def chrome_options():
    options = webdriver.ChromeOptions()
    #options.add_argument('--headless')
    options.add_argument('--start-maximized')
    return options

@pytest.fixture()
def driver(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    url = 'https://computer-database.gatling.io/computers'
    driver.get(url)
    yield driver
    driver.quit()

