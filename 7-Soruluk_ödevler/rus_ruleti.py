#ödev7 RUS RULETİ

import random
print("*-*-*-*-*-*-*RUS RULETİ OYUNUNA HOSGELDİNİZ*-*-*-*-*-*-*")
print("OYUN NASIL OYANIR?")
print("1 ila 6 arasında bir sayı tutulur. eğer o sayıyı secerseniz drekt tahtalı köye")
def rasgelesayı():

    return random.randint(1,6)

def oyun():
    kursun = rasgelesayı()
   # print(kursun) #isterseniz burayı aÇın

    while True:
        kullamıcıdanalınansayı = int(input("sec: "))

        if kullamıcıdanalınansayı == kursun:
            print("öldün cık ")
            break
        else:
            print("yasadın")
            

oyun()


""" 
#benimde anlamdığım bir kod owpragjwerggwbtıwrğtb

def oyun():
    print(rasgelesayı())
    rasgelesatıseç = rasgelesayı()

    while True:
        kullanıcıdanalınansayı = int(input("seç2: "))


        if kullanıcıdanalınansayı != rasgelesatıseç:
            print("öldün")
            break
        elif kullanıcıdanalınansayı == rasgelesatıseç:
            print("yasadın")
            break


oyun()
"""
