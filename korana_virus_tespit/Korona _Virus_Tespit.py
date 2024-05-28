# Korana virus tespit Uygulamasi.Hasta belirli semptomlari sagliyorsa 
# En yakin saglik kurulusuna gitmesi icin yonlendiriyor .



ates_durumu=float(input('Lutfen ates Derecenizi Yaziniz:'))
oksuruk = input('Oksurugunuz var mi ? E/H:').lower()
bas_agrisi= input('Bas agriniz var mi ? E/H:').lower()
gun =int(input('Sikayetleriniz kac Gundur var?'))


if ates_durumu >=39:
    if gun >=3:
        print('*** Uyari Hastaneye Gidiniz')
    else:
        print('Ates Durumunuz Sinirda ,Devam Ederse Lutfen En Yakin Saglik Kurulusuna gidiniz')

if (ates_durumu >= 39) and (oksuruk=='e') and (bas_agrisi=='e')and(gun>=3):
    print('**** Acil Lutfen En Yakin Saglik Kurulusuna Gidiniz.')
    print('**** Acil Durumunuz Olumlu Degil....')

elif (oksuruk=='e') or (bas_agrisi=='e') or (gun >=3):
    print('*** Hatirlatma Durumunuz Bu Sekilde Devam Ederse Lutfen Saglik Kurulusuna Gidiniz...')

else:
    print('Ates Durumunuz 39 Derecenin Ustune Cikar Ise ,Lutfen Saglik Kurulusuna Gidiniz')
    print(f'Atesiniz: {ates_durumu}')