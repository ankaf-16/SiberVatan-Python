import os

gecerli_dizin = os.getcwd()
print(gecerli_dizin)

for i in os.listdir(gecerli_dizin):
    print(i)

new_kütüphane = os.path.join(gecerli_dizin,"yeni metin")
os.mkdir(new_kütüphane)
print(f"{new_kütüphane} oluştu")

os.chdir(new_kütüphane)
print(f"{new_kütüphane} dizine gidildi")

dosya_yolu = os.path.join(new_kütüphane,"example.exe")

with open(dosya_yolu, 'w',encoding='utf-8' ) as file:
    file.write("hello worl")

os.remove('example.txt')

os.chdir(gecerli_dizin)

os.rmdir('yeni metin')

