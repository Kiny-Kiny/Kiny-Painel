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

result = pyfiglet.figlet_format("Kiny", font = "cosmic"  )

def covid19():
    print(f'{C}{G}{result}{C}')
    print(f'{C}[{Y}i{C}] Informe o UF. Exemplo: sp, pa, ba ')
    choice = input('===>')
    data = requests.get('https://covid19-brazil-api.now.sh/api/report/v1/brazil/uf/{}'.format(choice)).json()
    os.system('clear')
    print(f'{C}[{Y}{result}{C}]')
    print("Data e horario local: {}".format(data['datetime']))
    print("Estado: {}".format(data['state']))
    print("UF: {}".format(data['uf']))
    print("UID: {}".format(data['uid']))
    print("Casos: {}".format(data['cases']))
    print("Mortes: {}".format(data['deaths']))
    print("Suspeitas: {}".format(data['suspects']))
    print("Recusados: {}".format(data['refuses']))
    pausa = input('Pressione enter para retornar ao menu.')
