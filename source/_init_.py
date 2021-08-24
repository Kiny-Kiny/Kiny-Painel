#---------------------------------------#
#Don't need reason, don't need rhyme
#Ain't nothin' that I’d rather do
#Going down, party time
#My friends are gonna be there too
#I'm on the highway to hell
#On the highway to hell
#Highway to hell
#I'm on the highway to hell
#---------------------------------------#
B='\033[1;34m';C='\033[1;37m'
from requests import get;from os import execl; from sys import executable; from sys import argv;from os import system
system('clear||cls')
def restart(): execl(executable, executable, *argv)
try: config=open('config', 'r');config_1=str(config.read());config.close()
except:
	config_0=int(input(str(C)+'['+str(B)+'1'+str(C)+'] Menu normal (PC - Mobile)\n'+'['+str(B)+'2'+str(C)+'] Menu Touch-Screen (PC - Mobile)\n'+str(B)+'===>'+str(C)));config=open('config', 'w+')
	if config_0==1: config_0 = config.write('1')
	elif config_0 ==2: config_0 = config.write('2')
	else: print(str(C)+'['+str(B)+'Opção Inválida'+str(C)+']');system('rm -rf config');exit()
	config.close();restart()
config=config_1
if config == '1': exec(get('https://raw.githubusercontent.com/Kiny-Kiny/Kiny-Painel/main/source/src/menuTerminal.py').text)
elif config == '2': exec(get('https://raw.githubusercontent.com/Kiny-Kiny/Kiny-Painel/main/source/src/menuTouch.py').text)
