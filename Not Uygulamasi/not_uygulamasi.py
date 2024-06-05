def note_calculate(line):
    line = line [:-1]
    list =line.split(':')

    studentName = list[0]
    notes =list[1].split(',')

    note1 =int(notes[0])
    note2 =int(notes[1])
    note3 =int(notes[2])

    avarage = (note1+note2+note3)/3


    if avarage >=90 and avarage<=100:
        word='AA'
    elif avarage>=85 and avarage<=89:
        word='BA'
    elif avarage>=80 and avarage<=84:
        word='BB'    
    elif avarage>=75 and avarage<=79:
        word='CB'
    elif avarage>=70 and avarage<=74:
        word='CC'
    elif avarage>=65 and avarage<=69:
        word='DC'
    elif avarage>=60 and avarage<=64:
        word='DD'    
    elif avarage>=50 and avarage<=59:
        word='FD'
    else:
        word='FF'
    return studentName+':'+word+'\n'
    
    
 





def read_averages():
   with  open('exam_notes.txt','r',encoding='utf-8')as file :
        for line in file :
            print(note_calculate(line))
    

def enter_note():
    name  = input('Ogrenci Adi: ')
    surname  = input('Ogrenci Soyadi: ')
    note1 = input('Note 1: ')
    note2 = input('Note 2: ')
    note3 = input('Note 3: ')
    # a kipiyle dosya olusturmada eger dosta var ise eklenmeyecek yok ise eklenerek devam edicek
    # w kipiyle dosya olusturmada onceki dosyalari silerek yenisi eklencek
    with open('exam_notes.txt','a',encoding='utf-8') as  file:
        file.write(name+' '+surname+':'+note1+','+note2+','+note3+'\n')






def record_notes():
    with open('exam_notes.txt','r',encoding='utf-8')as file:
        list= []

        for i in file :
            list.append(note_calculate(i))

        with open('results.txt','w',encoding='utf-8')as file2:
            for i in list:
                file2.write(i)




while True:
    process = input('1- Notlari Oku\n2- Not Gir\n3- Notlar Kayit Et\n4- Cikis\n ' )

    if process == '1':
        read_averages()
    elif process == '2':
        enter_note()
    elif process =='3':
        record_notes()
    else:
        break