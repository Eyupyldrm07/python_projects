import sqlite3

# Veritabanı bağlantısı oluşturulur
db = sqlite3.connect('veresiye.db')
yetki = db.cursor()

# 'kisiler' adında bir tablo oluşturulur, eğer mevcut değilse
yetki.execute("CREATE TABLE IF NOT EXISTS kisiler (İsim, borc)")

# Ana döngü, kullanıcıdan giriş alarak işlemleri gerçekleştirir
while True:
    print("***VERESİYE DEFTERİNE HOŞGELDİNİZ***")
    sor = input("1-BORÇLU EKLE:\n2-BORÇLULARI GÖR:\n")
    
    if sor == "1":
        # Kullanıcıdan borçlu kişinin ismi ve borç miktarı istenir
        borclu_isim = input('Lütfen borçlunun ismini giriniz:')
        borclu_miktari = input('Lütfen borç miktarını giriniz:')
        
        # Borçlu bilgileri veritabanına eklenir
        yetki.execute(f'INSERT INTO kisiler VALUES("{borclu_isim}", "{borclu_miktari}")')
        db.commit()
        
        print(f'İşlem Tamamlandı, Borçlu kişinin adı: {borclu_isim}')

    elif sor == '2':
        # Tüm borçlu bilgileri veritabanından alınır
        yetki.execute('SELECT * FROM kisiler')
        yazdir = yetki.fetchall()
        
        # Borçlu bilgileri ekrana yazdırılır
        say = 1
        for i in yazdir:
            print('-----Borçlu bilgisi-----')
            print(f'{say}: Borçlunun İsmi: {i[0]}\n Borçlu olduğu miktar: {i[1]}\n')
            say += 1
        
        input('Devam Edilsin mi?')
