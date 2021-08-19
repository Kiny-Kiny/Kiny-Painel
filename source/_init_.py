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
global R,B,C,G
R='\033[1;31m';B='\033[1;34m';C='\033[1;37m';G='\033[1;32m';Format="\033[0m";Letra="\033[38;5;15m";Fundo="\033[48;5;19m"
from os import system;from os import execl; from sys import executable; from sys import argv; from os import name; from time import sleep
#---------------------------------------#
def clear(): system('cls' if name == 'nt' else 'clear')
def restart(): execl(executable, executable, *argv)
def sair(): system('rm -rf __pycache__ && clear');print(str(banner)+str(G)+'_ ! _ '+str(C)+'Até logo. '+str(G)+' _ ! _'+str(C));Sair=True
#---------------------------------------#
try: from requests import get
except: system('python3 -m pip install --upgrade pip && pip3 install -r requirements.txt');restart()
#---------------------------------------#
def show():
	file = open('LICENSE','r')
	print(file.read());
	file.close()
	input(str(B)+'\n<'+str(C)+' Aperte Enter para retornar ao menu '+str(B)+'>'+str(C))
#---------------------------------------#
try:
	user = open('username','r')
	user2 = str(user.read())
	user.close()
except:
	clear();user1=input(str(C)+'Digite seu nome de usuário'+str(B)+' >>> '+str(C))
	user=open('username','w+')
	user.write(user1)
	user.close()
	restart()
user=user2
#---------------------------------------#
banner=str(B)+'''
  __  __     __     __   __     __  __    
 /\ \/ /    /\ \   /\ "-.\ \   /\ \_\ \   
 \ \  _"-.  \ \ \  \ \ \-.  \  \ \____ \  
  \ \_\ \_\  \ \_\  \ \_\\"\_\  \/\_____\ 
   \/_/\/_/   \/_/   \/_/ \/_/   \/_____/ 
                                         '''+str(C)+'Coded By: '+str(B)+'Kiny'+str(C)+'\n'+str(Fundo)+str(Letra)+'Hello, '+str(user)+'!'+str(Format)+'   '+str(Fundo)+str(C)+str(Letra)+'Version: 4.0'+str(Format)+str(C)+'   '+str(Fundo)+str(C)+str(Letra)+' PIX: (61) 9603-5417'+str(Format)+str(C)+'\n\n'+str(Fundo)+str(C)+str(Letra)+'_ ! _ Esse programa foi disponiblizado gratuitamente, se você pagou, foi enganado._ ! _'+str(Format)+str(C)+'\n\n'
#---------------------------------------#
try: v=get('https://raw.githubusercontent.com/Kiny-Kiny/Kiny-Painel/main/source/apis.json').json()
except: restart()
#---------------------------------------#
num_status = (str(G)+'ON'+str(C) if "ON" in v['numero'][1] else str(R)+'OFF'+str(C))
cpf_status = (str(G)+'ON'+str(C) if "ON" in v['cpf'][1] else str(R)+'OFF'+str(C))
nome_status = (str(G)+'ON'+str(C) if "ON" in v['nome'][1] else str(R)+'OFF'+str(C))
cnpj_status = (str(G)+'ON'+str(C) if "ON" in v['cnpj'][1] else str(R)+'OFF'+str(C))
placa_status = (str(G)+'ON'+str(C) if "ON" in v['placa'][1] else str(R)+'OFF'+str(C))
ip_status = (str(G)+'ON'+str(C) if "ON" in v['ip'][1] else str(R)+'OFF'+str(C))
cep_status = (str(G)+'ON'+str(C) if "ON" in v['cep'][1] else str(R)+'OFF'+str(C))
covid_status = (str(G)+'ON'+str(C) if "ON" in v['covid'][1] else str(R)+'OFF'+str(C))
bin_status = (str(G)+'ON'+str(C) if "ON" in v['bin'][1] else str(R)+'OFF'+str(C))
banco_status = (str(G)+'ON'+str(C) if "ON" in v['banco'][1] else str(R)+'OFF'+str(C))
#---------------------------------------#
def rds():
	clear();print(str(banner));r_social=v['r_social']
	for i in r_social:
		print(str(B)+'_ ! _ '+str(C)+str(i))
	input(str(B)+'\n<'+str(C)+' Aperte Enter para retornar ao menu '+str(B)+'>'+str(C))
#---------------------------------------#
Sair=False
while Sair==False:
	def init():
		if op == 1:
			r_msg = str(B)+'_ ! _'+str(C)+' Exemplo: 18996166070'+str(B)+'_ ! _'+str(C)+'\nDigite o número que irá consultar'
			req= v['numero'][0]
		elif op == 2:
			r_msg=str(B)+'_ ! _'+str(C)+' Exemplo: 00000000272'+str(B)+'_ ! _'+str(C)+'\nDigite o CPF que irá consultar '
			req= v['cpf'][0]
		elif op == 3:
			r_msg=str(B)+'_ ! _'+str(C)+' Exemplo: Jair Messias Bolsonaro'+str(B)+'_ ! _'+str(C)+'\nDigite o nome que irá consultar '
			req= v['nome'][0]
		elif op == 4:
			r_msg=str(B)+'_ ! _'+str(C)+' Exemplo: 01944765000142'+str(B)+'_ ! _'+(C)+'\nDigite o CNPJ que irá consultar '
			req=v['cnpj'][0]
		elif op == 5:
			r_msg=str(B)+'_ ! _'+str(C)+' Exemplo: bpm9099'+str(B)+'_ ! _'+str(C)+'\nDigite a placa que irá consultar '
			req=v['placa'][0]
		elif op == 6:
			r_msg=str(B)+'_ ! _'+str(C)+' Exemplo: 183.181.164.210'+str(B)+'_ ! _'+str(C)+'\nDigite o IP que irá consultar '
			req=v['ip'][0]
		elif op ==7:
			r_msg=str(B)+'_ ! _'+str(C)+' Exemplo:  13218840'+str(B)+'_ ! _'+str(C)+'\nDigite o CEP que irá consultar '
			req=v['cep'][0]
		elif op ==8:
			r_msg=str(B)+'_ ! _'+str(C)+' Exemplo:  RJ'+str(B)+'_ ! _'+str(C)+'\nDigite o UF que irá consultar '
			req=v['covid'][0]
		elif op ==9:
			r_msg=str(B)+'_ ! _'+str(C)+' Exemplo:  45717360'+str(B)+'_ ! _'+str(C)+'\nDigite a BIN que irá consultar '
			req=v['bin'][0]
		elif op ==10:
			r_msg=str(B)+'_ ! _'+str(C)+' Exemplo:  237'+str(B)+'_ ! _'+str(C)+'\nDigite o código bancario que irá consultar '
			req=v['banco'][0]
		else:
			print(str(R)+'- ! -'+str(C)+' Opção Inválida '+str(R)+'- ! -'+str(C));sleep(2);restart()
		clear();r=input(str(banner)+str(C)+str(r_msg)+str(B)+'>>> '+str(C))
		if 'placa' in req or 'cep' in req:
			msg1=str(req)+str(r)+'/json'
		else:
			msg1=str(req)+str(r)
		try:
			msg= get(str(msg1), verify=False).text.replace('<br>', '\n').replace('<p>', '').replace('{', '').replace('}', '').replace(',', '\n').replace(':', ' ')
		except:
			msg=str(R)+'- ! -'+str(C)+' API OFFLINE OU SERVIDOR FORA DO AR'+str(R)+'- ! -'+str(C)
		clear();sub=int(input(str(banner)+'\n'+str(msg)+'\n'+str(B)+'- ! -'+str(C)+' Deseja fazer uma nova consulta? '+str(B)+'- ! -'+str(C)+'\n['+str(B)+'1'+str(C)+'] Sim\n['+str(B)+'2'+str(C)+'] Nao\n'+str(B)+'===> '+str(C)))
		if sub == 1: init()
		elif sub == 2: sair()
		else: pass
#---------------------------------------#
	try:
		clear();op=int(input(str(banner)+'              ['+str(B)+'1'+str(C)+'] Número ['+str(num_status)+']\n              ['+str(B)+'2'+str(C)+'] CPF    ['+str(cpf_status)+']\n              ['+str(B)+'3'+str(C)+'] Nome   ['+str(nome_status)+']\n              ['+str(B)+'4'+str(C)+'] CNPJ   ['+str(cnpj_status)+']\n              ['+str(B)+'5'+str(C)+'] Placa  ['+str(placa_status)+']\n              ['+str(B)+'6'+str(C)+'] IP     ['+str(ip_status)+']\n              ['+str(B)+'7'+str(C)+'] CEP    ['+str(cep_status)+']\n              ['+str(B)+'8'+str(C)+'] COVID  ['+str(covid_status)+']\n              ['+str(B)+'9'+str(C)+'] BIN    ['+str(bin_status)+']\n              ['+str(B)+'10'+str(C)+'] Banco ['+str(banco_status)+']\n\n              ['+str(B)+'97'+str(C)+'] LICENSE\n              ['+str(B)+'98'+str(C)+'] Redes Sociais\n              ['+str(B)+'99'+str(C)+'] Trocar nome\n              ['+str(R)+'0'+str(C)+'] Sair\n'+str(B)+'              ===> '+str(C)))
		if op == 0: Sair=True
		elif op == 97: show()
		elif op == 98: rds()
		elif op == 99: system('rm -rf username');restart()
		elif op == None: pass
		else: init()
	except: pass
sair()
#---------------------------------------#
