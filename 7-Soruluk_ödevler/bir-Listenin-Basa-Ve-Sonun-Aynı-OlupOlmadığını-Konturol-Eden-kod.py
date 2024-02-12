#ödev4 / BİR FONKSİYON İÇİNDEKİ LİSTENİN İLK VE SON SAYILARI EŞİTSE TRUE DEĞİSE FALSE YAZDORAN KOD.


def ucak(liste1):
    if liste1[0] == liste1[3]:
        print("true")

        
    elif liste1[0] != liste1[3]:
        print("false")

    return

liste = [25,6,2009,25]

liste2 = ucak(liste)

print(liste2)


# İLK BAŞTA BU KODU YAZDIM... BANA CIKTI OLARAK "true, None" SONUCUNU VERDİ AMA CAH-...
#T CPT YE SORDUM "UA BU KOD BANA NDEN EKSTRA None SONUCU VERDİ?" DEDİM ODA BANA DEDİKİ 
#Bu kodunuzda, ucak fonksiyonu hiçbir şey döndürmüyor (veya daha spesifik olarak None döndürüyor). Bu nedenle, ucak(liste) çağrısı sonucunda liste2 değişkeni None olacaktır.
#DEDİ
#BENDE HATAMI GÖRÜP DEĞİŞTİRDİM



#DEĞİŞTİRDİĞİM KOD AŞAĞİDADIR.


"""
def ucak(liste1):

    if liste1[0] == liste1[3]:

        return True
        
    elif liste1[0] != liste1[3]:

        return False

liste = [25, 6, 2009, 25]



liste2 = ucak(liste)



print(liste2)
"""