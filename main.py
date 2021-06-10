global R,B,C,Y,G,RT,CY,CO
CO='\033[m';R='\033[1;31m';B='\033[1;34m';C='\033[1;37m';CY='\033[1;36m';Y='\033[1;33m';G='\033[1;32m';RT='\033[;0m';NO_FORMAT="\033[0m";C_GREY89="\033[38;5;254m";C_RED1="\033[48;5;196m"
#######################
## RECODADO POR YATO ##
#######################

def restart():
    python = sys.executable
    os.execl(python, python, *sys.argv)

import os,sys,time,json,subprocess,platform
try:
	import requests,random,json
except:
    choice = input(f'{C}{G}[i]{C} Vejo que é sua primeira vez aqui,\n Deseja instalar o software necessário?\n1-Sim\n2-Não\n_')
    if choice:
        os.system("apt install figlet -y")
        os.system('python3 -m pip install --upgrade pip')
        os.system('pip3 install requests pytube phonenumbers')
    else:
        print(f'Ok,instale por si ou isso é um adeus.');exit()
    restart()

try:
    from data import cpf,ui,ip,cnpj,placa,crm,cep,numero
    from data import covid as covid19
    from data import bin as bina
    from data import cpf_2 as cpf2
    from data import banco as banks
except:
	print('Arquivos corrompidos.');exit()

def clear():
	os.system('cls');os.system('clear')

requests = requests.Session();result = os.popen('figlet KINY').read()

try:
    if __name__ == '__main__':
        ui.dialog('Buscando atualizações ...')
        update = subprocess.check_output('git pull', shell=True)
        if 'Already up to date' not in update.decode():
            ui.dialog('Atualização instalada.\nReiniciando o painel.')
            restart()
        else:
            print(f'{C}[{Y}i{C}] Nenhuma atualizacao disponivel.')
            time.sleep(2)
except:
    if os.path.exists('.git'):
        pass
    else:
        ui.error_dialog('Falta de repositório GIT local')
'''
Atualização por git pull falhou.tentando por método antigo.
os.popen('git clone http://github.com/oporadokrl/Kiny-Painel.git').read()
os.popen('cd Kiny-Painel && mv * ../').read()
'''

try:
    subprocess.check_output('apt update -y', shell=True)
    os.system("apt install figlet curl -y")
except:
    os.system("pacman -Sy figlet curl")

Sair = False
while(Sair == False):
    try:
        op = int(ui.menu(f'BUSCADOR DE CEP\nCONSULTAR IP\nCONSULTA DE CNPJ\nCONSULTA BANCARIA\nCONSULTA CPF {C}[{G}ON{C}]\nCONSULTA PLACA\nCONSULTA CRM\nCONSULTA DE NUMERO\nCONSULTA BIN\nGERAR PESSOA\nMOSTRAR MEU IP\nCOVID19\nCONSULTAR MÃE {C}[{R}OFF{C}]\nCONSULTAR NOME {C}[{R}OFF{C}]\nCONSULTA DE EMAIL {C}[{R}OFF{C}]\nFERRAMENTAS::Atualizar\nSair'))
    except:
        ui.error_dialog('Caracteres não reconhecidos');op=None
    ui.clear()

    if op == 1:
        cep.consultar()
    elif op == 2:
        ip.consultar()
    elif op == 3:
        cnpj.consultar()
    elif op == 4:
        banks.consultar()
    elif op == 5:
        choice = ui.menu('CPF 1\nCPF 2')
        if choice == '1':
            cpf.consultar()
        elif choice == '2':
            cpf2.consultar()
        else:
            ui.error_dialog()
    elif op == 6:
        placa.consultar()
    elif op == 7:
        crm.consultar()
    elif op == 8:
        numero.consultar() # TELEFONE
    elif op == 9:
        bina.consultar()
    elif op == 10:
        ui.error_dialog('A consulta está desativada por falta de API.') #gerar pessoa
    elif op == 11:
        ip.consultar('25d800a8b8e8b99d77c809567aa291b8',1) #mostrar IP
    elif op == 12:
        covid19.consultar() # nCOVID19
    elif op == 13:
        ui.error_dialog('A consulta está desativada por falta de API.') # MAE
    elif op == 14:
        ui.error_dialog('A consulta está desativada por falta de API.') # NOME
    elif op == 15:
        ui.error_dialog('A consulta está desativada por falta de API.') # EMAIL
    elif op == 16: #Ferramentas
        ui.dialog('Em construção,\n  Aguardem.')
    elif op == 17: #Atualizar painel
        os.popen('cd data && bash update.sh');ui.dialog('Reiniciando o painel...');ui.restart()
    elif op == 18:
        Sair = True
    elif op == None:
        pass
    else:
        ui.error_dialog('Opção incorreta')
