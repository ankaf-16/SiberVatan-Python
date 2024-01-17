
sayı1 = 42
sayı2 = -17
print(type(sayı1))
print(type(sayı2)) #sayı ne pozitif nede negatif olsun her şekilde "int" sonucu çıkarır.

#___________________________________________________________________________________________

sayı3 = 1.5
sayı4 = -5.5
print(type(sayı3))
print(type(sayı4)) # "float cıkar cevap"

#_____________________________________________________________________________________________

dogru_mu = True
yanlıs_mı = False
print(type(dogru_mu))
print(type(yanlıs_mı)) #cevap "bool" cıkar iki sonuçta da 

#________________________________________________________________________________________________


ondalık1 =  3.14
ondalık2 =  - 0.5

#________________________________________________________________________________________________

sayi_float = float(sayı1)
print("int to float", sayi_float)

sayı_int = int(ondalık1)
print("float to int",sayı_int)

#_________________________________________________________________________________________________

sayi_bool = int(dogru_mu)
print("bool to int" , sayi_bool)

print(type(sayi_bool))



#____________________________________________________________________________________________________


#input

# kullanıcı_ad = input("Lütfen Adınızı Girin:")
# print("Hoşgeldin",kullanıcı_ad) 

girilensayı = int(input("Lütfen Sayıyı Giriniz:"))
girilensayı2 = int(input("Lütfen İkinci Sayıyı Giriniz:")) #int ve input yerlerine dikkat et!!!

print(girilensayı + girilensayı2)


#farklı bir yöntem


sayı1 = input("sayı gir:")
sayı2 = input("ikinci sayı gir:")
print(int(sayı1)+int(sayı2))               # sonuç = 7'dir


#___________________________________________________________________________________________________

