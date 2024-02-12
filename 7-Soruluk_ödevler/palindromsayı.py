#ödev5 / Bir sayının palindrom sayı olup olmadığını kontrol eden kod.

def palindrom(sayı):
    sayı_str = str(sayı)

    sayı = sayı_str[::-1]

    if sayı_str == sayı:
        return True
    else:
        return False
sayı = int(input("lütfen palindrom bir sayı giriniz..: "))

print(palindrom(sayı))

