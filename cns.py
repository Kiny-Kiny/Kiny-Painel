global R, B, C, Y, G, RT, CY, CO
CO = '\033[m'
R = '\033[1;31m'
B = '\033[1;34m'
C = '\033[1;37m'
CY = '\033[1;36m'
Y = '\033[1;33m'
G = '\033[1;32m'
RT = '\033[;0m'

import requests
import os
import sys
import pyfiglet
import random

result = pyfiglet.figlet_format("Kiny", font = "cosmic"  )

def cns(token, anim):
    print(f'{C}{G}{result}{C}')
    print(f'''
{C}[{G}i{C}]Formas de operação
[{G}1{C}]Gerar CNS
[{G}2{C}]Consultar CNS
''')
    choice = input('===>')
    os.system('clear')
    if choice == '1' or choice == '01':
        print(f'{C}[{G}i{C}] Gerando CNS')
        cns = requests.request('GET', 'http://geradorapp.com/api/v1/cns/generate?token={}'.format(token[0])).json()
        cns2 = cns['data']['number_formatted']
        entrada = cns['data']['number']
        print(f'{C}[{Y}i{C}] O CNS gerado foi: ' + cns2)
        if anim == 1:
            time.sleep(1)
        print(f'{C}[{G}i{C}] Consultando CNS...')
    if choice == '2' or choice == '02':
        entrada = input('===>')
    if anim == 1:
        time.sleep(1)
    os.system('clear')
    cns_data = requests.get('http://geradorapp.com/api/v1/cns/validate/{}?token={}'.format(entrada, token[0])).json()
    try:
        print('Numero: {}'.format(cns_data["data"]["number"]))
        print('Mensagem: {}'.format(cns_data["data"]["message"]))
    except:
        print(f'{C}[{R}*{C}] CNS INVALIDO.')
    print(f"{C}{G}DESEJA REALIZAR UMA NOVA CONSULTA?{C}")
    print(f"{C}{G}[1]{C} Sim")
    print(f"{C}{G}[2]{C} Não")
    lo = input('===> ')
    if lo == '1' or lo == '01':
        cns(token, anim)
