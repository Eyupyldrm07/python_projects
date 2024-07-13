sampleString= 'Python is general purpose programming language'
print(len(sampleString))


print(sampleString.upper())  #Cumleyi buyutmek icin kullanilir
print(sampleString.lower())  #Cumleyi kucultmek icin kullanilir
print(sampleString.title())  #Ilk harfi buyulur
print(sampleString.find('p')) #bulunduhu index bulur yoksa =1 doner
print(sampleString.rfind('p')) #bulunduhu index bulur yoksa =1 doner
print(sampleString.replace('general purpose','high level'))  #Cumle icerisinde kelime veya cumle degisikligi yapmak icin kullaniliriz


print('Python' in sampleString) #Icersinde olup olmadigini kontrol eder 
print('jython' in sampleString)
print(sampleString.count('p'))  #icerisinde kac tane bulundugunu bulur