#ödev2 / ASAL SAYI BULMA. list1 [10,15,20] / list2 [5,100,250]


def enBüyük(liste1):
    if liste1:
        return max(liste1)
    
    return

def enKüçük(liste2):
    if liste2:
        return min(liste2)
    
    return

liste1 = [10,15,20]
liste2 = [5,100,250]

en_buyuk = enBüyük(liste1)
en_kücük = enKüçük(liste2)

print(en_buyuk + en_kücük)