from githubUserInfo import username, password  # Kullanıcı bilgilerini içe aktar
from selenium.webdriver.common.by import By  # Selenium için gerekli kütüphaneler
from selenium import webdriver
import time  # Zaman gecikmeleri için gerekli kütüphane

class Github:
    def __init__(self, username, password):
        self.browser = webdriver.Firefox()  # Firefox tarayıcısını başlat
        self.username = username
        self.password = password
        self.followers = []  # Takipçileri tutacak liste

    def signIn(self):
        # GitHub giriş sayfasını aç
        self.browser.get('https://github.com/login')
        time.sleep(2)

        # Kullanıcı adı ve şifreyi ilgili alanlara gir
        self.browser.find_element(By.XPATH, "//*[@id='login_field']").send_keys(self.username)
        self.browser.find_element(By.XPATH, "//*[@id='password']").send_keys(self.password)
        time.sleep(1)

        # Giriş yap butonuna tıkla
        self.browser.find_element(By.XPATH, "//*[@id='login']/div[4]/form/div/input[13]").click()
        time.sleep(2)

    def getFollowers(self):
        # Kullanıcının takipçi sayfasını aç
        self.browser.get(f"https://github.com/{self.username}?tab=followers")
        time.sleep(2)

        # Takipçi elemanlarını bul
        items = self.browser.find_elements(By.XPATH, "//*[@id='user-profile-frame']/div")

        # Her takipçiyi takipçiler listesine ekle
        for i in items:
            self.followers.append(i.find_element(By.XPATH, "//*[@id='user-profile-frame']/div/div[5]/div[2]/a/span[2]").text)

# Github sınıfından bir örnek oluştur ve işlemleri gerçekleştir
github = Github(username, password)
github.signIn()
github.getFollowers()
print(github.followers)  # Takipçileri yazdır