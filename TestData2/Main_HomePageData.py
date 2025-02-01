
'''
class main_homePageData:

    #test_Main_HomePageData=[{"Name":"RahulShetty","Gender":"Male"},{"Name":"AnushkaShetty","Gender":"Female"}]

    @staticmethod
    def HomePageData_Func():
       
        return [{"Name":"RahulShetty","Gender":"Male"},{"Name":"AnushkaShetty","Gender":"Female"},{"Name":"Guru","Gender":"Male"}]
    
    #Since this class is a static method means it does not require instance attribute we are
    #writing @staticmethod, here since we are not using self which is an instance and needs
    #an instance variable say for "main_homePageData" which is needed to be created an instance
    # Main_HomePageData= main_homePageData(), this can be avoided since HomePageData_Func does not
    #require self since it does not require instance attribute
'''
