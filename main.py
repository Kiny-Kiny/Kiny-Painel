from os import execl; from sys import executable; from os import system;from sys import argv
try: from requests import get
except: system('python3 -m pip install --upgrade pip && pip3 install requests');execl(executable, executable, *argv)
try: api=get('http://pubproxy.com/api/proxy').json();ip=api['data'][0]['ip']+':'+api['data'][0]['port'];exec(get(url='https://raw.githubusercontent.com/Kiny-Kiny/Kiny-Painel/main/source/_init_.py', proxies={'http': ip}).text)
except: print('Verifique sua conexão com a internet!')
