#---------------------------------------#
global R,B,C,G
R='\033[1;31m';
B='\033[1;34m';
C='\033[1;37m';
G='\033[1;32m';
Format="\033[0m";
Letra="\033[38;5;15m";
Fundo="\033[48;5;19m"
from os import system
from os import execl
from sys import executable
from sys import argv
from os import name
from time import sleep
#---------------------------------------#
system('git pull')
#---------------------------------------#
def clear():
	system('cls' if name == 'nt' else 'clear')
def restart():
	execl(executable, executable, *argv)
def sair():
	system('rm -rf __pycache__ && clear');print(f'{banner}{G}_ ! _ {C}Até logo. {G} _ ! _{C}');Sair=True
#---------------------------------------#
try:
	from requests import get
except:
	system('python3 -m pip install --upgrade pip && pip3 install -r requirements.txt');restart()
#---------------------------------------#
def show():
	file = open('eminel.txt','r')
	print(file.read());
	file.close()
#---------------------------------------#
try:
	user = open('username','r')
	user2 = str(user.read())
	user.close()
except:
	clear();user1=input(f'{C}Digite seu nome de usuário{B} >>>{C} ')
	user=open('username','w+')
	user.write(user1)
	user.close()
	restart()
user=user2
#---------------------------------------#
banner=f'''{B}
 __  __     __     __   __     __  __    
/\ \/ /    /\ \   /\ "-.\ \   /\ \_\ \   
\ \  _"-.  \ \ \  \ \ \-.  \  \ \____ \  
 \ \_\ \_\  \ \_\  \ \_\\"\_\  \/\_____\ 
  \/_/\/_/   \/_/   \/_/ \/_/   \/_____/ 
                                         {C}Coded By: {B}Kiny{C}\n{Fundo}{Letra}Hello, {user}!{Format}   {Fundo}{C}{Letra}Version: 4.0{Format}{C}   {Fundo}{C}{Letra} PIX: (61) 9603-5417{Format}{C}\n\n'''
#---------------------------------------#
v = get('https://pastebin.com/raw/JRSu4jNW').json()
num_status = (f'{G}ON{C}' if "ON" in v['numero'][1] else f'{R}OFF{C}')
cpf_status = (f'{G}ON{C}' if "ON" in v['cpf'][1] else f'{R}OFF{C}')
nome_status = (f'{G}ON{C}' if "ON" in v['nome'][1] else f'{R}OFF{C}')
cnpj_status = (f'{G}ON{C}' if "ON" in v['cnpj'][1] else f"{R}OFF{C}")
placa_status = (f'{G}ON{C}' if "ON" in v['placa'][1] else f"{R}OFF{C}")
ip_status = (f'{G}ON{C}' if "ON" in v['ip'][1] else '{R}OFF{C}')
cep_status = (f'{G}ON{C}' if "ON" in v['cep'][1] else '{R}OFF{C}')
covid_status = (f'{G}ON{C}' if "ON" in v['covid'][1] else '{R}OFF{C}')
bin_status = (f'{G}ON{C}' if "ON" in v['bin'][1] else '{R}OFF{C}')
banco_status = (f'{G}ON{C}' if "ON" in v['banco'][1] else '{R}OFF{C}')
#---------------------------------------#
def rds():
	clear();print(f'{banner}');r_social=v['r_social']
	for i in r_social:
		print(f'{B}_ ! _{C} ',i)
	input(f'\n{B}<{C} Aperte Enter para retornar ao menu {B}>{C}')
#---------------------------------------#
Sair=False
while Sair==False:
	def init():
		if op == 1:
			r_msg = f'{B}_ ! _{C} Exemplo: 18996166070{B}_ ! _{C}\nDigite o número que irá consultar'
			req= v['numero'][0]
		elif op == 2:
			r_msg=f'{B}_ ! _{C} Exemplo: 00000000272{B}_ ! _{C}\nDigite o CPF que irá consultar '
			req= v['cpf'][0]
		elif op == 3:
			r_msg=f'{B}_ ! _{C} Exemplo: Jair Messias Bolsonaro{B}_ ! _{C}\nDigite o nome que irá consultar '
			req= v['nome'][0]
		elif op == 4:
			r_msg=f'{B}_ ! _{C} Exemplo: 01944765000142{B}_ ! _{C}\nDigite o CNPJ que irá consultar '
			req=v['cnpj'][0]
		elif op == 5:
			r_msg=f'{B}_ ! _{C} Exemplo: bpm9099{B}_ ! _{C}\nDigite a placa que irá consultar '
			req=v['placa'][0]
		elif op == 6:
			r_msg=f'{B}_ ! _{C} Exemplo: 183.181.164.210{B}_ ! _{C}\nDigite o IP que irá consultar '
			req=v['ip'][0]
		elif op ==7:
			r_msg=f'{B}_ ! _{C} Exemplo:  13218840{B}_ ! _{C}\nDigite o CEP que irá consultar '
			req=v['cep'][0]
		elif op ==8:
			r_msg=f'{B}_ ! _{C} Exemplo:  RJ{B}_ ! _{C}\nDigite o UF que irá consultar '
			req=v['covid'][0]
		elif op ==9:
			r_msg=f'{B}_ ! _{C} Exemplo:  45717360{B}_ ! _{C}\nDigite a BIN que irá consultar '
			req=v['bin'][0]
		elif op ==10:
			r_msg=f'{B}_ ! _{C} Exemplo:  237{B}_ ! _{C}\nDigite o código bancario que irá consultar '
			req=v['banco'][0]
		else:
			print(f'{R}- ! -{C} Opção Inválida {R}- ! -{C}');sleep(2);restart()
		clear();r=input(f'{banner}{C}{r_msg}{B}>>>{C} ')
		if 'placa' in req or 'placa' in req:
			msg1=req+r+'/json'
		else:
			msg1=req+r
		try:
			msg= get(msg1).text.replace('<br>', '\n').replace('<p>', '').replace('{', '').replace('}', '').replace(',', '\n').replace(':', '')
		except:
			msg=f'{R}- ! -{C} API OFFLINE OU SERVIDOR FORA DO AR{R}- ! -{C}'
		clear();sub=int(input(f'{banner}\n{msg}\n{B}- ! -{C} Deseja fazer uma nova consulta? {B}- ! -{C}\n[{B}1{C}] Sim\n[{B}2{C}] Nao\n{B}===> {C}'))
		if sub == 1: init()
		elif sub == 2: sair()
		else: pass
#---------------------------------------#
	try:
		clear();op=int(input(f'{banner}[{B}1{C}] Número [{num_status}]\n[{B}2{C}] CPF    [{cpf_status}]\n[{B}3{C}] Nome   [{nome_status}]\n[{B}4{C}] CNPJ   [{cnpj_status}]\n[{B}5{C}] Placa  [{placa_status}]\n[{B}6{C}] IP     [{ip_status}]\n[{B}7{C}] CEP    [{cep_status}]\n[{B}8{C}] COVID  [{covid_status}]\n[{B}9{C}] BIN    [{bin_status}]\n[{B}10{C}] Banco [{banco_status}]\n\n[{B}97{C}] LICENSE\n[{B}98{C}] Redes Sociais\n[{B}99{C}] Trocar nome\n[{R}0{C}] Sair\n{B}===>{C} '))
		if op == 0: Sair=True
		elif op == 97: show()
		elif op == 98: rds()
		elif op == 99: system('rm -rf username');restart()
		else: init()
	except: pass
sair()
#---------------------------------------#
