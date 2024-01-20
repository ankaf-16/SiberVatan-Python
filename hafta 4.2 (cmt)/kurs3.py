
ad = "Yunus Emre "
soyAd = "Tepeli "
Yas = str(15)

karsilama = "Benim Adım: " + ad + "Soyadım: " + soyAd + 'Yaşım ' + Yas +  ' Hoşgeldin'
print(karsilama)

uzunluk = len(karsilama)
#print(uzunluk , "Harf Vardır") #len komutunu unutma !!!! "bu komutta kaç harf vs. onları gösterir"

print(karsilama[-1]) # sonuc "n" çıkar 
print(uzunluk-1)

print(karsilama[37:56])          # sonuç = "i Yaşım 15 Hoşgeldi" çıkar / burdaki 37 sayısı cümlenin başlama yeridir 56 sayısı ise cumlenin nerde bitiğini gostermektedir.

print(karsilama[0:10])  # sonuç = "Benim Adım" çıkar.

print(karsilama[:22]) # sonuç = "Benim Adım: Yunus Emre" sonuçu çıkar
print(karsilama[23:]) # sonuç = "Soyadım: Tepeli Yaşım 15 Hoşgeldin" sonuçu cıkar. (neden 22 değil, çünkü 22 de boşluk ( ) var o sebebten direkt cumleden başlar.)


print(karsilama[:-3]) #sonuç = "Benim Adım: Yunus Emre Soyadım: Tepeli Yaşım 15 Hoşgel" çıkar
print(karsilama[::-1]) #sonuç = "nidlegşoH 51 mışaY ilepeT :mıdayoS ermE sunuY :mıdA mineB" çıkar.

karsilama_upper = karsilama.upper()
print(karsilama_upper) 

karsilama_lower = karsilama.lower()
print(karsilama_lower)

karsilama_split = karsilama.split()
print(karsilama_split)
print((karsilama_split)[-1])

# 40 58

print((karsilama_split)[7]) #küme şeklinde ayrılılır.

karsilama_join = "-".join(karsilama)
print(karsilama_join)

karsilama_find = karsilama.find("Yunus")
print(karsilama_find) # ne zaman başladığını söyler.

karsilama_startwith = karsilama.startswith('A')
print(karsilama_startwith)

karsilama_startwith = karsilama.startswith('n')
print(karsilama_startwith)

karsilama_replace = karsilama.replace('Yunus', 'Te')
print(karsilama_replace)


