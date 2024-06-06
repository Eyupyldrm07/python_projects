# Bankamatik Uygulamasi

# Eyup YILDIRIM'in hesap bilgileri
eyupHesap = {
    'ad': 'Eyup YILDIRIM',
    'hesapNo': '13245678',
    'bakiye': 3000,
    'ekHesap': 2000
}

# Mustafa YILDIRIM'in hesap bilgileri
mustafaHesap = {
    'ad': 'Mustafa YILDIRIM',
    'hesapNo': '13245678',
    'bakiye': 3000,
    'ekHesap': 2000
}

# Para çekme işlemi için fonksiyon
def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    # Ana hesaptaki bakiyenin yeterli olup olmadığını kontrol et
    if hesap['bakiye'] >= miktar:
        hesap['bakiye'] -= miktar
        print('Paranızı alabilirsiniz.')
        bakiyeSorgula(hesap)

    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']

        # Toplam bakiye yeterli mi kontrol et
        if toplam >= miktar:
            ekHesapKullanimi = input('Ek hesap kullanılsın mı (E/H): ')

            if ekHesapKullanimi.lower() == 'e':
                ekHesapKullanilacakMiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ekHesapKullanilacakMiktar
                print('Paranızı alabilirsiniz.')
                bakiyeSorgula(hesap)
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır.")

        else:
            print('Üzgünüz bakiye yetersiz.')
            bakiyeSorgula(hesap)

# Hesap bakiyesini sorgulama fonksiyonu
def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesap limitiniz ise {hesap['ekHesap']} TL bulunmaktadır.")

# Eyup YILDIRIM'in hesabından para çekme işlemi
paraCek(eyupHesap, 3000)

print('******************************')

# Eyup YILDIRIM'in hesabından tekrar para çekme işlemi
paraCek(eyupHesap, 2000)