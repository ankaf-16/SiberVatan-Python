import re 

def parola_kontrol(parola):
    if len(parola)< 8:
        raise Exception("parola en az 8 karakterden oluşmalı...")
    elif not re.search("[a-z]", parola):
        raise Exception("PAROLA KÜCÜK HARF İÇERMELİDİR...")
    elif not re.search("[A-Z]", parola):
        raise Exception("PAROLA BÜYÜK HARF İÇERMELİDİR...")
    elif not re.search("[0-9]", parola):
        raise Exception("PAROLA SAYI İÇERMELİDİR...")
    elif not re.search(r"[^\w\s]" , parola ):
        raise Exception("PAROLADA ÖZEL KARAKTER BULUNMALI...")
password = "12345678Aa12@"
try:

    parola_kontrol(password)

except Exception as ex:
    print(ex)

else:
    print("parola oluşturma başarılı...")