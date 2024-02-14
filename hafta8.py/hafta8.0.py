"""
def faktoriyel(n):
    if n  == 0:
        return 1 
    
    else:
        return n * faktoriyel(n-1)
    
sayı = 4
print(faktoriyel(sayı))


x = "global değişken"

def fonksiyon():
    x = "local değişken"
    print(x)
fonksiyon()
print(x)

#ilk önce x'e g.d denımışız ama kodumuz fonksiyona girdiği için ve fonksiyon un içine bir şey tanıkmılşız ve fonksiyondan cıkıp İLK ÇNCE FONSİYON U CAĞIRMIŞIZ VE SONRA İLK BAŞLAIĞIMIZ X İ YAZDIRMIŞIZ.

x = "global değişken"

def fonksiyon():
    x = "local değişken"
    print(x)
fonksiyon()
print(x)
"""
#print(a) #NameError / Ad Hatası

#int("a19") ValueError / Değer Hatası

#print(10/0)  ZeroDivisionError: / sıfıra bölünme hatası


#print("hello"world) #SyntaxError / Sözdizimi hatası

"""
try:


    print(x/y)
#except ZeroDivisionError:
    print("sıfıra bölünme hatası...")



except ValueError:
   # print("x ve y için sayısal veri giriniz...")
    
    
except Exception as ex:
            print("bilgiler yanlış ", ex)



while True:
    try:
    

        print(x/y)

    except Exception as ex: 
        print("bilgiler yanlış ", ex )

    else:
        break
    finally:
        print("her şey yolunda...")



try:
    x = int(input("x giriniz: " ))
    y = int(input("y giriniz: "))
    print(x/y)

except NameError:
    print("ad hatası ")

except ZeroDivisionError:
    print("sıfıra bölünme hatası")

except ValueError:
    print("Değer Hatası")

except SyntaxError:
    print("Sözdizimi hatası")

"""
import re

def parola_kontrol(parola):
    if len(parola)< 8:
        raise Exception("parola en az 8 karakterden oluşmalı...")
    elif not re.search("[a-z]", parola):
        raise Exception("PAROLA KÜCÜK HARF İÇERMELİDİR...")
    elif not re.search("[A-Z]", parola):
        raise Exception("PAROLA KÜCÜK HARF İÇERMELİDİR...")
    elif not re.search("[0-9]", parola):
        raise Exception("PAROLA KÜCÜK HARF İÇERMELİDİR...")
    
password = "123aA"
try:

    parola_kontrol(password)

except Exception as ex:
    print(ex)

else:
    print("parola oluşturma başarılı...")




