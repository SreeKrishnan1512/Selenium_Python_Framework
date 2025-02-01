from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import sys

sys.path.append("../")

from BaseFolder2.baseFolder import Test_BaseFolder2

#Class name and file name should be different
class ConfirmPage(Test_BaseFolder2):

    def __init__(self,driver):
        self.driver=driver
 
    country_name= (By.CSS_SELECTOR,"input[class*='form-control']")
    country_name_select= (By.XPATH,"//a[normalize-space()='India']")
    purchase=(By.CSS_SELECTOR,"input[value='Purchase']")
    message=(By.CSS_SELECTOR,"div[class*='alert-success']")

    def country_name_Type_Func(self):
        
        return self.Reusable_Webdriver_for_find_element(ConfirmPage.country_name)
    
    def country_name_Select_Func(self):
        #now Reusable_Webdriver belongs to the ConfirmPage class since Reusable_Webdriver
        # is inherited from the Test_BaseFolder2 class and we are calling it inside
        #the method of ConfirmPage class that is "country_name_Select_Func" rather than from
        # class level of ConfirmPage, we are writing self.Reusable_Webdriver()
        
        return self.Reusable_WebdriverWait_for_visibility_of_element_located(
            ConfirmPage.country_name_select) 
    
    def purchaseFunc(self):
        return self.Reusable_Webdriver_for_find_element(ConfirmPage.purchase)
    
    def message_Func(self):
        return self.Reusable_WebdriverWait_for_visibility_of_element_located(ConfirmPage.message)