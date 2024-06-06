# Telefon rehberini saklamak için bir sözlük oluştur
tel_rehberi = dict()

# Yeni telefon numarası ekleme fonksiyonu
def tel_no_ekle(x):
    print('***Numara Ekleme Ekranına Hoşgeldiniz***')
    numara_isim_al = input('Lütfen Kayıt Edilecek Kişinin Adını Yazınız: ')
    numara_no_al = input('Lütfen Telefon Numarasını Giriniz: ')

    # Telefon rehberine numarayı ekle
    x = tel_rehberi.setdefault(numara_isim_al, numara_no_al)
    print(f'{numara_isim_al} adlı kişi telefon listesine eklendi....')
    input('Devam Edilsin mi? ')

# Telefon rehberini gösteren fonksiyon
def tel_rehber_goster(x):
    kisi_sayisi = len(x)
    print(f'Rehberinizdeki Kayıtlı Kişi Sayısı: {kisi_sayisi}')
    print('Rehbere Hoşgeldiniz')

    # Rehberdeki tüm kişileri ve numaralarını yazdır
    for isim, numara in x.items():
        print(isim, ':', numara)
    input('Devam Edilsin mi? ')

# Telefon rehberine numara ekleme ve gösterme örnekleri
tel_no_ekle(tel_rehberi)
tel_rehber_goster(tel_rehberi)

# Numarayı silme fonksiyonu
def no_sil(x):
    print('Kişi Silme Ekranına Hoşgeldiniz...')
    silinecek_kisi = input('Silinecek Kişiyi Yazınız: ')
    
    # Belirtilen kişiyi rehberden sil
    if silinecek_kisi in x:
        x.pop(silinecek_kisi)
        print(f'{silinecek_kisi} adlı kişi rehberden silindi.')
    else:
        print(f'{silinecek_kisi} adlı kişi rehberde bulunamadı.')
    
    input('Devam Edilsin mi? ')

# Ana menü döngüsü
while True:
    print('***HOŞGELDİNİZ***')
    print('***Seçim Yapınız***')
    secim_yap = int(input('1-Ekle\n2-Sil\n3-Rehberi Gör\n4-Çıkış\n'))

    if secim_yap == 1:
        tel_no_ekle(tel_rehberi)
    elif secim_yap == 2:
        no_sil(tel_rehberi)
    elif secim_yap == 3:
        tel_rehber_goster(tel_rehberi)
    elif secim_yap == 4:
        print('Programdan çıkılıyor...')
        break
    else:
        print('***Lütfen Uygun Tuşlara Basınız***')