import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC    
from selenium.webdriver.support.ui import WebDriverWait

from PageObjects2.c_confirmPage import ConfirmPage
import sys

sys.path.append("../")

from BaseFolder2.baseFolder import Test_BaseFolder2

class CheckOutPage(Test_BaseFolder2):

    def __init__(self,driver,count=None):
        self.driver=driver
        self.count=count

    mobile_card= (By.XPATH,"//h4[@class='card-title']/a")
    checkOut_btn= (By.CSS_SELECTOR,".nav-link.btn.btn-primary")
    confirm_checkout= (By.CSS_SELECTOR,".btn.btn-success")

     
    def mobile_cardsFunc(self):
        
        return self.Reusable_WebdriverWait_for_visibility_of_any_elements_located(
            CheckOutPage.mobile_card)
    
    def mobile_Func(self):

        xpath=f"(//button[normalize-space()='Add'])[{self.count}]"
        Xpath=(By.XPATH,xpath)
        return self.Reusable_Webdriver_for_find_element(Xpath)

    def checkOut_btn_Func(self):
        return self.Reusable_Webdriver_for_find_element(CheckOutPage.checkOut_btn)
    
    def checkOut_Confirm_btn_Func(self):
        self.Reusable_Webdriver_for_find_element(CheckOutPage.confirm_checkout).click()
        confirmPage_Obj=ConfirmPage(self.driver)
        return confirmPage_Obj
  