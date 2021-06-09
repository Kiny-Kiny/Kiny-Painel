global R, B, C, Y, G, RT, CY, CO
CO = '\033[m'
R = '\033[1;31m'
B = '\033[1;34m'
C = '\033[1;37m'
CY = '\033[1;36m'
Y = '\033[1;33m'
G = '\033[1;32m'
RT = '\033[;0m'
import os
import sys
import requests
import pyfiglet
import time
result = pyfiglet.figlet_format("Kiny", font = "cosmic"  )

def bin():
    print(f'{C}{G}{result}{C}')
    print('Exemplo:45717360')
    print(f'{C}[{Y}i{C}] Digite a BIN.')
    bin_input = input("===>")
    headers = {"Accept-Version": "3",
               "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
    try:
        req = requests.get('https://lookup.binlist.net/' + bin_input, headers=headers)
        req_data = req.json()
    except:
        print(f'{C}[{R}ERROR{C}] Ocorreu um erro,tente novamente.')
    os.system('clear')
    print(result)
    print('Bandeira: {}'.format(req_data['scheme']))
    print('Marca: {}'.format(req_data['brand']))
    print('Tipo: {}'.format(req_data['type']))
    print('Pais: {}'.format(req_data['country']['name']))
    print('Latitude: {}'.format(req_data['country']['latitude']))
    print('Longitude: {}'.format(req_data['country']['longitude']))
    print('Moeda: {}'.format(req_data['country']['currency']))
    print('Emoji: {}'.format(req_data['country']['emoji']))
    print(f'{C}[{Y}i{C}] Deseja realizar uma nova consulta?')
    print('1.Sim')
    print('2.Não')
    choice = input("===>")
    if choice == '1' or choice == '01':
        bin()
    elif choice == '2' or choice == '02':
        pass
    else:
        print(f'{C}[{R}ERROR{C}] Opção inválida')
        time.sleep(3)
