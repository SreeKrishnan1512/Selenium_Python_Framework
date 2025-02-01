
from logging import config
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--browserName",
        action="store",
        default="chrome",
        #help="my option: type1 or type2",
        #choices=("type1", "type2"),
    )

@pytest.fixture(scope="class")

def setup(request):
    browserName=request.config.getoption("browserName") #Using this key we can retrieve value that is chrome
    #if config.getoption("chrome"):
    if browserName == "chrome":
            chrome_path="C:/Users/psaik/Desktop/Python_Selenium_Framework2/chromedriver-win64/chromedriver-win64/chromedriver.exe" 
            serive_object= Service(chrome_path)
            driver= webdriver.Chrome(service=serive_object)
        
    
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver=driver
 
    yield
    driver.close()

    # this is how we should write in cli : pytest .\Test_E2E.py --browserName=chrome -v -s 
    # or pytest .\Test_E2E.py --browserName chrome -v -s
    #--html=report.html this is the command line for getting reports in browser

    