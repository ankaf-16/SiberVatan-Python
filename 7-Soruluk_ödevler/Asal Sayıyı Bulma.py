#ödev2 / ASAL SAYI BULMA.
def cegir():
    a = input("birinci sayıyı giriniz..: ")
    b = input("ikinci sayıyı giriniz..: ")

    if a < 2:
        return False
    for i in range(2, int(a**0.5) +1 ):
        if a % i == 0 :
            return False
    return True


cegir
    
#NOT

"""
YAPAMADIM
"""

