
"""
def sayıKontrol(sayı):
    rakam_str = str(sayı)
    if len(set(rakam_str)) == 1:
        return 1
    else:
        return 0
    

a = [233,45,777,81,99999,36,90,88,11,61]
for sayı in a:
    if sayıKontrol(sayı):
        print(f"{sayı}: basamakları eş")

    else:
        print(f"{sayı}: basamkları eş değil")
---------------------------------------------
cıktı:

233: basamkları eş değil
45: basamkları eş değil
777: basamakları eş
81: basamkları eş değil
99999: basamakları eş
36: basamkları eş değil
90: basamkları eş değil
88: basamakları eş
11: basamakları eş
61: basamkları eş değil



#------------------------------


liste = [10,20,30]
print(type(liste))


class Person:
    address = "biligi yoğk"
    def __init__(self,name,lname,dy):
        self.name = name
        self.lname = lname
        self.dy = dy

    def intro(self):
        print(f"merhaba ben   {self.dy}")

    def yas(self):
        print(2024 - self.dy)




p1 = Person("Mert", "Yılmaz",dy=int( "1992")) #twich <3
p2= Person("FULYA","REYİZ",dy=int("1944"))
print(p1)

print("ismim",p2.name,"soyisim",p2.lname)
p1.intro()
print("benim adım/Address: ", p2.name,"soyadım", p2.lname, "adresim", p1.address,"yaşım'kesinlıkle doğru'", p2.yas)
#cıktı: "benim adım/Address:  Mert soyadım Yılmaz adresim biligi yoğk"
p2.intro()
p1.yas()
#self3 = p1 , p2

#print(self3)

"""




class Daire:
    pi = 3.1415
    def __init__(self,ycap):
    
        self.ycap = ycap
    def cevre(self):
        print(2*self.pi*self.ycap)

    def alan(self):
        print(self.pi*(self.ycap*self.ycap))

anka1 = Daire(ycap=1)

anka1.cevre()
#_______________------__---____--_____-_____-___--__-__
class Square:
    def __init__(self,akare):
        self.akare = akare

    def k_alan(self):

        print(self.akare * self.akare)

anka3 = Square(akare=10)
anka3.k_alan()
