from selenium import webdriver;
from webdriver_manager.chrome import ChromeDriverManager;
from selenium.webdriver.common.by import By;
from selenium.webdriver.support.wait import WebDriverWait;
from selenium.webdriver.support import expected_conditions;


class WaitForCommonCommand:
    def __init__(self,driver):
        self.driver=driver

    def waitById(self,id:str,time=5):
        WebDriverWait(self.driver,time).until(
            expected_conditions.visibility_of_element_located((By.ID,id)));

    def waitByXPath(self,xpath:str,time=5):
        WebDriverWait(self.driver,time).until(
            expected_conditions.visibility_of_element_located((By.XPATH,xpath)));
    
    def waitByCssSelector(self,cssSelector:str,time=5):
        WebDriverWait(self.driver,time).until(
            expected_conditions.visibility_of_element_located((By.XPATH,cssSelector)));