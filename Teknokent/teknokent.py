from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

# Hedef URL ve başlık bilgisi
url = 'https://www.gaziantepteknopark.com.tr/blg-arge-bilisim-hiz-dan-egt-gida-mak-ve-tb-urn-iml-san-ve-tic-ltd-sti'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# URL'ye istek gönder ve BeautifulSoup ile içeriği ayrıştır
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

# Selenium ile tarayıcıyı başlat
tarayici = webdriver.Chrome()
tarayici.get('https://www.gaziantepteknopark.com.tr/')
time.sleep(1)
tarayici.maximize_window()

# Menüdeki "Firma Listesi" linkine tıkla
tikla = tarayici.find_element(By.XPATH, '//*[@id="navbar"]/ul/li[3]/a')
time.sleep(2)
tikla.click()
time.sleep(2)

# Firma kartlarını bul ve sayısını yazdır
firma_listesi = tarayici.find_elements(By.XPATH, '//div[contains(@class, "firma-card")]/a')
print('Bulunan Firma sayisi', len(firma_listesi))
print('Firma Listesi.oge ', firma_listesi[1].text)

# Şirket bilgilerini saklamak için bir sözlük oluştur
listelenmis_hali = {'Sirket ismi': 'sirket_isim', 'Sirket maili': 'div_cek'}

# Her bir firma için bilgileri çek
for i in firma_listesi:
    href = i.get_attribute('href')
    
    # Her firma için yeni bir tarayıcı penceresi aç
    tarayici1 = webdriver.Chrome()
    tarayici1.get(href)
    time.sleep(1)
    
    # İletişim sekmesine tıkla
    iletisim_tikla = tarayici1.find_element(By.XPATH, '//*[@id="iletisim-tab"]')
    time.sleep(1)
    iletisim_tikla.click()

    # Firma detay sayfasını BeautifulSoup ile ayrıştır
    response1 = requests.get(href, headers=headers)
    soup1 = BeautifulSoup(response1.content, 'html.parser')

    # Şirket e-posta ve isim bilgilerini çek
    div_cek = soup1.find('table', {'class': 'table'}).a
    sirket_isim = soup1.find('h1', {'class': 'section-title w-full t-left t-bold t-oswald profile-title'}).text
    
   

    # Bilgileri sözlüğe ekle
    listelenmis_hali[sirket_isim.replace('\n','').strip()] = div_cek.get('href').replace("mailto:",'')
    tarayici1.quit()
    print(listelenmis_hali.items())
    


# Tüm bilgileri yazdır
print(listelenmis_hali.items())

# Ana tarayıcıyı kapat
time.sleep(10)
tarayici.quit()