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
import time
import os
import sys 
import pyfiglet 

result = pyfiglet.figlet_format("Kiny", font = "cosmic"  )

def cnpj(kct, token, anim):
    os.system('clear')
    if kct == '1' or kct == '01':
        gen = "1"
    elif kct == '2' or kct == '02':
        print(f'{C}{G}{result}{C}')
        print("DIGITE O CNPJ SEM / . OU -")
        cnpj_input = input("===>")
        gen = 0
    else:
        print('Opção inválida')
        time.sleep(3)
        cnpj(token, anim)
    if gen == "1":
        print(f'{C}[{G}*{C}] Gerando CNPJ...')
        if anim == '1':
            time.sleep(1)
        cnpj_data = requests.get('http://geradorapp.com/api/v1/cnpj/generate?token={}'.format(token[0])).json()
        cnpj_input = (cnpj_data['data']['number'])
        cnpj_formatted = (cnpj_data['data']['number_formatted'])
        print(f'{C}[{Y}i{C}] O CNPJ gerado foi: {cnpj_formatted}')
    print(f'{C}[{G}i{C}] Consultando CNPJ... ')
    try:
        cnpj_data = requests.get('https://www.receitaws.com.br/v1/cnpj/{}'.format(cnpj_input)).json()
    except:
        print(f'{C}[{R}*{C}]Erro no servidor')
        cnpj_data = "message"

    if 'message' not in cnpj_data:
        tagain = '0'
        print("CNPJ: {}".format(cnpj_data['cnpj']))
        print("Atividade principal: {}".format(cnpj_data['atividade_principal'][0]['text']))
        print("Nome: {}".format(cnpj_data['nome']))
        print("CEP: {}".format(cnpj_data['cep']))
        try:
            print("Telefone: {}".format(cnpj_data['telefone']))
        except:
            pass
        try:
            print("Email: {}".format(cnpj_data['email']))
        except:
            pass
        print("Situação: {}".format(cnpj_data['situacao']))
        print("UF: {}".format(cnpj_data['uf']))
        print("Municipio: {}".format(cnpj_data['municipio']))
        print("Logradouro: {}".format(cnpj_data['logradouro']))
        print("Numero: {}".format(cnpj_data['numero']))
        print("Complemento: {}".format(cnpj_data['complemento']))
        print("Porte: {}".format(cnpj_data['porte']))
        print("Natureza: {}".format(cnpj_data['natureza_juridica']))
        print("Data de abertura: {}".format(cnpj_data['abertura']))
        print("Tipo: {}".format(cnpj_data['tipo']))
        print("Capital: {}".format(cnpj_data['capital_social']))
        try:
            print("===============================")
            print("pessoal: {}".format(cnpj_data['qsa'][0]['nome']))
            print("Cargo: {}".format(cnpj_data['qsa'][0]['qual']))
        except:
            pass
        try:
            print("pessoal: {}".format(cnpj_data['qsa'][1]['nome']))
            print("Cargo: {}".format(cnpj_data['qsa'][1]['qual']))
        except:
            pass
        try:
            print("Pessoal: {}".format(cnpj_data['qsa'][2]['nome']))
            print("Cargo: {}".format(cnpj_data['qsa'][2]['qual']))
        except:
            pass
    else:
        try:
            print(f'{C}[{R}ERROR{C}]' + '{}: CNPJ INVALIDO.'.format(cnpj_formatted))
        except:
            print(f'{C}[{R}ERROR{C}] Sem dados.')
        if gen == '1':
            del cnpj_data
            del cnpj_input
            del cnpj_formatted
            tagain = '1'
            print(f'{C}[{Y}i{C}]Tentando novamente...')
            time.sleep(3)
            cnpj(kct, token, anim)
    if tagain == '0':
        print(f"{C}[{Y}i{C}] DESEJA REALIZAR UMA NOVA CONSULTA?")
        print(f"{C}[{G}1{C}] Sim")
        print(f"{C}[{G}2{C}] Não")
        lo = input('===> ')
        if lo == '1' or lo == '01':
            cnpj(kct, token, anim)
