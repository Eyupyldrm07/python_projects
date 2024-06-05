#  Bankamatik Uygulamasi

eyupHesap = {
    'ad':'Eyup YILDIRIM',
    'hesapNo':'13245678',
    'bakiye':3000,
    'ekHesap':2000
}

mustafaHesap = {
    'ad':'Mustafa  YILDIRIM',
    'hesapNo':'13245678',
    'bakiye':3000,
    'ekHesap':2000
}


def paraCek(hesap, miktar):
    print(f'Merhaba {hesap['ad']}')

    if (hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar
        print('paranizi alabilirsiniz.')
        bakiyeSorgula(hesap)

    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']

        if (toplam >= miktar):
            ekHesapKullanimi = input('Ek hesap kullanilsin mi (E/H)')

            if ekHesapKullanimi =='e':

                ekHesapKullanilacakMiktar = miktar - hesap['bakiye']
                hesap ['bakiye'] = 0 
                hesap['ekHesap'] -= ekHesapKullanilacakMiktar
                print('paranizi alabilirsiniz')
                bakiyeSorgula(hesap)
            else:
                print(f'{hesap['hesapNo']}nolu hesabinizda {hesap['bakiye']} bulunmaktadir.')
    

        else:
            print('uzgunuz bakiye yetersiz.')
            bakiyeSorgula(hesap)
            

def bakiyeSorgula(hesap):
    print(f'{hesap['hesapNo']}nolu hesabinizda  {hesap['bakiye']} TL bulunmaktadir.Ek hesao liminitiz ise {hesap['ekHesap']} TL bulunmaktadir.')

paraCek(eyupHesap,3000)

print('******************************')
paraCek(eyupHesap,2000)
