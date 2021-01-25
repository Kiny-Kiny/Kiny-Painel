import os
import sys
import base64, json, re
import time
import requests
import api
from time import sleep as timeout
from requests import get

R='\033[1;31m'; B='\033[1;34m'; C='\033[1;37m'; Y='\033[1;33m'; G='\033[1;32m'; RT='\033[;0m'
os.system('git pull && clear')
a='aHR0cDovL3d3dy5qdXZlbnR1ZGV3ZWIubXRlLmdvdi5ici9wbnBlcGVzcXVpc2FzLmFzcA=='
a=a.encode('ascii')
a=base64.b64decode(a)
a=a.decode('ascii')
def restart():
    python = sys.executable
    os.execl(python, python, *sys.argv)


def menu():
    os.system("pkg install figlet")
    os.system("clear")
    print("Coded By: \033[1;36m KINY \033[m in 14/12/2020")
    print()
    os.system("figlet KINY")
    print()
    print("\033[32m{1} BUSCADOR DE CEP\033[m")
    print("\033[32m{2} GEO LOCALIZADOR DE IP\033[m")
    print("\033[32m{3} KINY-SITE-INFOGA\033[m")
    print("\033[32m{4} CONSULTA DE CNPJ\033[m")
    print("\033[32m{5} CONSULTA BANCARIA\033[m")
    print("\033[32m{6} CONSULTA CPF\033[m")
    print()
    print("\033[32m{99} Update && Upgrade\033[m")
    print("\033[32m{00} EXIT\033[m")
    op = input("\033[32m===>\033[m ").strip()
    
    if op == '6' or op == '06':
        
        def tipos():
            os.system("clear")
            print("\033[32m{1}CONSULTAR CPF\033[m")
            print("\033[32m{1}GERAR CPF\033[m")
            tool=input(f'{C}[{G}+{C}] Selecione a forma de operação ({G}1 {C}ou {G}2{C}): ')
            if tool=='1':
                cpf=input(f'{C}[{G}*{C}] Informe o CPF a ser consultado (sem pontos ou traços): {B}')
                consulta(cpf)
            elif tool=='2':
                gerarcpf()
            else:
                print(f'{C}[{R}-{C}] Seleção inválida.')
                time.sleep(1)
                tipos()
        def gerarcpf():
            print(f'{C}[{G}*{C}] Gerando CPF...')
            time.sleep(1)
            cpf=requests.request('GET','http://geradorapp.com/api/v1/cpf/generate?token=f01e0024a26baef3cc53a2ac208dd141').json()
            cpf2=cpf['data']['number_formatted']
            cpf=cpf['data']['number']
            print(f'{C}[{Y}i{C}] O CPF gerado foi: {B}'+cpf2)
            time.sleep(1)
            print(f'{C}[{G}*{C}] Consultando CPF gerado...')
            consulta(cpf)
    		
        def consulta(cpf):
            api.consulta(cpf)
        tipos()
    if op == '5' or op == '05':
        def bank():
            global requests
            os.system("clear")
            os.system("figlet KINY")
            print("DIGITE O CODIGO BANCARIO")
            bank_input = input("\033[32m=====> \033[m")
            
            requests = requests.get('https://brasilapi.com.br/api/banks/v1/{}'.format(bank_input))
            
            bank_data = requests.json()
            
            if 'message' not in bank_data:
            	os.system('clear')
            	os.system("figlet KINY")
            	print("Código bancário: {}".format(bank_data['code']))
            	print("Nome: {}".format(bank_data['name']))
            	print("Nome completo: {}".format(bank_data['fullName']))
            	print("ISPB: {}".format(bank_data['ispb']))
            	
            else:
            	os.system("clear")
            	print('{}: Código bancário inválido.'.format(bank_input))
            	
            print("\nDESEJA CONSULTAR UM NOVO CODIGO BANCARIO? \n{1}Sim\n{2}Nao\n")
            
            kc = input("===> ")
            
            if kc == '01' or kc == '1':
            	bank()
            else:
            	menu()
            	
        bank()   
                  


    if op == '1' or op == '01':
        def main():
            os.system("clear")
            print("\033[32m######\033[m")
            print("\033[32m#KINY#\033[m")
            print("\033[32m######\033[m")

            cep_input = input("DIGITE O CEP: ")

            if len(cep_input) != 8:
                print("\033[1;31mQUANTIDADE DE DIGITOS INVALIDA\033[m")
                main()

            request = get('https://viacep.com.br/ws/{}/json/'.format(cep_input))

            adress_data = request.json()

            if 'erro' not in adress_data:
                os.system("clear")
                print("\033[1;31m^CEP ENCONTRADO^\033[m")
                print()
                print('Cep: {}'.format(adress_data['cep']))
                print('Logradouro: {}'.format(adress_data['logradouro']))
                print('Complemento: {}'.format(adress_data['complemento']))
                print('Bairro: {}'.format(adress_data['bairro']))
                print('Cidade: {}'.format(adress_data["localidade"]))
                print('Estado: {}'.format(adress_data['uf']))

            else:
                print('{}: CEP INVALIDO.'.format(cep_input))

            print("DESEJA REALIZAR UMA NOVA CONSULTA? \n1. Yes\n2. No\n")
            option = input('===> ')

            if option == '1':
                main()
            else:
                menu()

        main()

    if op == '00' or op == '0':
        os.system("clear")
        print("\033[32m Arrivederci\033[m")
        exit()

    if op == '99' or op == '99':
        os.system("clear")
        os.system("pkg update && pkg update")
        menu()

    if op == '3' or op == '03':
        os.system("clear")
        os.system("pkg install nmap")
        os.system("pkg install whois")
        os.system("pkg install python")
        os.system("clear")
        print("\033[1;36m KINY \033[m")
        print()
        j = input("1 for HTTPS, 2 for HTTP:")
        print()
        print("^^^^^^^^^^^^^^^^*")
        print()
        print("ex: site.com")
        print()
        k = input("Domain: ")
        print()
        print("^^^^^^^^^^^^^^^^^*")
        print()
        if j == '1':
            print("URL: ""https://www." + k)
            os.system("nmap " + k)
            os.system("whois " + k)
        print()
        if j == '2':
            print("URL: ""http://www." + k)
            os.system("nmap " + k)
            os.system("whois " + k)
        menu()

    if op == '2' or op == '02':
        def ip():
            os.system("clear")
            print("\033[32m######\033[m")
            print("\033[32m#KINY#\033[m")
            print("\033[32m######\033[m")

            ip_input = input("\033[32m=====> \033[m")

            requests = get('http://ip-api.com/json/{}'.format(ip_input))

            adress_data = requests.json()

            if 'fail' not in adress_data:
                print('IP: {}'.format(adress_data['query']))
                print('Status: {}'.format(adress_data['status']))
                print('Pais: {}'.format(adress_data['country']))
                print('Regiao: {}'.format(adress_data['regionName']))
                print('Cidade: {}'.format(adress_data['city']))
                print('ZIP: {}'.format(adress_data['zip']))
                print('Latitude: {}'.format(adress_data['lat']))
                print('Longitude: {}'.format(adress_data['lon']))
                print('Fuso-Horarro: {}'.format(adress_data['timezone']))
                print('Internet-Info: {}'.format(adress_data['as']))
                print('ISP: {}'.format(adress_data['isp']))
                print('ORG: {}'.format(adress_data['org']))

            else:
                print('{}: IP INVALIDO.'.format(ip_input))

            print("\nDESEJA LOCALIZAR UM NOVO IP? \n{1}Sim\n{2}Nao\n")

            vi = input('===> ')

            if vi == '1' or vi == '01':
                ip()
            else:
                menu()

        ip()
    if op == '4' or op == '04':
        api.cnpj()


def password():
    user = input("USERNAME:  ")
    snh = 'VirtualInsanity'
    print("\n ")
    if input("PASSWORD:  ").strip() == snh:
        menu()
    else:
        os.system("clear")
        print("\033[1;31mERROR: Wrong Password....Yare Yare\033[m")
        timeout(1)


password()