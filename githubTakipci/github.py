from githubUserInfo import username,password
from selenium.webdriver.common.by import By

from selenium import webdriver
import time

class Github:
    def __init__(self,username,password) :
        self.browser = webdriver.Firefox()
        self.username= username
        self.password=password
        self.followers=[]

    def singIn(self):
        self.browser.get('https://github.com/login')
        time.sleep(2)

        self.browser.find_element(By.XPATH,"//*[@id='login_field']").send_keys(self.username)
        self.browser.find_element(By.XPATH,"//*[@id='password']").send_keys(self.password)


        time.sleep(1)


        self.browser.find_element(By.XPATH,"//*[@id='login']/div[4]/form/div/input[13]").click()

    time.sleep(2)

    def getFollowers(self):
        self.browser.get("https://github.com/Eyupyldrm07?tab=followers")
        time.sleep(2)

        items=self.browser.find_elements(By.XPATH,"//*[@id='user-profile-frame']/div")

        for i in items:
            self.followers.append(i.find_element(By.XPATH,"//*[@id='user-profile-frame']/div/div[5]/div[2]/a/span[2]").text)


github =Github (username ,password)
github.singIn()
github.getFollowers()
print(github.followers)
