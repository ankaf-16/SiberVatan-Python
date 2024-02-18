#open("yeni_dosya.txt", "w")

# "w" Write => Yazma Modu , yoksa oluşturur içeriyi silip ekler.

# "a" Append => Ekleme Modu 

# "x" Create => Oluşturma Modu , aynısı varsa hata verir

# "r" Read => Okuma Modu

file = open("Yeni_dosya.txt", "w")
print(file)
file.close()

file_dizin = open("C:/Users/acer/OneDrive/Masaüstü/yenidosya" , "w")
file_dizin.close()

file = open("Yeni_dosya.txt", "w" , encoding= 'utf-8')
file.write("ABDÜRĞHMAN")
file.close()
file = open("Yeni_dosya.txt", "a", encoding='utf-8')
file.write("\nYUNUS EMTRE")
file.close()

file = open("Yeni_dosya2.txt" , "x")




try:
    print(file)
    file.write("2334")
   # file.close()


except FileNotFoundError:

    print("birşey hatası")
    print("dosya kapatıldı")

finally:
    print("dosya oluştu...")




#file = open("Yeni_dosya.txt" , "r" , encoding='utf-8')

file.write("yunus")
file = open("Yeni_dosya.txt", "r", encoding='utf-8')
file.write("\nYUNUS EMTRE")

for i in file:
   print(i,end="")

icerik = file.read()
print(icerik)

icerik_karakteri = file.read(0)
icerik_karakteri = file.read(17)
print(icerik_karakteri)

# print(file.readline(), end="")
# print(file.readline(),end="")


# liste = file.readlines()
# print(liste)
# print(liste [0])
# print(liste [1])
# file.close
with open("Yeni_dosya.txt", "w" , encoding='utf-8') as file: 
    file.write("jffjhfhgfhgfgfjhfjhfjhfjfjfjffjfjfjgfgffjfjgj")
with open("Yeni_dosya.txt", "r" , encoding='utf-8') as file: 
    content = file.read()
    print(content)
    file.seek(10)
    print(file.tell())
    content2 = file.read()
    print(content2)



with open("Yeni_dosya.txt" , "r+" , encoding='utf-8') as file:

    file.seek(15)
    file.write("-Siber-Vatan-")




citylist= ["Karabük\n", "Bayburt\n" , "izmir\n"]
with open("yenidosya.txt", "a" , encoding="utf-8") as file:
    file.write(citylist[0])
    file.write(citylist[1])
    file.write(citylist[2]) #basit yolu...



citylist= ["Karabük", "Bayburt" , "izmir"]
index = 1
with open("yenidosya.txt", "a" , encoding="utf-8") as file:
    for i in citylist:
        if index == len(citylist):
            file.write(i)

        else:
            file.write(i+'\n')
        index+=1


import math as islem 

sonuc = islem.factorial(5)

print(sonuc)





from math import *

print(factorial(5))
print(sqrt(5))
print(factorial(5))



import random 

sayılar = [0,1,2,3,4,5,6,7,8]
liste = " "
i=0
while i != 6:
    
    liste+=str(sayılar[random.randint(0,len(sayılar)-1)])
    i+=1

print(liste)



import random 

sayılar = [0,1,2,3,4,5,6,7,8]
liste = " "
i=0
while i != 6:
    
    liste+=str(random.choice(sayılar)) 
    i+=1

print(liste)


import random 

sayılar = [0,1,2,3,4,5,6,7,8]
liste =[]
i=0
while i != 6:
    
    liste.append(random.choice(sayılar)) 
    i+=1

print("Before Shuffle")
print(list)
random.shuffle
print("After Shuffle")
print(liste)






import sibervatan

sayı = sibervatan.sayılar[2]
print(sayı)


sayı2 = sibervatan.numara
print(sayı2)