from pytube import YouTube
from pytube import Playlist
import time

# Video bilgilerini gösteren fonksiyon
def bilgileri_göster():
    url = YouTube(input("Lütfen Bilgilerini Görmek İstediğiniz Linki Yapıştırınız:"))
    son_dakika = url.length / 60
    print("*" * 45)
    print('Video Başlığı:', url.title)
    print('Videonun Sahibi:', url.author)
    print("Videonun Küçük Resmi:", url.thumbnail_url)
    print("İzlenme Sayısı:", url.views)
    print("Video Uzunluğu:", son_dakika, "dakika")
    print("*" * 45)

# Video indiren fonksiyon
def video_indir():
    url = YouTube(input("Lütfen İndirilecek Video Linkini Yapıştırınız:"))
    son_dakika = url.length / 60

    indirme_baglantisi = url.streams.filter(progressive='True').first()
    indirme_baglantisi.download()
    print("*" * 45)
    print('Video Başlığı:', url.title)
    print('Videonun Sahibi:', url.author)
    print("İzlenme Sayısı:", url.views)
    print("Video Uzunluğu:", son_dakika, "dakika")
    print("*" * 45)

# Ses indiren fonksiyon
def ses_indir():
    url = YouTube(input("Lütfen İndirilecek Ses Linkini Yapıştırınız:"))
    son_dakika = url.length / 60

    indirme_baglantisi = url.streams.filter(mime_type="audio/mp4").first()
    indirme_baglantisi.download()
    print("*" * 45)
    print('Ses Başlığı:', url.title)
    print('Ses Sahibi:', url.author)
    print("İzlenme Sayısı:", url.views)
    print("Ses Uzunluğu:", son_dakika, "dakika")
    print("*" * 45)

# Playlist indiren fonksiyon
def play_listIndir():
    playlist_url = input("Lütfen İndirilecek Playlist Linkini Yapıştırınız:")
    p1 = Playlist(playlist_url)

    i = 0

    for video_url in p1.video_urls:
        i = i + 1
        yt = YouTube(video_url)
        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        video.download(f'Videos/{yt.author}')
        print('İndirildi !!', i)
    print('Hepsi İndirildi....')

# Ana menü
while True:
    sec = input('1-Youtube Video Bilgilerini Göster\n2-Video İndir \n3-Ses İndir\n4-Playlist İndir \n5-Çıkış..\n')

    if sec == '1':
        bilgileri_göster()
        input('Devam Edilsin mi ?')
    elif sec == '2':
        video_indir()
        input('Devam Edilsin mi ?')
    elif sec == '3':
        ses_indir()
        input('Devam Edilsin mi ?')
    elif sec == '4':
        play_listIndir()
        input('Devam Edilsin mi ?')
    elif sec == '5':
        print('Çıkış Yapılıyor...')
        print('5')
        time.sleep(1)
        print('4')
        time.sleep(1)
        print('3')
        time.sleep(1)
        print('2')
        time.sleep(1)
        print('1')
        time.sleep(1)
        print('Uygulamadan Çıkıldı...')
        break
    else:
        print('Geçersiz bir değer girdiniz...')