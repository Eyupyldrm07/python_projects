from pytube import YouTube
from pytube import Playlist



def bilgileri_göster():
    url = YouTube(input("Lütfen Bilgilerini Görmek İstediğiniz Linki Yapıştırınız:"))
    son_dakika=url.length/60
    print("*"*45)
    print('Video Basligi:',url.title)
    print('Videounun Sahibi:',url.author)
    print("Vıdeounun Kucuk Resmı:",url.thumbnail_url)
    print("Izlenme Sayısı:",url.views)
    print("Vıdeo Uzunluğu:",son_dakika,"dakika")
    print("*"*45)

def video_indir():
   url = YouTube(input("Lütfen Indirilecek Video Linkini Yapistiriniz:"))
   son_dakika=url.length/60

   indirme_baglantisi = url.streams.filter(progressive='True').first()
   indirme_baglantisi.download()
   print("*"*45)
   print('Video Basligi:',url.title)
   print('Videounun Sahibi:',url.author)
   print("Izlenme Sayısı:",url.views) 
   print("Vıdeo Uzunluğu:",son_dakika,"dakika")
   print("*"*45)



def ses_indir():
    url = YouTube(input("Lütfen Indirilecek Ses Linkini Yapistiriniz:"))
    son_dakika=url.length/60

    indirme_baglantisi=url.streams.filter(mime_type="audio/mp4").first()
    indirme_baglantisi.download()
    print("*"*45)
    print('Ses Basligi:',url.title)
    print('Ses Sahibi:',url.author)
    print("Izlenme Sayısı:",url.views) 
    print("Ses Uzunluğu:",son_dakika,"dakika")
    print("*"*45)



def play_listIndir():
    playlist_url = input("Lütfen Indirilecek Playlist Linkini Yapistiriniz:")
    p1 =Playlist(playlist_url)

    i = 0
  
    for video_url in p1.video_urls:
        i =  i + 1
        yt=YouTube(video_url)
        video = yt.streams.filter(progressive=True,file_extension='mp4').order_by('resolution').desc().first()
        video.download(f'Videos/{yt.author}')
        4
        print('Indirildi !!',i) 
    print('Hepsi Indirildi....')
    

 

  
while True:
    sec  = input('1-Youtube Video Bilgilerini Goster\n2-Video indir \n3-Ses indir\n4-Playlist Indir \n5-Cikis..\n')

    if sec == '1':
        bilgileri_göster()
        input('Devam Edilsin mi ?')
    elif sec=='2':
        video_indir()
        input('Devam Edilsin mi  ?')
    elif sec=='3':
        ses_indir()
    elif sec=='4':
        play_listIndir()
        input('Devam Edilsin mi  ?')
    elif sec=='5':
        print('Cikis Yapiliyor...')
        print('5')
        time.sleep(1)
        print('4')
        time.sleep(1)
        print('3')
        time.sleep(1)
        print('2')
        time.sleep(1)
        print('1 ')
        time.sleep(1)
        print('Uygulamadan Cikildi...')
        break
    else:
        print('gecersiz bir deger girdiniz....')


    




