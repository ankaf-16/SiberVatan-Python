"""
meyveler = ["elma", "kivi", "limon" ,"böğürtlen"]
print(meyveler[2])
print(meyveler[:4])

sayılar = [10,20,30,40,50]

sayılar[0]=+sayılar[1]
sayılar[0]=+sayılar[2]
sayılar[0]=+sayılar[3]

toplam =0

for sayı in sayılar:
    toplam +=sayı

print(toplam)

meyveler = ["elma", "kivi", "limon" ,"böğürtlen"]

for meyve in meyveler:
    print(meyve)

"""
"""
sayılar = [1,3,4,6,9,2,567,8,10,234]
for sayı in sayılar:
    if sayı %2 == 0 :
        print("TEK OLAN:",sayı)

    else:
        print("ÇİFT OLAN", sayı)


sayı =  int(input("BİR SAYI GİRİNİZ: "))

sayac = 0

while sayac<sayı:
    print(sayac)
    sayac+=1

"""
bos_liste = [ ]
i = 5
while i < 5:

  sayı = int(input("1.sayıyı giriniz"))
  bos_liste.append(sayı)
  i+=1
print(bos_liste)
