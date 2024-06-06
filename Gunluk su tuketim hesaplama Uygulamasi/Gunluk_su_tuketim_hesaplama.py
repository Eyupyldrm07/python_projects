def su_hesapla(kilo):
    # Erkekler için su miktarını hesapla (kilogram başına 0.04 litre)
    e_hesapla = kilo * 0.04
    # Kadınlar için su miktarını hesapla (kilogram başına 0.03 litre)
    k_hesapla = kilo * 0.03

    # Kullanıcıdan cinsiyet bilgisini al
    cinsiyet = input('Lütfen cinsiyetinizi giriniz: Kadın/Erkek:  ').lower()

    # Cinsiyet erkek ise
    if cinsiyet == 'erkek':
        print('*' * 30)
        print('Cinsiyetiniz :', cinsiyet)
        print(e_hesapla, 'Litre su içmelisiniz...')
    # Cinsiyet belirtilmemişse
    elif not cinsiyet:
        print('Lütfen cinsiyetinizi belirtiniz...')

    # Cinsiyet kadın ise
    elif cinsiyet == 'kadin':
        print('*' * 30)
        print('Cinsiyetiniz :', cinsiyet)
        print(k_hesapla, 'Litre su içmelisiniz...')

# Kullanıcıdan kilo bilgisini al ve float veri tipine çevir
kilo_al = float(input('Lütfen kilonuzu giriniz: '))
# su_hesapla fonksiyonunu çağır
su_hesapla(kilo_al)