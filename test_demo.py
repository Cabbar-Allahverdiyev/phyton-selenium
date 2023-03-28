from time import sleep
import pytest
from selenium import webdriver;
from webdriver_manager.chrome import ChromeDriverManager;
from selenium.webdriver.common.by import By;
from selenium.webdriver.support.wait import WebDriverWait;
from selenium.webdriver.support import expected_conditions;
from selenium.webdriver.common.action_chains import ActionChains
from pathlib import Path;
from datetime import date
from common.waitForCommonCommand import WaitForCommonCommand;
from common.seleniumActionCommand import SeleniumActionCommand;



class Test_Demo :
    #het testden once
    def setup_method(self):
        self.driver=webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        self.waitCommand=WaitForCommonCommand(self.driver)
        self.actionCommand=SeleniumActionCommand(self.driver)
        self.actionChains=ActionChains(self.driver)
        self.standardUser="standard_user"
        self.secretSauce="secret_sauce"
        self.loginButtonId="login-button"
        self.userNameId="user-name"
        self.passwordId="password"
        self.loginBtnMessagePath="//*[@id='login_button_container']/div/form/div[3]/h3"
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

#day4 task 2
    def test_empty_login_password(self):
        self.waitCommand.waitById(self.userNameId)
        loginBtn=self.actionCommand.findById(self.loginButtonId)
        loginBtn.click()

        errorMessage=self.actionCommand.findByXPath(self.loginBtnMessagePath)
        #sleep(10)
        assert errorMessage.text=="Epic sadface: Username is required"

    
    def test_invalid_password(self):
        self.waitCommand.waitById(self.userNameId)
        userNameInput=self.actionCommand.findById(self.userNameId)
        userNameInput.send_keys(self.standardUser)

        loginBtn=self.actionCommand.findById(self.loginButtonId)
        loginBtn.click();

        self.waitCommand.waitByXPath(self.loginBtnMessagePath)
        errorMessage= self.actionCommand.findByXPath(self.loginBtnMessagePath)

        assert errorMessage.text=="Epic sadface: Password is required"

    #@pytest.mark.parametrize("username,password",[("1","1"),("ad","soyad")])
    def test_userName_lockedOutUser(self):
        self.waitCommand.waitById(self.userNameId)
        userNameInput=self.actionCommand.findById(self.userNameId)
        passwordInput=self.actionCommand.findById(self.passwordId)

        self.actionChains.send_keys_to_element(userNameInput,"locked_out_user")
        self.actionChains.send_keys_to_element(passwordInput,self.secretSauce)
        self.actionChains.perform()
        
        loginBtn=self.actionCommand.findById(self.loginButtonId)
        loginBtn.click();

        errorMessage= self.actionCommand.findByXPath(self.loginBtnMessagePath)
        assert errorMessage.text=="Epic sadface: Sorry, this user has been locked out."

    def test_whenUserNameAndPasswordIsEmpty_shouldViewRedX(self):
        self.waitCommand.waitById(self.userNameId)
        loginBtn=self.actionCommand.findById(self.loginButtonId)
        loginBtn.click();

        userNameCssSelector="#login_button_container > div > form > div:nth-child(1) > svg"
        paswordCssSelector="#login_button_container > div > form > div:nth-child(2) > svg"
        sleep(5)
        usernameErrorBtn:str=""
        passwordErrorBtn=""
        try:
            usernameErrorBtn=self.actionCommand.findByCssSelector(userNameCssSelector)
            passwordErrorBtn=self.actionCommand.findByCssSelector(paswordCssSelector)
            if(not usernameErrorBtn.is_displayed() or not passwordErrorBtn.is_displayed()):
                assert False;
                
        except:
            assert False
        #    assert False
        errorBtn=self.actionCommand.findByXPath("//*[@id='login_button_container']/div/form/div[3]/h3/button")
        errorBtn.click()

        try:
            usernameErrorBtn=self.actionCommand.findByCssSelector(userNameCssSelector)
            passwordErrorBtn=self.actionCommand.findByCssSelector(paswordCssSelector)
            if(not usernameErrorBtn.is_displayed() and not passwordErrorBtn.is_displayed()):
                assert True;
            assert False
        except:
            assert True
    
    def test_whenValidLogin_shouldBeInInventory(self):
        self.waitCommand.waitById(self.userNameId)
        userNameInput=self.actionCommand.findById(self.userNameId)
        passwordInput=self.actionCommand.findById(self.passwordId)

        self.actionChains.send_keys_to_element(userNameInput,self.standardUser)
        self.actionChains.send_keys_to_element(passwordInput,self.secretSauce)
        self.actionChains.perform()
        loginBtn=self.actionCommand.findById(self.loginButtonId)
        loginBtn.click();

        currentUrl=str(self.driver.current_url)
        assert "https://www.saucedemo.com/inventory.html" == currentUrl

        
    def test_whenValidLogin_shoulBeVisibleSixProduct(self):
        self.waitCommand.waitById(self.userNameId)
        userNameInput=self.actionCommand.findById(self.userNameId)
        passwordInput=self.actionCommand.findById(self.passwordId)

        self.actionChains.send_keys_to_element(userNameInput,self.standardUser)
        self.actionChains.send_keys_to_element(passwordInput,self.secretSauce)
        self.actionChains.perform()
        loginBtn=self.actionCommand.findById(self.loginButtonId)
        loginBtn.click();

        xpathInventoryContainer="//*[@id='inventory_container']/div"
        self.waitCommand.waitByXPath(xpathInventoryContainer)
        countOfProducts=len(self.driver.find_elements(By.CLASS_NAME,"inventory_item"))
        assert countOfProducts==6
