import requests  # HTTP isteklerini yapmak için kullanılır
import json  # JSON verilerini işlemek için kullanılır

# API anahtarınızı buraya yerleştirin
api_key = 'efa6937ab9bc45d176e3788e'

# API URL'sini oluşturun
api_url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/'

# Kullanıcıdan dönüştürülecek döviz türünü alın (ör. USD)
converted_money = input('Dönüştürülen döviz türü: ')  # Örnek: USD

# Kullanıcıdan alınacak döviz türünü alın (ör. TRY)
received_money = input('Alınan döviz türü: ')  # Örnek: TRY

# Kullanıcıdan dönüştürülecek miktarı alın
miktar = int(input(f'Ne kadar {converted_money} dönüştürmek istiyorsunuz: '))  # Örnek: Ne kadar USD

# API'den döviz kurlarını almak için istek gönderin
result = requests.get(api_url + converted_money)

# API'den gelen yanıtı JSON formatında ayrıştırın
result_json = json.loads(result.text)

# Döviz kurunu hesaplayıp sonucu yazdırın
print('{0} {1} = {2} {3}'.format(miktar, converted_money, miktar * result_json['conversion_rates'][received_money], received_money))