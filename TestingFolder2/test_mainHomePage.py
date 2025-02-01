
import pytest
import sys
sys.path.append("../")

from BaseFolder2.baseFolder import Test_BaseFolder2
from PageObjects2.a_homePage import HomePage
from TestData2.mainHomePageExcel import MainHomePageData_Excel

#@pytest.mark.usefixtures(getData)
@pytest.mark.parametrize("data", MainHomePageData_Excel.Main_HomePage_Function_Excel())
class Test_Main_HomePage(Test_BaseFolder2):
    
    
    def test_mainHP(self,data):

        
        
        logger=self.get_logger()
        logger.info(f"Running test for: {data}")

        HomePage_Object= HomePage(self.driver)  
        HomePage_Object.homeName_Func().send_keys(data["Name"])
        logger.info("The name is "+ data["Name"])
        HomePage_Object.homeEmail_Func().send_keys("rahulshetty@gmail.com")
        HomePage_Object.homePassword_Func().send_keys("Rahulshetty")



        self.Resuable_Select(HomePage_Object.homeDropDown_Func(),data["Gender"])
       
        logger.info(f"The gender is {data['Gender']}")

        

        HomePage_Object.homeSubmit_Func().click()


        txt= HomePage_Object.homeSuccessText_Func().text
        logger.info(f"Form submission message: {txt}")
        self.driver.refresh()

'''

    #MainHomePage_Obj=main_homePageData()
    @pytest.mark.parametrize("data", MainHomePageData_Excel.Main_HomePage_Function_Excel())
    def test_mainHP(self,data):
        logger=self.get_logger()
        logger.info(f"Running test for: {data}")

    @pytest.fixture(params= MainHomePageData_Excel.Main_HomePage_Function_Excel())

    def getData(self,request):

        return request.param
'''
