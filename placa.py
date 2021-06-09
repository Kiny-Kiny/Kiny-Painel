global R, B, C, Y, G, RT, CY, CO
CO = '\033[m'
R = '\033[1;31m'
B = '\033[1;34m'
C = '\033[1;37m'
CY = '\033[1;36m'
Y = '\033[1;33m'
G = '\033[1;32m'
RT = '\033[;0m'

import json
import requests
import os
import sys
import pyfiglet

result = pyfiglet.figlet_format("Kiny", font = "cosmic"  )

def consultaplaca():
    # http://api.masterplaca.devplank.com/v2/placa/{placa}/json
    print(f'{C}{G}{result}{C}')
    print(f'{C}[{G}i]{C}Digite o numero da placa.')
    placa_input = input("===>")
    req = requests.get('https://apicarros.com/v1/consulta/{}/json'.format(placa_input), verify=False)  # JSQ7436
    placa_data = req.json()
    clear()
    print(f'{C}{G}{result}{C}')
    try:
        if (placa_data['codigoRetorno']) == "0":
            print(f"{C}Ano: {B}{placa_data['ano']}{C}")
            print(f"Data: {B}{placa_data['data']}{C}")
            print(f"Modelo: {B}{placa_data['modelo']}{C}")
            print(f"Ano do modelo: {B}{placa_data['anoModelo']}{C}")
            print(f"Cor: {B}{placa_data['cor']}{C}")
            print(f"Marca: {B}{placa_data['marca']}{C}")
            print(f"Roubo/furto: {B}{placa_data['dataAtualizacaoRouboFurto']}{C}")
            print(f"Situação: {B}{placa_data['situacao']}{C}")
            print(f"Placa: {B}{placa_data['placa']}{C}")
            print(f"Chassi: {B}{placa_data['chassi']}{C}")
            print(f"UF: {B}{placa_data['uf']}{C}")
            print(f"Município: {B}{placa_data['municipio']}{C}")
            print(f"Modificada em: {B}{placa_data['dataAtualizacaoCaracteristicasVeiculo']}{C}")
            print(f"Alarme atualizado: {B}{placa_data['dataAtualizacaoAlarme']}{C}")
            print(f"Mensagem de retorno: {B}{placa_data['mensagemRetorno']}{C}")
            print(f"Código de retorno: {B}{placa_data['codigoRetorno']}{C}")
        else:
            print(f'{C}[{R}i]{C} Sem dados sobre.')
    except:
        print(f'{C}[{R}ERROR{C}] Placa invalida')
        time.sleep(3)
    del placa_data
    del req
    del placa_input
    print(f'{C}[{G}i{C}] Deseja realizar uma nova consulta?')
    print('1.Sim')
    print('2.Não')
    choice = input("===>")
    if choice == "1" or choice == "01":
        consultaplaca()
    if choice == "2" or choice == "02":
        pass
    else:
        print("Opcao invalida.")
