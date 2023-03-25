from selenium import webdriver;
from webdriver_manager.chrome import ChromeDriverManager;
from time import sleep;
from selenium.webdriver.common.by import By

driver  = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.google.com")
sleep(4)
input= driver.find_element(By.NAME, "q")
input.send_keys("kodlama io")
searchButton=driver.find_element(By.NAME,"btnK")
sleep(4)
searchButton.click()
sleep(4)
firstResult=driver.find_element(By.XPATH,"/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/a")
firstResult.click()
listOfCourses=driver.find_elements(By.CLASS_NAME, "course-listing")
print(len(listOfCourses))
#/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/a
##print(f"In : {input}")

while True :
    continue