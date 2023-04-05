import pytest
import sys;
from selenium import webdriver;
from webdriver_manager.chrome import ChromeDriverManager;
from selenium.webdriver.common.by import By;
from selenium.webdriver.common.action_chains import ActionChains
from pathlib import Path;
from datetime import date;
from commonCommands.waitForCommonCommand import WaitForCommonCommand;
from commonCommands.seleniumActionCommand import SeleniumActionCommand;

class Test_Sauce : 

    # def __init__(self) :
    #     self.driver=webdriver.Chrome(ChromeDriverManager().install())
    #     self.driver.maximize_window()
    #     self.driver.get("https://www.saucedemo.com/")
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
        self.removeSauceLabsBackpackId="remove-sauce-labs-backpack"
        self.SauceLabsBackpackAddToCartBtnId="add-to-cart-sauce-labs-backpack";
        self.loginBtnMessagePath="//*[@id='login_button_container']/div/form/div[3]/h3"
        #gunun tarixini al yoxdusa yarat
        #24.03.23
        self.folderPath=f"images/screenShots/{str(date.today())}"
        Path(self.folderPath).mkdir(exist_ok=True)
        self.method:str=""
        
    #her testden sonra calisar
    def teardown_method(self):
        path=f"{self.folderPath}/{self.method}.png"
        self.driver.save_screenshot(path)
        self.driver.quit()



#day4 task 2
    def test_empty_login_password(self):
        self.waitCommand.waitById(self.userNameId)
        loginBtn=self.actionCommand.findById(self.loginButtonId)
        loginBtn.click()

        errorMessage=self.actionCommand.findByXPath(self.loginBtnMessagePath)
        #sleep(10)
        assert errorMessage.text=="Epic sadface: Username is required"
        self.method=sys._getframe().f_code.co_name

    
    def test_invalid_password(self):
        self.waitCommand.waitById(self.userNameId)
        userNameInput=self.actionCommand.findById(self.userNameId)
        userNameInput.send_keys(self.standardUser)

        loginBtn=self.actionCommand.findById(self.loginButtonId)
        loginBtn.click();

        self.waitCommand.waitByXPath(self.loginBtnMessagePath)
        errorMessage= self.actionCommand.findByXPath(self.loginBtnMessagePath)

        assert errorMessage.text=="Epic sadface: Password is required"
        self.method=sys._getframe().f_code.co_name

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
        self.method=sys._getframe().f_code.co_name

    def test_whenUserNameAndPasswordIsEmpty_shouldViewRedX(self):
        self.waitCommand.waitById(self.userNameId)
        loginBtn=self.actionCommand.findById(self.loginButtonId)
        loginBtn.click();

        userNameCssSelector="#login_button_container > div > form > div:nth-child(1) > svg"
        paswordCssSelector="#login_button_container > div > form > div:nth-child(2) > svg"
        #sleep(5)
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

        self.method=sys._getframe().f_code.co_name
    
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
        self.method=sys._getframe().f_code.co_name

        
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
        self.method=sys._getframe().f_code.co_name

    def test_whenClickAddToCart_shouldBeCartItemIconIsRedOne(self):
        self.waitCommand.waitById(self.userNameId)
        userNameInput=self.actionCommand.findById(self.userNameId)
        passwordInput=self.actionCommand.findById(self.passwordId)
        self.actionChains.send_keys_to_element(userNameInput,self.standardUser)
        self.actionChains.send_keys_to_element(passwordInput,self.secretSauce)
        self.actionChains.perform()
        loginBtn=self.actionCommand.findById(self.loginButtonId)
        loginBtn.click();

        try :
            self.waitCommand.waitByCssSelector("#item_4_img_link > img")
        except:
            assert False
        
        
        addToCartBtn=self.actionCommand.findById(self.SauceLabsBackpackAddToCartBtnId)
        addToCartBtn.click();

        try :
            self.waitCommand.waitByCssSelector("#shopping_cart_container > a > span")
        except:assert False
        cartIcon=self.actionCommand.findByCssSelector("#shopping_cart_container > a > span")
        assert cartIcon.text=="1"

        self.method=sys._getframe().f_code.co_name

    def test_whenClickRemoveToCart_shouldBeCartItemIconBeEmpty(self):
        self.waitCommand.waitById(self.userNameId)
        userNameInput=self.actionCommand.findById(self.userNameId)
        passwordInput=self.actionCommand.findById(self.passwordId)
        self.actionChains.send_keys_to_element(userNameInput,self.standardUser)
        self.actionChains.send_keys_to_element(passwordInput,self.secretSauce)
        self.actionChains.perform()
        loginBtn=self.actionCommand.findById(self.loginButtonId)
        loginBtn.click();

        try :
            self.waitCommand.waitByCssSelector("#item_4_img_link > img")
        except:
            assert False
        
        self.SauceLabsBackpackAddToCartBtnId="add-to-cart-sauce-labs-backpack";
        addToCartBtn=self.actionCommand.findById(self.SauceLabsBackpackAddToCartBtnId)
        addToCartBtn.click();

        try :
            self.waitCommand.waitByCssSelector("#shopping_cart_container > a > span")
        except:assert False
        cartIcon=self.actionCommand.findByCssSelector("#shopping_cart_container > a > span")
        if cartIcon.text!="1":assert False;
        self.waitCommand.waitById(self.removeSauceLabsBackpackId)
        removeToCartBtn=self.actionCommand.findById(self.removeSauceLabsBackpackId);
        removeToCartBtn.click();
        try:
            cartIcon=self.actionCommand.findByCssSelector(
                "#shopping_cart_container > a > span");
        except:assert True; self.method=sys._getframe().f_code.co_name;
       
