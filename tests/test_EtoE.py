from selenium.webdriver.support.select import Select

from tests.signup import Signup
from utilities.BaseClass import BaseClass


class TestFacebook(BaseClass):
    def test_e2e(self):

        signup=Signup(self.driver)
        signup.getfirstname().send_keys("Hari")
        signup.getsurname().send_keys("peram")
        signup.getmobileoremail().send_keys("9876543211")
        signup.getnewpassword().send_keys("9876543211")
        ddropdown = Select(signup.getday())
        ddropdown.select_by_index(2)
        mdropdown = Select(signup.getmonth())
        mdropdown.select_by_index(2)
        ydropdown = Select(signup.getyear())
        ydropdown.select_by_index(2)
        signup.getgender().click()
        signup.getsignup().click()
