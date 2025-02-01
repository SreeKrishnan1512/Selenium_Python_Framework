from selenium.webdriver.common.by import By

from PageObjects2.b_checkoutPage import CheckOutPage

import sys

sys.path.append("../")

from BaseFolder2.baseFolder import Test_BaseFolder2

class HomePage(Test_BaseFolder2):

    def __init__(self,driver):
        self.driver=driver

    home= (By.XPATH,"//a[normalize-space()='Shop']")
    name= (By.XPATH,"(//input[@name='name'])[1]")
    email=(By.XPATH,"//input[@name='email']")
    password= (By.CSS_SELECTOR,"#exampleInputPassword1")
    Dropdown= (By.CSS_SELECTOR,"[id='exampleFormControlSelect1']")
    Submit= (By.CSS_SELECTOR,"input[value='Submit']")
    success_text= (By.CSS_SELECTOR,"div [class*=alert]")

    def homeFunc(self):
        
        self.Reusable_Webdriver_for_find_element(self.home).click()
        checkOut_Obj=CheckOutPage(self.driver)
        return checkOut_Obj
    
    def homeName_Func(self):
        return self.Reusable_Webdriver_for_find_element(self.name)
    #We can also write self.name or HomePage.name since they belong to the same class

    def homeEmail_Func(self):
        return self.Reusable_Webdriver_for_find_element(self.email)

    def homePassword_Func(self):
        return self.Reusable_Webdriver_for_find_element(self.password)
    
    def homeDropDown_Func(self):
        return self.Reusable_Webdriver_for_find_element(self.Dropdown)
     
    def homeSubmit_Func(self):
        return self.Reusable_Webdriver_for_find_element(self.Submit)
    
    def homeSuccessText_Func(self):
        return self.Reusable_WebdriverWait_for_visibility_of_element_located(self.success_text)
   