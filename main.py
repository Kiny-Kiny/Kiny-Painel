global R,B,C,Y,G,RT,CY,CO
CO='\033[m'
R='\033[1;31m'
B='\033[1;34m'
C='\033[1;37m'
CY='\033[1;36m'
Y='\033[1;33m'
G='\033[1;32m'
RT='\033[;0m'

## Distribuido livremente pela licença MIT,
## Aos que não sabem o que isso significa,sugerimos estudo.
#######################
##
## Soubemos do grande roubo ao script do Snuking,feito pelo usuário ZeusXaloc,
## Demonstramos repúdio as atitudes do mesmo,totalmente desprezível.
## ZeusXaloc,você NÃO é bem vindo aqui.
## 
#######################
## Obrigado pelo apoio snuking
#######################

def restart():
    python = sys.executable
    os.execl(python, python, *sys.argv)

import os,sys,time,base64, json, re,subprocess,webbrowser,platform
try:
    import requests,platform,signal,atexit,argparse,random,hashlib,urllib3,html5lib,phonenumbers,json,tools, pyfiglet
    from colorama import Fore, Style
    from bs4 import BeautifulSoup
    from phonenumbers import carrier
    from phonenumbers import geocoder
    from phonenumbers import timezone
    from urllib.parse import urlencode
    #from fordev.generator import people #Presente para algum dev que esteja lendo :p
except:
    os.system('pip3 install requests phonenumbers urllib3 colorama bs4 html5lib argparse pytube pyglet')
    for i in range(3):
        print(f'{C}[{Y}i{C}] Reiniciando o painel em {i} seg...')
        time.sleep(1)
    restart()

result = pyfiglet.figlet_format("Kiny", font = "cosmic"  )

def clear():
   if platform.system() == "Windows":
      os.system("cls")
   elif platform.system() == "Linux":
      os.system("clear")
   else:
       os.system("clear")

def youtube():
   if platform.system() == "Windows":
      webbrowser.open_new_tab("https://youtube.com/channel/UC1aTvkvmTVO7OJ6oixtJo8w")
   else:
       os.system("termux-open-url https://youtube.com/channel/UC1aTvkvmTVO7OJ6oixtJo8w")

def zapzap():
   if platform.system() == "Windows":
      webbrowser.open_new_tab("http://wa.me/552179180533")
   else:
       os.system("termux-open-url http://wa.me/552179180533")

def twyu():
   if platform.system() == "Windows":
      webbrowser.open_new_tab("https://youtu.be/njoBMZD_jP0")
   else:
       os.system("termux-open-url https://youtu.be/njoBMZD_jP0")
def gbzap():
   if platform.system() == "Windows":
      webbrowser.open_new_tab("https://chat.whatsapp.com/Gnv9j0SbMtP2uO39CfjMqu")
   else:
       os.system("termux-open-url https://chat.whatsapp.com/Gnv9j0SbMtP2uO39CfjMqu")

if sys.version_info[0] < 3:
    print(f'{C}[{R}ERROR{C}] Necessário utilizar python3!')
    print(f'{C}[{Y}i{C}] Instale-o com base em sua distribuição.')
    sys.exit()

requests = requests.Session()
def clear_config():
	if os.path.exists('options.txt'):
    			try:
    				os.remove('options.txt')
    			except:
    				os.system('rm options.txt')

	if os.path.exists('user'):
    			try:
    				os.remove('user')
    			except:
    				os.system('rm user')

def write():
    clear_config()
    f = open('options.txt','a')
    f.write(str(login))
    f.write(str(cpf_api))
    f.write(str(ip_api))
    f.write(str(placa_api))
    f.write(str(cnpj_api))
    f.write(str(anim))
    f.write(str(menu_return))
    f.close()
    if os.path.exists('user'):
        os.remove('user')
    f = open("user","a")
    f.write(user)
    f.close

global login
global user
global cpf_api
global ip_api
global placa_api
global cnpj_api

if os.path.exists('options.txt') and os.path.exists('user'):
    f = open('options.txt','r') # Nao espero que vc se ache hacker por saber mexer com esse arquivo
    data = f.read()
    login = int(data[0])
    cpf_api = int(data[1])
    ip_api = int(data[2])
    placa_api = int(data[3])
    cnpj_api = int(data[4])
    anim = int(data[5])
    menu_return = int(data[6])
    f.close()
    f = open('user','r')
    user = f.read()
    f.close()
    del data
else:
    login = int('1')
    user = 0
    cpf_api = 0
    ip_api = 0
    placa_api = 0
    cnpj_api = 0
    menu_return = 0
    anim = 0

'''
    Logo abaixo você pode colocar seus tokens pessoais para usar as APIs de forma privada
    1 lugar da lista é da API Geradorapp
    2 lugar da lista é a API de consulta de CRM
    3 lugar da lista é da API OpenWeather.org
'''
token = ["f01e0024a26baef3cc53a2ac208dd141","5072097263","25d800a8b8e8b99d77c809567aa291b8"]

welcome_msg = ["Que a força esteja com você", "Bem vindo", "Você é um mito", "Okaerinasai", "Esta pessoa é muito boa no Websexo ->", "Você é um baitola", "Você é corno", "Você é gay"]
try:
    if __name__ == '__main__':
        print(f'{C}{G}{result}{C}')
        print(f'{C}[{Y}i{C}] {G} Checando por atualizacoes... {C}')
        update = subprocess.check_output('git pull', shell=True)
        if 'Already up to date' not in update.decode():
            print(f'{C}[{Y}*{C}] {G}Atualizacao instalada!\n{C}[{Y}*{C}]Reiniciando o painel...{C}')
            print("Loading:")
            #animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
            animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
            for i in range(len(animation)):
                time.sleep(0.2)
                sys.stdout.write("\r" + animation[i % len(animation)])
                sys.stdout.flush()
            print("\n")
            time.sleep(5)
            subprocess.run('clear')
            restart()
        else:
            print(f'{C}[{Y}i{C}] Nenhuma atualizacao disponivel.')
            time.sleep(2)
except:
    pass

if login == 1:
    tools.clear()
    print(f'{C}{G}{result}{C}')
    user = input(f"{C}[{G}+{C}]USERNAME:  ")
    snh = 'VirtualInsanity'
    if input(f"{C}[{G}+{C}]PASSWORD:  ").strip() == snh:
        tools.clear()
    else:
        print(f"{C}[{R}ERROR{C}] Wrong Password....Yare Yare")
        if anim == 1:
            time.sleep(1)
        exit()
    print("\n ")
if user == 'YATO' or user == 'KINY':
    kinymode=1
    kiny=1
    print(f"{C}[{Y}i{C}]Nova Opção Desbloqueada")
else:
    kinymode=0

try:
    os.system("pkg update -y")
    os.system("pkg install figlet -y")
except:
    os.system("apt update -y")
    os.system("apt install figlet -y")

Sair = False
while(Sair == False):

    tools.clear()
    print(f"Coded By: {CY} KINY {CO} and {CY} YATO {CO} in 07/02/2021")
    print()
    print(f'{C}{G}{result}{C}')
    print(f'{C}[{G}*{C}]'+random.choice(welcome_msg)+' '+str(user)+'!')
    if anim == 1:
        time.sleep(1)
    print(f'{C}[{Y}*{C}]Meu Pix: 228463d7-0bec-44bd-bddd-a780d9530f27')
    print(f'{C}[{Y}*{C}]Patrocinadores: Josuke(Douglas) e Margarina')
    print()
    print(f'{C}[{Y}IMPORTANTE!{C}]Leiam as Notas ao vivo.')
    print(f"{C}[{Y}Data de retorno das consultas{C}]: {C}[{R}NÃO DEFINIDA{C}]")
    print(f"{C}{G}[1]{C} BUSCADOR DE CEP")
    print(f"{C}{G}[2]{C} GEO LOCALIZADOR DE IP")
    print(f"{C}{G}[3]{C} KINY-SITE-INFOGA")
    print(f"{C}{G}[4]{C} CONSULTA DE CNPJ")
    print(f"{C}{G}[5]{C} CONSULTA BANCARIA")
    print(f"{C}{G}[6]{C} CONSULTA CPF {C}[{R}OFF{C}]")
    print(f"{C}{G}[7]{C} CONSULTA CNS")
    print(f"{C}{G}[8]{C} CONSULTA PLACA")
    print(f"{C}{G}[9]{C} CONSULTA CRM")
    print(f"{C}{G}[10]{C} CONSULTA DE NUMERO")
    print(f"{C}{G}[11]{C} CONSULTA BIN")
    print(f"{C}{G}[12]{C} GERAR PESSOA")
    print(f"{C}{G}[13]{C} MOSTRAR MEU IP")
    print(f"{C}{G}[14]{C} CC CHECKER")
    print(f"{C}{G}[15]{C} COVID19")
    print(f"{C}{G}[16]{C} CONSULTAR MÃE {C}[{R}OFF{C}]")
    print(f"{C}{G}[18]{C} CONSULTAR NOME {C}[{R}OFF{C}]")
    print(f"{C}{G}[19]{C} MÚSICAS")
    if kinymode == 1:
    	print(f"{C}{G}[17]{C} FERRAMENTAS")
    if anim==1:
        time.sleep(1)
    print()
    if login:
    	pass
    else:
    	print(f"{C}{G}[95]{C} Mudar username")
    print(f"{C}{G}[90]{C} Meu grupo")
    print(f"{C}{G}[92]{C} Meu Whatsapp")
    print(f"{C}{G}[93]{C} Meu canal")
    print(f"{C}{G}[94]{C} Notas ao vivo")
    print(f"{C}{G}[96]{C} Opções")
    print(f"{C}{G}[97]{C} Notas de versão")
    print(f"{C}{G}[98]{C} Atualizar")
    print(f"{C}{G}[99]{C} Update && Upgrade")
    print(f"{C}{G}[00]{C} EXIT")
    print()
    op = input(f"{C}[{G}Escolha uma opção{C}]: {B}").strip()
    tools.clear()

    if op == '90':
    	gbzap()
    	pass

    if op == '92':
    	zapzap()
    	pass

    if op == '19':
        print(f'{C}{G}{result}{C}')
        os.system("apt install mpg123 -y")
        os.system("clear")
        print(result)
        print(f'{C}[{Y}i{C}]{G} Ainda irei colocar mais músicas, mas eu tô com preguiça.{C}')
        print(f"01 - [{C}{G}Elvis Presley{C}] The Wonder Of You")
        print(f"02 - [{C}{G}Jamiroquai{C}] Virtual Insanity")
        print(f"03 - [{C}{G}Michael Jackson{C}] Billie Jean")
        print(f"04 - [{C}{G}King Crimson{C}] In The Court Of The Crimson King")
        print(f"05 - [{C}{G}The O'Jays{C}] Love Train")
        music = input(f"{C}[{G}Digite o número da música{C}]===>{B}").strip()
        if music == "01" or music == "1":
        	os.system("clear")
        	print(f'{C}{G}{result}{C}')
        	print(f'{C}[{Y}i{C}] Aperte "Q" para parar a música.')
        	file = "TheWonderOfYou.mp3"
        	os.system("mpg123 " + file)
        	pass
        if music == "02" or music == "2":
        	os.system("clear")
        	print(f'{C}{G}{result}{C}')
        	print(f'{C}[{Y}i{C}] Aperte "Q" para parar a música.')
        	shura = "VirtualInsanityRemastered.mp3"
        	os.system("mpg123" + shura)
        	pass
        if music == "03" or music == "3":
        	os.system("clear")
        	print()
        	print(f'{C}[{Y}i{C}] Aperte "Q" para parar a música.')
        	zangetsu = "BillieJean.mp3"
        	os.system("mpg123" + zangetsu)
        	pass
        if music == "04" or music == "4":
        	os.system("clear")
        	print(f'{C}{G}{result}{C}')
        	print(f'{C}[{Y}i{C}] Aperte "Q" para parar a música.')
        	josuke = "InTheCourtOfTheCrimsonKing.mp3"
        	os.system("mpg123" + josuke)
        	pass
        else:
        	pass

    
    if op == '93':
    	youtube()
    	pass
    
    if op == '98':
    	try:
    		print(f'{C}{G}{result}{C}')
    		if __name__ == '__main__':
    			print(f'{C}[{Y}i{C}]{G} Checando por atualizacoes... {C}')
    			update = subprocess.check_output('git pull', shell=True)
    			if 'Already up to date' not in update.decode():
    				print(f'{C}[{Y}*{C}] {G}Atualizacao instalada!\n{C}[{Y}*{C}]Reiniciando o painel...{C}')
    				print("Loading:")
    				#animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
    				animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
    				for i in range(len(animation)):
    					time.sleep(0.2)
    					sys.stdout.write("\r" + animation[i % len(animation)])
    					sys.stdout.flush()
    				print("\n")
    				time.sleep(5)
    				subprocess.run('clear')
    				restart()
    			else:
    				print(f'{C}[{Y}i{C}]Nenhuma atualizacao disponivel.')
    				time.sleep(2)
    	except:
    			pass
    			

    if op == '94':
    	tools.aovivo()

    if op == '18':
    	tools.consultanome()

    if op == '16':
    	tools.nomemae()

    if op == '17' and kinymode == 1:
        print(f'{C}{G}{result}{C}')
        print()
        print(f'{C}[{G}1{C}] Gerar link whatsapp')
        print(f'{C}[{G}2{C}] Youtube downloader')
        print()
        print(f'{C}[{G}0{C}] Sair')
        print()
        choice = input('===>')
        if choice == '1' or choice == '01':
            tools.gerarlinkwhats()
        if choice == '2' or choice == '02':
            tools.youtube()

    if op == '95':
    	print()
    	print(f'{C}[{G}i{C}] Me diga como quer ser chamado.')
    	user = input('===>')
    	write()

    if op == '96':
            print(result)
            print(f'{C}[{G}1{C}] Login : {login}')
            print(f'{C}[{G}2{C}] Trocar APIs')
            print(f'{C}[{G}3{C}] Limpar data')
            print(f'{C}[{G}4{C}] Animação: {anim}')
            #print(f'{C}[{G}5{C}] Modo retornar ao menu: {menu_return}')
            print()
            print(f'{C}[{G}0{C}] Voltar')
            choice = input('===>')
            tools.clear()
            if choice == '1' or choice == '01':
                login ^= 1
            if choice == '2' or choice == '02':
                lista_api_cpf = ["MTE","CADSUS"]
                cpf_api_name = (lista_api_cpf[cpf_api])
                lista_api_ip = ["IP-API 1","API-IP 2"]
                ip_api_name = (lista_api_ip[ip_api])
                lista_api_cnpj = ["receitaws","Governo"]
                cnpj_api_name = (lista_api_cnpj[cnpj_api])
                lista_api_placa = ["receitaws","Governo"]
                placa_api_name = (lista_api_placa[placa_api])
                print(f'{C}[{G}1{C}] CPF API: {cpf_api_name}')
                print(f'{C}[{G}2{C}] IP API: {ip_api_name}')
                print(f'{C}[{G}3{C}] PLACA API: {placa_api_name}')
                print(f'{C}[{G}4{C}] CNPJ API: {cnpj_api_name}')
                print()
                print(f'{C}[{G}0{C}] Voltar')
                choice2 = input('===>')

                if choice2 == '1' or choice2 == '01':
                    cpf_api = cpf_api + 1
                if choice2 == '2' or choice2 == '02':
                    ip_api = ip_api + 1
                if choice2 == '3' or choice2 == '03':
                    placa_api = placa_api + 1
                if choice2 == '4' or choice2 == '04':
                    cnpj_api = cnpj_api + 1

                if int(cpf_api) >= int('2'):
                    cpf_api = 0
                if int(cnpj_api) >= int('2'):
                    cnpj_api = 0
                if int(placa_api) >= int('2'):
                    placa_api = 0
                if int(ip_api) >= int('2'):
                    ip_api = 0
            if choice == '3' or choice == '03':
                clear_config()
            if choice == '4' or choice == '04':
                anim ^= 1
            if choice == '5' or choice == '05':
                menu_return ^= 1
            if choice != 1 and choice !=2 and choice !=3 and choice!=4 and choice!=5 and choice!=0:
                tools.clear()
                print(f'{C}[{R}ERROR{C}] Opção inválida')
            write()

    if op == '97':
        tools.notes()

    if op == '15':
    	tools.covid19()

    if op == '14':
        tools.cc_checker(token)

    if op == '13':
    	tools.ip(ip_api,0,token)

    if op == '12':
        tools.gerar_pessoa(token)

    if op == '11':
        tools.bin()

    if op == '10':
        tools.consultatel()

    if op == '9' or op == '09':
        tools.crm(token)

    if op == '8' or op == '08':
        tools.consultaplaca()

    if op == '7' or op == '07':
        tools.cns(token,anim)

    if op == '6' or op == '06':
        tools.consultacpf(cpf_api,token)

    if op == '5' or op == '05':
        tools.bank(anim)

    if op == '1' or op == '01':
        tools.cep(anim)

    if op == '00' or op == '0':
        os.system("clear")
        Sair = True

    if op == '99' or op == '99':
        os.system("clear")
        os.system("pkg update && pkg update")
        pass

    if op == '3' or op == '03':
        tools.kiny_infoga()

    if op == '2' or op == '02':
        mode = 1
        tools.ip(ip_api,mode,token)

    if op == '4' or op == '04':
        print(f'{C}{G}{result}{C}')
        print(f'''
{C}[{Y}i{C}] O QUE DESEJA FAZER?
{C}[{G}1{C}] GERAR CNPJ
{C}[{G}2{C}] CONSULTAR CNPJ
        ''')
        kct = input("===> ")
        tools.cnpj(kct,token,anim)
os.system('rm -rf __pycache__')
print(f'{C}{R} Arrivederci{C}')
