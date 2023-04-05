from selenium import webdriver;
from webdriver_manager.chrome import ChromeDriverManager;
from selenium.webdriver.common.by import By;

class SeleniumActionCommand:
    def __init__(self,driver:webdriver.Chrome):
        self.driver=driver

    def findById(self,id:str):
        findedElement=self.driver.find_element(By.ID,id)
        return findedElement ;

    def findById(self,name:str):
        findedElement=self.driver.find_element(By.NAME,name)
        return findedElement ;

    def findByXPath(self,xpath:str):
        findedElement=self.driver.find_element(By.XPATH,xpath)
        return findedElement ;

    def findByCssSelector(self,cssSelector):
        findedElement=self.driver.find_element(By.CSS_SELECTOR,cssSelector)
        return findedElement ;
