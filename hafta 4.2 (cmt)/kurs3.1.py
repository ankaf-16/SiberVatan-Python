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

