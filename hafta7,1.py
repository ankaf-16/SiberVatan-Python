"""
def selamdunya():
    print("Hello World")

selamdunya()


selamdunya()
"""

#___________
"""
#benim yaptığım

def hosgeldin(name):
    print("HOŞGELDİNİZ!: "+ name)

     #input("isminizi giriniz: ")

hosgeldin(input("isminizi giriniz:")) 

#hocanın yapyığı

def selamVer(isim):
    print("hosgeldin: " + isim)

selamVer(input("isminizi giriniz: "))
"""
#____________________________________________________________________________________
"""
def fonksiyon(sehir = "karabük"):
    print("en sevdiğim şehir: " + sehir)

fonksiyon("istanbul")
fonksiyon()

def sayı(x):
    x = x+5
    return x 

sonuc = sayı(10)
print(sonuc)

"""
#_________________________________________________
"""
def sayı1(x,y):
    v = x+y    
    return v

sonuc = sayı1(1,1) 

print(sonuc)
"""
"""
def fonk_tuple(*argv):
    for arg in argv:
        print(arg)

fonk_tuple("SELAM", "NABER", "NASILSIN", "İYİDİR")

"""





def toplama(x, y):
    return x + y

def cikarma(x, y):
    return x - y

def carpma(x, y):
    return x * y

def bolme(x, y):
    if y == 0:
        return "Tanımsız"
    else:
        return x / y
    
def faktoriyel(n):
    faktoriyel = 1
    for i in range(1, n+1):
        faktoriyel *= i
    return faktoriyel

while True:
    
    print("*-*-*-*-*-*-*-*-*HOŞGELDİNİZ*-*-*-*-*-*-*-*-*")
    print("TOPLAMA İÇİN - 1..")
    print("ÇIKARTMA İÇİN - 2..")
    print("ÇARPMA İÇİN - 3..")
    print("BÖLME İÇİN - 4..")
    print("ÇIKIŞ İÇİN İSE 5'E BASINIZ..")
    print("6.Faktoriyel")

    secim = input("Tercih yapınız : ")

    if secim == '6':
        print("Çıkılıyor...")
        break

    sayı1 = int(input("Birinci sayıyı giriniz :"))

    sayı2 = float(input("İkinci sayıyı giriniz :"))

    if secim == "1" :
        print("Sonuç",toplama(sayı1,sayı2))    
    elif secim == "2" :
        print("Sonuç",cikarma(sayı1,sayı2))
    elif secim == "3" :
        print("Sonuç",carpma(sayı1,sayı2))
    elif secim == "4" :
        print("Sonuç",bolme(sayı2,sayı2))    
    elif secim == "5":
        print("Sonuc",faktoriyel(sayı1))
    else:
        print("Sayı girişi yanlış")
















"""
def cift_sayı(x):
    bos_liste = [ ]
    for x in range(0,10,2):
        bos_liste.append(x)
    return bos_liste

alınan_sayı = input("sayı giriniz : ")
bos_liste2 = cift_sayı(alınan_sayı)
print(bos_liste2)


def toplam(sayı_1,sayı_2):
    return sayı_1+sayı_2
def cıkarma(sayı_1,sayı_2):
    return sayı_1 - sayı_2
def carpma(sayı_1,sayı_2):
    return sayı_1 * sayı_2
def bolme(sayı_1,sayı_2):
    return sayı_1 / sayı_2
def fakoroel(sayı_1):
    


def devam_etsinMi 
while(devam_etsinMi):
 

    print("*-*-*-*-*-*-*-*-*HOŞGELDİNİZ*-*-*-*-*-*-*-*-*")

    sayı_1 = float(input("1. Sayıyı Giriniz..: "))
    sayı_2 = float(input("2.Sayıyı Giriniz..:"))

    print("TOPLAMA İÇİN - 1..")
    print("ÇIKARTMA İÇİN - 2..")
    print("ÇARPMA İÇİN - 3..")
    print("BÖLME İÇİN - 4' E BASINIZ...")

    seçim = input("LÜTFEN İŞLEMİNİZİ SEÇİNİZ..: ")
    if seçim == "1":
        sonuç = sayı_1+sayı_2
    elif seçim == "2" :
        sonuç = sayı_1-sayı_2
    elif seçim == "3":
        sonuç = sayı_1*sayı_2
    elif seçim == "4":
        sonuç = sayı_1/sayı_2
    elif seçim == "6":
        sonuç = 
        

    else :
        print("hesaplama hatası yada başka bir işlem...")

print("işleminizin sonuçu: ", sonuç  )

"""