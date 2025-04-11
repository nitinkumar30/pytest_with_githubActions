import pytest

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


@pytest.fixture
def setup():
    option = Options()
    option.add_argument('--headless')

    driver = webdriver.Chrome(options=option)
    # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=option)

    yield driver
    driver.quit()
