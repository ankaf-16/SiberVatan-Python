"""
print("*-*-*-*-*-*-*-*-*HOŞGELDİN*-*-*-*-*-*-*-*-*")
print("*...MAAŞ ÖDEME SİSTEMİ...*")
print("kaç saat çalıştın?")
print("1 saat çalıştım...1'e basınız")
print("2 saat çalıştım...2'e basınız")
print("3 saat çalıştım...3'e basınız")
print("4 saat çalıştım...4'e basınız")
print("5 saat çalıştım...5'e basınız")
print("6 saat çalıştım...6'e basınız")
print("7 saat çalıştım...7'e basınız")
print("8 saat çalıştım...8'e basınız")
print("9 saat çalıştım...9'e basınız")
print("10 saat çalıştım...10'e basınız")
print("40 saat çalıştım...11'e basınız")

söylenen_saat = int(input("kaç saat çalıştın? : "))
kesin_maas = 500
def çalışma_saatti():
    if söylenen_saat == "1":
        sonuc = kesin_maas + 50
        print(sonuc)    
çalışma_saatti
"""


"""

def hasaplamasaati(toplam_çalışma_saati):
    saatlik_ücret = 50
    if toplam_çalışma_saati <= 40:
        maas = toplam_çalışma_saati * saatlik_ücret
    else:
        normal_calısma_saati = 40
        fazla_mesai_saati = toplam_çalışma_saati - 40
        maas = normal_calısma_saati * saatlik_ücret + fazla_mesai_saati * (saatlik_ücret * 1.5)
        return maas
    



    ...

"""



sicaklık_değerler_liteler = [5, -15, 25, 12, 2, 30, 18, -5, 35, -18, 8]
def sıcaklık_aralığı(sıcaklıkları):
    sıcaklık_aralıkları ={
        "(-20) - (0)" : 0,
        "(0) - (20)" : 0,
        "(20) - (40) " : 0
    }


for sıcaklık in sıcaklık_aralığı:
    if -20 <= sıcaklık < 0:
        sıcaklık_aralığı["-20 - (0)"] += 1

    elif 0 <= sıcaklık < 20:
        sıcaklık_aralığı["(0)- (20)"] +=1

    elif 20 <= sıcaklık < 40 :
        sıcaklık_aralığı["(20) - (40)"] += 1
    

for aralık,sayı in sıcaklık_aralığı.items():
    print(aralık,"arasındakı Sayı ", sayı,"bu kadar fark var ")

sicaklık_değerler_liteler = [5,-15,25,12,2,30,18,-5,35,-18,8]
sıcaklık_aralığı


#kod tamamlanmamış değildir.
