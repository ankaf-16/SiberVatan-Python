
a = 90
b="SiberVatan"

num1,num2,num3= 55,55,65
print("Sayılar", num1, num2, num3)

num1=num1+50
num2=num2+50
num3=num3+90

num1/=num2



numara =(50,55,66)
#print(type(numara))
num1,num2,num3 = numara
#print(num4) hata veriri


a,b,c,d = 50,100,50,75

sonuc=(a>b)
print(sonuc)
sonuc=(a==c)
print(sonuc)
sonuc=(a>d)
print(sonuc)
sonuc=(a!=c)
print(sonuc)


unsername1 = "ceku"
unsername2= "arif"

print("A.R.O.G'a Hoş Geldiniz...\n")

unsername_input =input("KULANICI ADI GİRİNİZ:\n ")

#sonuc = (unsername1 == unsername_input == print(unsername1 == unsername_input), print(unsername2 == unsername_input))

sonuc = (unsername1.lower()==unsername_input.lower())
sonuc2 = (unsername2.lower()==unsername_input.lower())

sonuc3 = (sonuc != sonuc2)

print(sonuc3)




print("'CEKU'EŞLEŞME SONUCU...",sonuc)

sonuc = (unsername2==unsername_input)

print("'ARİF'EŞLEŞME SONUCU...",sonuc)


#________________________________________denemeler

kullanıcı1 = "elon" 
kullanıcı1sifre = "tesla"
kullanıcı_bilgisi1 = input("lütfen kullanıcı adı giriniz: "), input("lütfen şifre giriniz:")
sonuc = (kullanıcı1== kullanıcı_bilgisi1)
sonucsifre = (kullanıcı1sifre==kullanıcı_bilgisi1)
print("kullanıcı adı",sonuc)
print("kullanıcı şifresi", sonucsifre)


kullanıcı1_email , kullanıcı1_şifre = "babapro.com" , "babapro"

girilen1email = input("lütfen email giriniz: ")
girilen1şifre = input("lütfen şifre giriniz: ")

gmail_sonuc =( kullanıcı1_email == girilen1email)
şifre_sonuc =(kullanıcı1_şifre == girilen1şifre)
print(gmail_sonuc == şifre_sonuc)

#_________soru sonucu

users = {
    "babapro@gmail.com" : "babapro",
    "kalemtutan@gmail.com" : "kalem"
}
print("lütfen bilgilerinizi giriniz: \n")

input_mail = input("mail giriniz: ")
input_şifre = input("şifre giriniz: ")

sonuc_mail = (input_mail in users.keys())
sonuc_şifre = (input_şifre in users.values())
sonuc_finali = (int(sonuc_mail)+int(sonuc_şifre) )== 2
print("eşleşme sonucu: ",sonuc_finali)


meyveler = ["elma", "muz", "portakal","kivi"]
print("muz" in meyveler)
print("kiraz" in meyveler)   #-in- kodu mesela, "meyveler içide varmı" in oporotörü karşılaştırma oporotör



x = y =[10,20,30]
z = [10,20,30]
print(x is y)
print(x == z)


birinci_sınav_notu = int(input("Vize Notunuzu Giriniz: "))
final_notu = int(input("LÜTFEN FİNAL NOTUNUZU GİRİNİZ: "))

ortalama = birinci_sınav_notu * 0.4 + final_notu*0.6
print("ORTALAMAN", ortalama)
print("sınavdan kalma durumun: ", ortalama > 50)


girilen_sayı = int(input("LÜTFEN BİR SAYI GİRİNİZ: "))

cıkan_sonuc = (girilen_sayı > 0) and (girilen_sayı % 2 == 0)
print("GİRİLEN SAYI ÇİFT SAYIMI: " + str(cıkan_sonuc))


x = 98
y = 98
if (x > y):
    print("EN BUYUK SAYI: ",x )
elif (x==y):
    print("SAYILAR EŞŞİTİR ")


else:
    print("EN BÜYÜK SAYI: ", y )

kullanıcı_takım =input("TAKIM ADI GİRİNİZ: ")
if kullanıcı_takım == "Galatasaray" :
    print("EN SEVDIĞINIZ RENKLER : SARI-KIRMIZI")
elif kullanıcı_takım== "FENERBAHCE" :
    print("EN SEVĞİN RENKLER: SARRI-LACIVERT")
elif kullanıcı_takım == "Karabükspor":
    print("EN SEVĞİN RENKLER: SARRI-LACIVERT")



kullanıcı_adı = "babapro"
kullanıcı_şifre = "babapro78"
girilen_kullanıcı = input("lütfen kullanıcı adı giriniz: ")
girilen_şifre = input("lütfen şifrenizi giriniz: ")
if girilen_kullanıcı == kullanıcı_adı and girilen_şifre == kullanıcı_şifre :
    print("giriş onaylandı")

elif kullanıcı_şifre == girilen_şifre :
    print("şifre hatalı") 

else :
    kullanıcı_adı == girilen_kullanıcı 
    print("kullanıcı adı yanlış")

#CALIŞIYORSA DOKUNMİYORUM...


print("*-*-*-*-*-*-*-*-*HOŞGELDİNİZ*-*-*-*-*-*-*-*-*")

sayı_1 = int(input("1. Sayıyı Giriniz..: "))
sayı_2 = int(input("2.Sayıyı Giriniz..:"))

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

else :
    print("hesaplama hatası yada başka bir işlem...")

print("işleminizin sonuçu: ", sonuç )
