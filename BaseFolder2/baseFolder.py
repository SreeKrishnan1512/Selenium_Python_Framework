
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

import inspect
import logging

import sys

sys.path.append("../")
#from PageObjects2.c_confirmPage import ConfirmPage
#from PageObjects2.a_homePage import HomePage

@pytest.mark.usefixtures("setup")

class Test_BaseFolder2:

    def get_logger(self):
        fileName= inspect.stack()[1][3]
        logger_obj=logging.getLogger(fileName)
        if not logger_obj.handlers:
            fileHandling_obj= logging.FileHandler("logging.log")
            formatter=logging.Formatter("%(asctime)s : %(levelname)s :%(name)s : %(message)s ")
            fileHandling_obj.setFormatter(formatter)
            logger_obj.addHandler(fileHandling_obj)
        logger_obj.setLevel(logging.DEBUG)
        return logger_obj

    def Reusable_WebdriverWait_for_visibility_of_element_located(self,locator):
       return WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located(locator))
    
    def Reusable_Webdriver_for_find_element(self,locator):
        return self.driver.find_element(*locator)
    #We are unpacking tuple here since we use self.driver here, so we use *locator 

    def Reusable_WebdriverWait_for_visibility_of_any_elements_located(self,locator):
       return WebDriverWait(self.driver,10).until(
            EC.visibility_of_any_elements_located(locator))
    
    def Resuable_Select(self,locator,text):
        dropdown= Select(locator)
       
        return dropdown.select_by_visible_text(text)
