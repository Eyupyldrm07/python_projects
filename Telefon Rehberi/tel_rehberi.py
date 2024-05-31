tel_rehberi = dict()

def tel_no_ekle(x):
    print('***Numara Ekleme Ekranina Hosgeldiniz***')
    numara_isim_al=input('Lutfen Kayit Edilecek Kisinin Adini Yaziniz')
    numara_no_al=input('Lutfen Telefon Numarasini Giriniz')

    x = tel_rehberi.setdefault(numara_isim_al,numara_no_al)
    print(f'{numara_isim_al}''adli kisi telefon listesine eklendi....')
    input('Devam Edilsin mi ?')




def tel_rehber_goster(x):
    kisi_sayisi = len(x)
    print(f'Rehberinizdeki Kayitli Kisi Sayisi:{kisi_sayisi}')
    print('Rehbere Hosgeldiniz')

    for i,j in x.items():
        print(i,':',j)
    input('Devam Edilsin mi ?')

tel_no_ekle(tel_rehberi)
tel_rehber_goster(tel_rehberi)


def no_sil(x):
    print('Kisi Silme Ekranina Hosgeldiniz...')
    silinecek_kisi=input('Silinecek Kisiyi Yazisiniz:')
    x =tel_rehberi.pop(silinecek_kisi )
    input('Devam Edilsin mi ?')



while True:
    print('***HOSGELDINIZ***')
    print('***Secim Yapiniz***')
    secim_yap=int(input('1-Ekle\n2-Sil\n3-Rehberi Gor\n'))

    if secim_yap==1:
        tel_no_ekle(tel_rehberi)
    elif secim_yap==2:
        no_sil(tel_rehberi)
    elif secim_yap==3:
        tel_rehber_goster(tel_rehberi)
    else:
        print('***Lutfen Uygun Tuslara Basiniz')