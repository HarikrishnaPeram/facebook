import pytest as pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(executable_path="C:/Users/selenium/work space/chromedriver.exe")
    driver.get("https://www.facebook.com/signup")
    #driver.implicitly_wait(2)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

