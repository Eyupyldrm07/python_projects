def su_hesapla(kilo):
    e_hesapla =kilo*0.04
    k_hesapla =kilo*0.03

    cinsiyet = input('Lutfen Cinsiyetiniz giriniz: Kadin/Erkek:  ').lower()

    if cinsiyet =='erkek':
        print('*'*30)
        print('Cinsiyetiniz :',cinsiyet)
        print(e_hesapla,'Litre su icmelisiniz....')
    elif not cinsiyet:
        print('Lutfen cinsiyetiniz belirtiniz...')

    elif cinsiyet == 'kadin':
        print('*'*30)
        print('Cinsiyetiniz :',cinsiyet)
        print(k_hesapla,'Litre su icmelisiniz...')



kilo_al =float(input('Lutfen kilonuzu giriniz :'))
su_hesapla(kilo_al)