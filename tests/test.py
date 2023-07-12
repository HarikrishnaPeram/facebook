from selenium.webdriver.support.select import Select

from tests.signup import Signup
from utilities.BaseClass import BaseClass


class TestFacebook(BaseClass):
    def test_e2e(self):

        signup=Signup(self.driver)