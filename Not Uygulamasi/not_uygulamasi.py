def note_calculate(line):
    # Satır sonundaki yeni satır karakterini kaldır
    line = line[:-1]
    # Satırı ':' karakterine göre ayırarak isim ve notları ayır
    list = line.split(':')

    studentName = list[0]
    notes = list[1].split(',')

    # Notları tamsayıya çevir
    note1 = int(notes[0])
    note2 = int(notes[1])
    note3 = int(notes[2])

    # Notların ortalamasını hesapla
    avarage = (note1 + note2 + note3) / 3

    # Ortalama not aralığına göre harf notunu belirle
    if avarage >= 90 and avarage <= 100:
        word = 'AA'
    elif avarage >= 85 and avarage <= 89:
        word = 'BA'
    elif avarage >= 80 and avarage <= 84:
        word = 'BB'
    elif avarage >= 75 and avarage <= 79:
        word = 'CB'
    elif avarage >= 70 and avarage <= 74:
        word = 'CC'
    elif avarage >= 65 and avarage <= 69:
        word = 'DC'
    elif avarage >= 60 and avarage <= 64:
        word = 'DD'
    elif avarage >= 50 and avarage <= 59:
        word = 'FD'
    else:
        word = 'FF'

    # Öğrenci ismi ve harf notunu döndür
    return studentName + ':' + word + '\n'

def read_averages():
    # 'exam_notes.txt' dosyasını oku ve her satır için ortalama notu hesapla
    with open('exam_notes.txt', 'r', encoding='utf-8') as file:
        for line in file:
            print(note_calculate(line))

def enter_note():
    # Kullanıcıdan öğrenci bilgilerini ve notlarını al
    name = input('Öğrenci Adı: ')
    surname = input('Öğrenci Soyadı: ')
    note1 = input('Not 1: ')
    note2 = input('Not 2: ')
    note3 = input('Not 3: ')
    
    # 'exam_notes.txt' dosyasına notları ekle
    with open('exam_notes.txt', 'a', encoding='utf-8') as file:
        file.write(name + ' ' + surname + ':' + note1 + ',' + note2 + ',' + note3 + '\n')

def record_notes():
    # 'exam_notes.txt' dosyasını oku ve her satır için ortalama notu hesapla
    with open('exam_notes.txt', 'r', encoding='utf-8') as file:
        list = []
        for i in file:
            list.append(note_calculate(i))
    
    # Hesaplanan notları 'results.txt' dosyasına yaz
    with open('results.txt', 'w', encoding='utf-8') as file2:
        for i in list:
            file2.write(i)

# Menü işlemleri için sonsuz döngü
while True:
    process = input('1- Notları Oku\n2- Not Gir\n3- Notları Kaydet\n4- Çıkış\n')

    if process == '1':
        read_averages()
    elif process == '2':
        enter_note()
    elif process == '3':
        record_notes()
    else:
        break