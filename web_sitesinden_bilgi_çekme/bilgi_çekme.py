#konu: siteden sadece windows k?tü amaçlı yazılım ları bulmak 

#saatlerce uğraşıp bu kadar azdığım kod
"""
from bs4 import BeautifulSoup
import requests

url = "https://malpedia.caad.fkie.fraunhofer.de/families/1/"

respone = requests.get(url)
print(respone) #istek alındı

soup = BeautifulSoup(respone.text , 'html.parser')
title = soup.find("title")

for title in soup.find_all():
    print(title)

"""


#Hocanın yaptığı

import requests
from bs4 import BeautifulSoup

def get_windows(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content,'html.parser')
        rows = soup.find_all('tr')
        windows_names = []
        for row in rows:
            icon = row.find('i',class_='fa-windows')
            if icon:
                common_name = row.find('td',class_='common_name').text.strip()
                windows_names.append(common_name)
        return windows_names
    

def seve_txt(names,filename):
    with open(filename,'a') as file:
        for name in names:
            file.write(name + '\n')

if __name__ == "__mein__":
    base_url = "https://malpedia.caad.fkie.fraunhofer.de/families/"
    toplam_sayfa = 31
    file_name = "output.txt"
    for sayfa_numrası in range(1,toplam_sayfa+1):
        url = base_url + str(sayfa_numrası) + '/'
        print(f"Sayfa İşleniyor {sayfa_numrası}")
        yaygın_isim = get_windows(url)
        if yaygın_isim:
            seve_txt(yaygın_isim,file_name)
            print(f"Bu Sayfa İşlendi Ve Bitti")
    
