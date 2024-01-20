
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



_________________________________________________________





liste = [1,2,3,4,5]
print(liste)
print(liste[4])
print(type(liste))

liste[3] = 100
print(liste[3])
print(liste) #sonuç "[1, 2, 3, 100, 5]" çıkar

alt_liste = liste[2:4]
print(alt_liste)

#tuple 

tuple = (10,20,30,40,50,60)
print(tuple)
print(tuple[1])



tuple[1] = 300
print(tuple) #hata verir
alt_tuple = tuple[1:4]
print(alt_tuple) # çıktı = (20, 30, 40)



#kümeler (set) diye de gecebilir.  -print(type(kume))-

kume = {100,200,300,400,500}
print(type(kume))
print(kume)
kume.add(700)

print(kume)
kume.update([400,900])
print(kume)

#dict dictionary (sözlük)

dict = {"anahtar1": "deger1" , "anahtar2" : "deger2"}
print(dict)

deger = dict["anahtar1"]
print(deger)

kume_list = list(kume)
print(kume_list)
print(type(kume_list))

list_keys = list(dict.keys())
print(list_keys)

list_values = list(dict.values())
print(type(list_values))
print(list_values)

sayılar =  [10,8,5,3,15,10]

en_buyuk = max(sayılar)
en_kucuk = min(sayılar)

print(en_buyuk)
print(en_kucuk)

sayılar.append(20)
sayılar.append(99)

yeni_en_buyuk = max(sayılar)
yeni_en_kucuk = min(sayılar)

print(yeni_en_buyuk)
print(yeni_en_kucuk)
print(sayılar)

sayılar.pop()
print(sayılar)

sayılar.sort()
print(sayılar)

sayılar.reverse()
print(sayılar)

print(sayılar.count(10))


aralık = range(1,100)
print(list(aralık))

import random

rasgele_sayı = random.randint(1,100)
print("tutulan sayı", rasgele_sayı)

