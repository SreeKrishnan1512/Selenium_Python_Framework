import time

import sys
 
sys.path.append("../")
from BaseFolder2.baseFolder import Test_BaseFolder2
from PageObjects2.a_homePage import HomePage
from PageObjects2.b_checkoutPage import CheckOutPage
from PageObjects2.c_confirmPage import ConfirmPage


class Test_Two(Test_BaseFolder2):


    def test_e2e(self):
        #Logger=Test_BaseFolder2.test_logger(self)
        logger=self.get_logger()
        home_obj=HomePage(self.driver)

        logger.info("Moving towards Checkut Page ")
        checkOut_Obj=home_obj.homeFunc()
        
        logger.info("Getting all the mobile card titles ")
        mobile_card=checkOut_Obj.mobile_cardsFunc()
        



        count=0
        for mobile in mobile_card:

                name= mobile.text
                count=count+1
                logger.info(name)
                if name== "Blackberry":
                        
                        checkOut_Count=CheckOutPage(self.driver,count)
                        logger.info(f"Selecting {name} mobile ")
                        checkOut_Count.mobile_Func().click()
                        


        print(count)               

        checkOut_Obj.checkOut_btn_Func().click()

       
        confirmPage_Obj=checkOut_Obj.checkOut_Confirm_btn_Func()

        logger.info("Entering country name India ")
        confirmPage_Obj.country_name_Type_Func().send_keys("India")
        
     
        confirmPage_Obj.country_name_Select_Func().click()
        
        confirmPage_Obj.purchaseFunc().click()
       

        message= confirmPage_Obj.message_Func().text


        logger.info(f"Confirmation message: {message}")    
            
    


            