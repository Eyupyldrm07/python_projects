import requests
from  bs4  import BeautifulSoup
from colorama import Fore,init 
import os 

  
init(autoreset=True)


def takim_bilgilerini_cek(takim):
    clear_screen()
    # web sitesinden verileri cek
    url =f'https://www.sporx.com/{takim}-fiksturu-ve-mac-sonuclari'
    response =requests.get(url)
    soup = BeautifulSoup(response.content,'html.parser')

    #  mac sonuclarini bul
    maclar = soup.find_all('tr')
    galibiyet_sayisi = 0
    toplam_gol = 0
    son_mac_skor = None 
    for mac in maclar :
        skor_elementi = mac.find('a',class_="d-block rounded bg-sporx text-white fw-bolder py-1 px-1 text-nowrap")
        if skor_elementi:
            skor = skor_elementi.get_text(strip=True)
            gol_sayisi = skor.split('-')
            if len (gol_sayisi) == 2  and gol_sayisi[0].strip()  and  gol_sayisi[1].strip():
                try:
                    attigi_gol = int(gol_sayisi[0])
                    gol_sayisi_g2 = int(gol_sayisi[1])
                except ValueError:
                    attigi_gol = None
                    gol_sayisi_g2 = None
                if attigi_gol is not None and gol_sayisi_g2 is not None:
                    ev_sahibi = mac.find('td',class_="text-start w-25").find('a').get_text(strip=True)
                    depslanman = mac.find('td',class_="text-end w-25").find('a').get_text(strip=True)
                    if takim.lower() == turkce_karakter_degistir(ev_sahibi.lower()):
                        toplam_gol += attigi_gol
                        if attigi_gol > gol_sayisi_g2:
                            galibiyet_sayisi +=1
                        son_mac_skor = f'{ev_sahibi} {skor} {depslanman}\n'
                    elif takim.lower() == turkce_karakter_degistir(depslanman.lower()):
                        toplam_gol+= gol_sayisi_g2
                        if attigi_gol<gol_sayisi_g2:
                            galibiyet_sayisi+=1
                            son_mac_skor = f'{ev_sahibi} {skor} {depslanman}\n'
    if galibiyet_sayisi ==0:
        print(Fore.RED + F'{takim}.capitalize()')
        return None,None,None
    else:
        return galibiyet_sayisi,toplam_gol,son_mac_skor
            
def clear_screen():
    os.system('cls' if os.name =='nt' else 'clear' )
def turkce_karakter_degistir(takim_ad):
    takim_ad =takim_ad.replace('ı','i')
    takim_ad =takim_ad.replace('ç','c')
    takim_ad =takim_ad.replace('ü','u')
    takim_ad =takim_ad.replace('ş','s')
    takim_ad =takim_ad.replace('ğ','g')
    takim_ad =takim_ad.replace('ö','o')
    return takim_ad

def son_mac_bilgilerini_cek(takim):
    url =f'https://www.sporx.com/{takim}-fiksturu-ve-mac-sonuclari'
    response =requests.get(url)
    soup = BeautifulSoup(response.content,'html.parser')
    maclar = soup.find_all('tr')
    son_10_mac_gol_sayilari = []
    mac_sayaci = 0

    for mac in maclar :
        skor_elementi = mac.find('a',class_="d-block rounded bg-sporx text-white fw-bolder py-1 px-1 text-nowrap")
        if skor_elementi:
            skor = skor_elementi.get_text(strip=True)
            gol_sayisi = skor.split('-')
            if len (gol_sayisi) == 2  and gol_sayisi[0].strip()  and  gol_sayisi[1].strip():
                try:
                    gol_sayisi_g1 =int(gol_sayisi[0])
                    gol_sayisi_g2 = int(gol_sayisi[1])
                    son_10_mac_gol_sayilari.append(gol_sayisi_g1)
                    son_10_mac_gol_sayilari.append(gol_sayisi_g2)
                    mac_sayaci +=1
                except ValueError:
                    continue
                if mac_sayaci >=7:
                    break

    return son_10_mac_gol_sayilari

def iki_takimli_analiz(takim1,takim2):
    clear_screen()
    # takimlar gosteriliyor
    sonuc=f'{takim1.capitalize()} vs{takim2.capitalize()}'
    sonuc=f'---------------------------------------------\n'

    # takim 1 bilgilerini cek 
    takim1_bilgilerini_cek = takim_bilgilerini_cek(takim1)
    if takim1_bilgilerini_cek is None:
        return
    galibiyet_sayisi_g1 , gol_sayisi_g1 , son_mac_skor_g1 = takim1_bilgilerini_cek
      # takim 2 bilgilerini cek 
    takim2_bilgilerini_cek = takim_bilgilerini_cek(takim2)
    if takim2_bilgilerini_cek is None:
        return
    galibiyet_sayisi_g2 , gol_sayisi_g2 , son_mac_skor_g2 = takim2_bilgilerini_cek

    sonuc+=f'{takim1}\nGalibiyet Sayisi:{galibiyet_sayisi_g1}\nGol Sayisi:{gol_sayisi_g1}\nSon Mac:{son_mac_skor_g1}             '
    sonuc+=f'{takim2}\nGalibiyet Sayisi:{galibiyet_sayisi_g2}\nGol Sayisi:{gol_sayisi_g2}\nSon Mac:{son_mac_skor_g2}             '
    

    if galibiyet_sayisi_g1 is not None and galibiyet_sayisi_g2 is not None:
        if galibiyet_sayisi_g1 > galibiyet_sayisi_g2:
            sonuc+=f'{Fore.GREEN} {takim1.capitalize()} Takimi {takim2.capitalize()} Similasyona gore yendi '
        elif galibiyet_sayisi_g1 < galibiyet_sayisi_g2:
            sonuc+=f'{Fore.GREEN} {takim2.capitalize()} Takimi {takim1.capitalize()} Similasyona gore yendi '
        else:
            sonuc += f'{Fore.YELLOW} Iki takim arasindaki mac similasyona gore berabere bitti'
    else:
        sonuc+= f'{Fore.RED} Veri Alinamadi Lutfen Daha Sonra Tekrar Deneyin!'

    # muhtemel gol sayisi
    if galibiyet_sayisi_g1 is not None and galibiyet_sayisi_g2 is not None:
        takim1_son_5_mac = son_mac_bilgilerini_cek(takim1)
        takim2_son_5_mac = son_mac_bilgilerini_cek(takim2)
        if len(takim1_son_5_mac) < 7 or len(takim2_bilgilerini_cek) <7:
            print(Fore.RED+'Veri Bulunamadi')
        ortalama_gol_takim1 = sum(takim1_son_5_mac)/len(takim1_son_5_mac)
        ortalama_gol_takim2 = sum(takim2_son_5_mac)/len(takim2_son_5_mac)

        # tahmin edilen gol sayisini hesapla 
        ortalama_gol = (ortalama_gol_takim1+ortalama_gol_takim2)/2
        gol_tahmini =ortalama_gol +0.25 if takim1_bilgilerini_cek[-1]>takim2_son_5_mac[-1] else ortalama_gol

        sonuc +=f'{Fore.GREEN}Macta Muhtemelen{gol_tahmini:.2f} gol olacak.\n'
    print(sonuc)



while  True:
    takim1=input('Lutfen Ev sahibi takimi Giriniz:')
    takim2=input('Lutfen Depslasman takimi Giriniz:')
    iki_takimli_analiz(takim1,takim2)
    devam = input('Baska islem Yapmak Istermisiniz? (E/H)')
    if devam.lower() !='e':
        break