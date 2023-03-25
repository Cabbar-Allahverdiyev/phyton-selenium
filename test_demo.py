import pytest
from selenium import webdriver;
from webdriver_manager.chrome import ChromeDriverManager;
from time import sleep;
from selenium.webdriver.common.by import By;
from selenium.webdriver.support.wait import WebDriverWait;
from selenium.webdriver.support import expected_conditions;
from selenium.webdriver.common.action_chains import ActionChains
from pathlib import Path;
from datetime import date


class Test_Demo :
    #het testden once
    def setup_method(self):
        self.driver=webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        #gunun tarixini al yoxdusa yarat
        #24.03.23
        self.folderPath=str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True)
        
    #her testden sonra calisar
    def teardown_method(self):
        self.driver.quit()

    def test_demoFunc(self):
        text="Hello"
        assert text== "Hello"

    #@pytest.mark.skip()#parametr olaraq reason verile biler arasdir
    @pytest.mark.parametrize("username,password",[("1","1"),("ad","soyad")])
    def test_invalid_login(self,username,password):
        WebDriverWait(self.driver,5).until(
            expected_conditions.visibility_of_element_located((By.ID,"user-name")));
        userNameInput=self.driver.find_element(By.ID,"user-name")
        passwordInput=self.driver.find_element(By.ID,"password")
        userNameInput.send_keys(username)
        passwordInput.send_keys(password)
        WebDriverWait(self.driver,5).until(
            expected_conditions.visibility_of_element_located((By.ID,"login-button")));
        loginBtn=self.driver.find_element(By.ID,"login-button")
        
        loginBtn.click()
        # WebDriverWait(self.driver,5).until(
        #     expected_conditions.visibility_of_element_located((By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")));
        errorMessage=self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-invalid-login-{username}-{password}.png")
        assert errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
        
    
    def test_valid_login(self):
        # self.driver.get("https://www.saucedemo.com/")
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
        assert True
