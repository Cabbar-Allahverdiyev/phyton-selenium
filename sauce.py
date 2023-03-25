from selenium import webdriver;
from webdriver_manager.chrome import ChromeDriverManager;
from time import sleep;
from selenium.webdriver.common.by import By;
from selenium.webdriver.support.wait import WebDriverWait;
from selenium.webdriver.support import expected_conditions;
from selenium.webdriver.common.action_chains import ActionChains

class Test_Sauce : 

    # def __init__(self) :
    #     self.driver=webdriver.Chrome(ChromeDriverManager().install())
    #     self.driver.maximize_window()
    #     self.driver.get("https://www.saucedemo.com/")

    

    def test_invalid_login(self):
        WebDriverWait(self.driver,5).until(
            expected_conditions.visibility_of_element_located((By.ID,"user-name")));
        userNameInput=self.driver.find_element(By.ID,"user-name")
        passwordInput=self.driver.find_element(By.ID,"password")
        userNameInput.send_keys("1")
        passwordInput.send_keys("1")
        WebDriverWait(self.driver,5).until(
            expected_conditions.visibility_of_element_located((By.ID,"login-button")));
        loginBtn=self.driver.find_element(By.ID,"login-button")
        
        loginBtn.click()
        WebDriverWait(self.driver,5).until(
            expected_conditions.visibility_of_element_located((By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")));
        errorMessage=self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testresult=errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
        print(f"cavab : {testresult}")
    
    def test_valid_login(self):
        self.driver.get("https://www.saucedemo.com/")
        WebDriverWait(self.driver,5).until(
            expected_conditions.visibility_of_element_located((By.ID,"user-name")));
        userNameInput=self.driver.find_element(By.ID,"user-name")
        passwordInput=self.driver.find_element(By.ID,"password")
        
        #Js
        self.driver.execute_script("window.scrollTo(0,500)")

        #action chains
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(userNameInput,"standard_user")
        actions.send_keys_to_element(passwordInput,"secret_sauce")
        actions.perform()
        WebDriverWait(self.driver,5).until(
            expected_conditions.visibility_of_element_located((By.ID,"login-button")));
        loginBtn=self.driver.find_element(By.ID,"login-button")
        
        loginBtn.click()
        sleep(100)

        


testClass=Test_Sauce()
testClass.test_invalid_login()
testClass.test_valid_login()


