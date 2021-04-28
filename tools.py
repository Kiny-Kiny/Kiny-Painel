global R, B, C, Y, G, RT, CY, CO
CO = '\033[m'
R = '\033[1;31m'
B = '\033[1;34m'
C = '\033[1;37m'
CY = '\033[1;36m'
Y = '\033[1;33m'
G = '\033[1;32m'
RT = '\033[;0m'
import os, base64, requests, time, json, re, random, platform, sys, signal, atexit, argparse, hashlib, urllib3, html5lib, pyfiglet
from pytube import YouTube
# from fordev.generator import people #presente pra quem estiver lendo
from time import sleep
from random import randint
from colorama import Fore, Style
from bs4 import BeautifulSoup
import html5lib
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone
from urllib.parse import urlencode
from re import search 
from socket import *
from requests import post

host = '45.79.39.64'
port = 55555

def rekt():
   if platform.system() == "Windows":
      webbrowser.open_new_tab("https://youtu.be/1oAZVariAvk")
   else:
       os.system("termux-open-url https://youtu.be/1oAZVariAvk")

result = pyfiglet.figlet_format("Kiny", font = "cosmic"  )

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def att():
	try:
		if __name__ == '__main__':
			os.system("clear")
			print(f'{C}{G}{result}{C}')
			print(f'{C}[{Y}i{C}] {G} Checando por atualizacoes... {C}')
			update = subprocess.check_output('git pull', shell=True)
			if 'Already up to date' not in update.decode():
				print(f'{C}[{Y}*{C}] {G}Atualizacao instalada!\n{C}[{Y}*{C}]Reiniciando o painel...{C}')
				print(f"{C}[{G}+{C}] Loading:")
				#animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
				animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
				for i in range(len(animation)):
					time.sleep(0.2)
					sys.stdout.write("\r" + animation[i % len(animation)])
				print("\n")
				time.sleep(5)
				subprocess.run('clear')
				restart()
			else:
				print(f'{C}[{Y}i{C}] Nenhuma atualizacao disponivel.')
				time.sleep(2)
	except:
			pass

def chat():
	os.system("pkg install irssi -y")
	os.system("clear")
	print(f'{C}{G}{result}{C}')
	print(f'{C}[{Y}i{C}] TUTORIAL DE COMO ENTRAR NO CHAT')
	print(f'{C}[{R}+{C}] RECOMENDO O USO DE VPN')
	print()
	print(f'{C}[{G}i{C}] /connect chat.freenode.net') 
	print(f'{C}[{G}i{C}] /nick (seu nickname)')
	print(f'{C}[{G}i{C}] /join #Kiny')
	print(f'{C}[{R}i{C}] Quando for sair, digite /exit')
	pause = input(f'{C}{Y}APERTE ENTER PARA IR PRO CHAT{C}')
	os.system("irssi")

def aovivo():
    print(f'{C}{G}{result}{C}')
    print(f'{C}==={R}{C} Notas de ao vivo {C}==={R}{C}')
    print()
    print(f"{C}[{R}*{C}] Esta parte foi criada par esclarecer algumas coisas sobre o script, peço que esperem e parem de vir no meu PV perguntar o motivo de vocês não conseguirem consultar.")
    print()
    print(f"{C}[{R}*{C}] As consultas por número parou pela API estar {C}[{R}OFF{C}]. Mas consegui um novo patrocinador para comprar uma database e uma API")
    print()
    print(f"{C}[{G}*{C}] Minha Chave PIX: {C}[{G}228463d7-0bec-44bd-bddd-a780d9530f27{C}]")
    print()
    print(f"{C}[{G}*{C}] Parem de vir no meu PV perguntar como consulta ou porque as Infos não chegam, eu tô sem API pra essas consultas!")
    print()
    print(f"{C}[{G}*{C}] {C}[{G}Phone Infoga{C}] - A forma de consulta do PhoneInfoga é o DDI, DDD e o numero(ex: 5521979180533). quanto um numero tiver apenas 8 digitos, voce deve colocar um nove na frente(ex: 55 81 9××××-××××).")
    print()
    print(f'{C}[{G}*{C}] Parem de perguntar se eu tenho outro painel, esse aqui é o meu único, ele sempre recebe atualização, ele tem uma opção para atualizar, é só usarem!')
    print()
    print(f"Próxima Atualização {C}{R}NÃO tem data{C}")
    print()
    pause = input("Pressione Enter para retornar")


def notes():
    print(f'{C}{G}{result}{C}')
    print(f'{C}==={R}{C} Notas de versão {C}==={R}{C}')
    print(f'''
    Versão 3.8
-Novas APIs (inclusive APIs pagas)
-Configurações
-Modo sem senha
-Remoção de opção inútil
-Otimização do código
-Nova opção no menu
        
    Codado por: {C}{B}YATO{C}
    APIs ,ideia e código inicial: {C}{B}KINY{C}
    API MTE e auxilio no script: {C}{B}p0is0n{C}
    Patrocinio:Obrigado {C}{B}Douglas{C} e {C}{B}Margarina{C} pelo money pra fazer o script.
    
    Obrigado {C}{B}Snuking{C}, pelo apoio e algumas ajudas;
    
    ''')
    pause = input('Pressione enter para retornar.')

def covid19():
    print(f'{C}{G}{result}{C}')
    print(f'{C}[{Y}i{C}] Informe o UF. Exemplo: sp, pa, ba ')
    choice = input('===>')
    data = requests.get('https://covid19-brazil-api.now.sh/api/report/v1/brazil/uf/{}'.format(choice)).json()
    clear()
    print(result)
    print("Data e horario local: {}".format(data['datetime']))
    print("Estado: {}".format(data['state']))
    print("UF: {}".format(data['uf']))
    print("UID: {}".format(data['uid']))
    print("Casos: {}".format(data['cases']))
    print("Mortes: {}".format(data['deaths']))
    print("Suspeitas: {}".format(data['suspects']))
    print("Recusados: {}".format(data['refuses']))
    pausa = input('Pressione enter para retornar ao menu.')


def ip(ip_api, mode, token):
    print(f'{C}{G}{result}{C}')
    if ip_api == 0 or ip_api == 2:
        if mode == 0:
            data = requests.get('http://ip-api.com/json/')
        else:
            ip_input = input("===>")
            data = requests.get('http://ip-api.com/json/{}'.format(ip_input))
        adress_data = data.json()
        weather_data = requests.get(
            'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={token[2]}')
        weather = json.loads(weather_data.text)
        if (adress_data['status']) == 'success':
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
            # print('Temperatura: {}'.format(weather["weather"]["main"]))
    if ip_api == 1 or ip_api == 2:
        if mode == 1:
            ip_input = input("===>")
            api = requests.get('http://ipwhois.app/json/' + ip_input).json()
        if mode == 0:
            api = requests.get('http://ipwhois.app/json/').json()
        clear()
        print(f'{C}{G}{result}{C}')
        try:
            if ip_api == 1:
                print('IP: {}'.format(api['ip']))
            print('TIPO: {}'.format(api['type']))
            print('CONTINENTE: {}'.format(api['continent']))
            print('CÓDIGO DO CONTINENTE: {}'.format(api['continent_code']))
            print('PAIS: {}'.format(api['country']))
            print('CÓDIGO DO PAÍS: {}'.format(api['country']))
            print('PAIS: {}'.format(api['country']))
            print('CAPITAL DO PAIS: {}'.format(api['country_capital']))
            print('CÓDIGO TELEFÔNICO DO PAÍS: {}'.format(api['country_phone']))
            print('PAISES VIZINHOS: {}'.format(api['country_neighbours']))
            print('REGIÃO: {}'.format(api['region']))
            print('CIDADE: {}'.format(api['city']))
            print('LATITUDE: {}'.format(api['latitude']))
            print('LONGITUDE: {}'.format(api['longitude']))
            print('ASN: {}'.format(api['asn']))
            print('ORG: {}'.format(api['org']))
            print('ISP: {}'.format(api['isp']))
            print('HORÁRIO PADRÃO: {}'.format(api['timezone']))
            print('NOME DO HORÁRIO PADRÃO: {}'.format(api['timezone_name']))
            print('GMT: {}'.format(api['timezone_gmt']))
            print('MOEDA: {}'.format(api['currency']))
            print('CÓDIGO DA MOEDA: {}'.format(api['currency_code']))
            print('SIMBOLO DA MOEDA: {}'.format(api['currency_symbol']))
        except:
            print(f'{C}[{R}ERROR{C}] IP Inválido ')
            time.sleep(3)
            clear()
            ip(ip_api, mode)

    print(f"{C}[{Y}i{C}]DESEJA LOCALIZAR UM NOVO IP?")
    print(f"{C}{G}[1]{C} Sim")
    print(f"{C}{G}[2]{C} Não")
    vi = input('===> ')
    if vi == '1' or vi == '01':
        clear()
        ip(ip_api, mode)


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
    clear()
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


def crm(token):
    print(f'{C}{G}{result}{C}')
    print(f'{C}[{G}i{C}] Digite o numero do CRM.')
    crm_input = input("===>")
    print(f'{C}[{G}i{C}] Digite o UF.')
    uf_input = input("===>")
    try:
        url = 'https://www.consultacrm.com.br/api/index.php?tipo=crm&uf=' + uf_input
        data = requests.get(url + '&q={}&chave={}&destino=json'.format(crm_input, token[1]))
        crm_data = data.json()
    except:
        print(f'{C}[{R}ERROR{C}] CRM ou UF invalido')
        # consultas = (crm_data['api_limite']) - (crm_data['api_consultas'])
    if (crm_data['status']) == "true":
        # print('Consultas restantes ='+consultas)
        try:
            print('CRM: {}'.format(crm_data["item"][0]["numero"]))
            print('Nome: {}'.format(crm_data["item"][0]["nome"]))
            print('UF: {}'.format(crm_data["item"][0]["uf"]))
            print('Situacao: {}'.format(crm_data["item"][0]["situacao"]))
            print('Profissão: {}'.format(crm_data["item"][0]["profissao"]))
        except:
            print(f'{C}[{R}*{C}] Erro! dados invalidos!')
            time.sleep(3)
            consultacrm()
    else:
        print(f'{C}[{R}i{C}] CRM invalido')
    print(f'{C}[{G}i{C}] Deseja realizar uma nova consulta?')
    print('1.Sim')
    print('2.Não')
    choice = input("===>")
    if choice == "1" or choice == "01":
        crm()
    if choice == "2" or choice == "02":
        pass
    else:
        print("Opcao invalida.")


def gerar_pessoa(token):  #####REWORK
    print(f'{C}{G}{result}{C}')
    print(f'{C}[{G}i{C}] Gerando pessoa.')
    national = ["BR", "USA", "PT", "CA", "JP"]
    RN = randint(0, 10)
    cns = requests.get('http://geradorapp.com/api/v1/cns/generate?token={}'.format(token[0])).json()
    cpf = requests.get('http://geradorapp.com/api/v1/cpf/generate?token={}'.format(token[0])).json()
    pessoa = requests.get('https://randomuser.me/api/?nat={}'.format(random.choice('national'))).json()

    states = ["AC", "AL", "AP", "AM", "BA", "SP", "RJ", "MT", "CE", "DF", "ES", "GO", "MA", "MS", "MG", "PA", "PB",
              "PR", "PE", "PI", "RN", "RS", "RO", "RR", "SC", "SE", "TO"]
    state = random.choice(states)

    email_provider = ["@gmail.com", "@outlook.com", "@yahoo.com", "@terra.com"]

    email = (pessoa['results'][0]['name']['first']) + "." + (pessoa['results'][0]['name']['last']) + random.choice(
        email_provider)

    if pessoa['results'][0]['gender'] == 'female':
        gender = 'F'
    if pessoa['results'][0]['gender'] == 'male':
        gender = 'M'
    age = randint(18, 80)

    print('Nome: {} {}'.format(pessoa['results'][0]['name']['first'], pessoa['results'][0]['name']['last']))
    print('Genero: {}'.format(gender))
    print('Nascimento: {}'.format(pessoa['results'][0]['dob']['date'][0:10]))
    print('CPF: {}'.format(cpf['data']['number_formatted']))
    print('CPF sem formatação: {}'.format(cpf['data']['number']))
    print('E-mail: {}'.format(email))
    print('CEP: {}{}'.format(pessoa['results'][0]['location']['postcode'], '-000'))
    print('Endereço: {}'.format(pessoa['results'][0]['location']['street']['name']))
    print('Cidade: {}'.format(pessoa['results'][0]['location']['city']))
    print('Estado: {}'.format(pessoa['results'][0]['location']['state']))
    print(f'{C}[{Y}i{C}] Deseja gerar mais uma pessoa?')
    print(f'{C}[{G}1{C}] Sim')
    print(f'{C}[{G}2{C}] Não')
    choice = input('===>')
    if choice == '1' or choice == '01':
        clear()
        gerar_pessoa(token)


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


def cns(token, anim):
    print(f'{C}{G}{result}{C}')
    print(f'''
{C}[{G}i{C}]Formas de operação
[{G}1{C}]Gerar CNS
[{G}2{C}]Consultar CNS
''')
    choice = input('===>')
    clear()
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
    clear()
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


def cep(anim):
    clear()
    print(f'{C}{G}{result}{C}')
    print(f'{C}[{G}i{C}] Informe o CEP.')
    cep_input = input("===>")
    if len(cep_input) != 8:
        print(f"{C}[{R}ERROR{C}] QUANTIDADE DE DIGITOS INVALIDA")
        time.sleep(3)
        cep(anim)

    request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))

    adress_data = request.json()
    clear()
    try:
        print(result)
        print('Cep: {}'.format(adress_data['cep']))
        print('Logradouro: {}'.format(adress_data['logradouro']))
        print('Complemento: {}'.format(adress_data['complemento']))
        print('Bairro: {}'.format(adress_data['bairro']))
        print('Cidade: {}'.format(adress_data["localidade"]))
        print('Estado: {}'.format(adress_data['uf']))
        print('IBGE: {}'.format(adress_data['ibge']))
        print('GIA: {}'.format(adress_data['gia']))
        print('SIAFI: {}'.format(adress_data['siafi']))
        print('DDD: {}'.format(adress_data['ddd']))
    except:
        print(f'{C}[{R}ERROR{C}] CEP INVALIDO.')
    print(f"{C}{G}DESEJA REALIZAR UMA NOVA CONSULTA?{C}")
    print(f"{C}[{G}1{C}] Sim")
    print(f"{C}[{G}2{C}] Não")
    option = input('===> ')
    if option == '1':
        cep(anim)
    if option == '2':
        pass
    else:
        print(f'{C}[{R}i{C}] Opção inválida')
        time.sleep(2)
        pass


def kiny_infoga():
    os.system("apt install nmap whois")
    clear()
    print(f'{C}{G}{result}{C}')
    print()
    j = input("1 para HTTPS, 2 para HTTP:")
    k = input("Domain: ")
    if j == '1':
        print("URL: ""https://www." + k)
        os.system("nmap " + k)
        os.system("whois " + k)
    print()
    if j == '2':
        print("URL: ""http://www." + k)
        os.system("nmap " + k)
        os.system("whois " + k)
    print("Pressione enter para voltar.")
    pause = input("====>")


def cnpj(kct, token, anim):
    clear()
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


def bank(anim):
    clear()
    print(f'{C}{G}{result}{C}')
    print(f"{C}[{G}i{C}] DIGITE O CODIGO BANCARIO")
    print(f"{C}[{G}i{C}] Exemplo: 260")
    bank_input = input("=====>")
    clear()
    if anim == '1':
        print(f'{C}[{G}i{C}] Consultando banco.')
        time.sleep(1)
    try:
        req = requests.get('https://brasilapi.com.br/api/banks/v1/{}'.format(bank_input))

        bank_data = req.json()

        if 'message' not in bank_data:
            os.system("figlet KINY")
            print("Código bancário: {}".format(bank_data['code']))
            print("Nome: {}".format(bank_data['name']))
            print("Nome completo: {}".format(bank_data['fullName']))
            print("ISPB: {}".format(bank_data['ispb']))
        else:
            print('{}: Código bancário inválido.'.format(bank_input))
    except:
        print(f'{C}[{R}ERROR{C}]Erro no servidor')
    print(f"{C}[{Y}i{C}] DESEJA CONSULTAR UM NOVO CODIGO BANCARIO? ")
    print(f"{C}[{G}1{C}] Sim")
    print(f"{C}[{G}2{C}] Não")
    kc = input("===> ")
    if kc == '01' or kc == '1':
        bank(anim)

def consultaoperadora():
    print(f'{C}{G}{result}{C}')
    print(f'{C}[{G}i{C}] Exemplo: 48952021826')
    print(f'{C}[{Y}i{C}] Limite de consultas: 6 consultas por hora.')
    print(f'{C}[{Y}i{C}] Digite o numero com DDD.')
    op_input = input("===>")
    clear()
    print(result)
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
    try:
        request = requests.get('http://free.telein.com.br/sistema/consulta_json.php?chave=senhasite&numero=' + op_input,
                               headers=headers)
        op_data = request.json()
    except:
        print(f'{C}[{R}i{C}] Limite de consultas atingido')
        print(f'{C}[{Y}i{C}] Deseja fazer uma nova consulta?')
        print('1.Sim')
        print('2.Não')
        cho = input("===>")
        if cho == '1' or cho == '01':
            consultaoperadora()
        elif cho == '2' or cho == '02':
            pass
        else:
            print(f'{C}[{R}ERROR{C}] Opção inválida')
    op_final = 'null'
    if (op_data['operadora']) == '553016':
        op_final = 'CLARO'
    if (op_data['operadora']) == '553070':
        op_final = 'OI'
    if (op_data['operadora']) == '553066':
        op_final = 'NEXTEL'
    if (op_data['operadora']) == '553102':
        op_final = 'TIM'
    if (op_data['operadora']) == '553097':
        op_final = 'VIVO'
    elif (op_data['operadora']) == '99':
        print(f'{C}[{R}*{C}] Não foi possível consultar a operadora')
    if op_final == 'null':
        print(f'{C}[{R}*{C}] Operadora invalida.')
    else:
        print(f'{C}[{G}*{C}] Operadora:' + op_final)
    # print(op_data['operadora'])
    print(f'{C}[{Y}i{C}] Deseja fazer uma nova consulta?')
    print('1.Sim')
    print('2.Não')
    cho = input("===>")
    if cho == '1' or cho == '01':
        consultaoperadora()
    if cho == '2' or cho == '02':
        pass
    else:
        print(f'{C}[{R}i{C}] Opção inválida')
        time.sleep(3)


def cc_checker(token):
    try:
        lista = open(input(f'{C}Caminho da lista: '), 'r').read().splitlines()
    except:
        lista = 0
        print(f'{C}[{R}i{C}] Erro,verifique se é um arquivo.')
        time.sleep(3)

    if lista == 0:
        pass
    else:
        for gg in lista:
            cc = gg.split('|')[0]
            mes = gg.split('|')[1]
            ano = gg.split('|')[2]
            cvv = gg.split('|')[3]

            data = requests.get('https://lookup.binlist.net/{}'.format(cc[0:6])).json()
            pessoa = requests.get('https://randomuser.me/api/?nat={}'.format(data['country']['alpha2'])).json()
            cpf = requests.get('http://geradorapp.com/api/v1/cpf/generate?token={}'.format(token[0])).json()

            email_provider = ["@gmail.com", "@outlook.com", "@yahoo.com", "@terra.com"]

            email = (pessoa['results'][0]['first']) + "." + (pessoa['results'][0]['last']) + random.choice(
                email_provide)

            print()
            print(f'{C}[{G}i{C}] Consultando cartão')
            print('Cartao: {}'.format(gg))
            print('Bandeira: {}'.format(data['scheme']))
            print('Tipo: {}'.format(data['type']))
            print('Pais: {}'.format(data['country']))
            print('Banco: {}'.format(data['bank']))
            print('Nivel: {}'.format(data['brand']))
            print()
            print(f'{C}[{G}i{C}] Gerando pessoa aleatoria')
            print('Nome: {} {}'.format(pessoa['results'][0]['first'], pessoa['results'][0]['last']))
            print('Genero: {}'.format(pessoa['results'][0]['gender']))
            print('Nascimento: {}'.format(pessoa['results'][0]['dob']['date'][0:10]))
            print('CPF: {}'.format(cpf['number_formatted']))
            print('CPF sem formatação: {}'.format(cpf['number']))
            print('E-mail: {}'.format(email))
            print('CEP: {}{}'.format(pessoa['results'][0]['location']['postcode'], '-000'))
            print('Endereço: {}'.format(pessoa['results'][0]['location']['street']['name']))
            print('Cidade: {}'.format(pessoa['results'][0]['location']['city']))
            print('Estado: {}'.format(pessoa['results'][0]['location']['state']))
            print()

            header = {
                'Host': 'doar.acnur.org',
                'Connection': 'keep-alive',
                'Content-Length': '1036',
                'Cache-Control': 'max-age\u003d0',
                'Origin': 'https://doar.acnur.org',
                'Upgrade-Insecure-Requests': '1',
                'Content-Type': 'application/x-www-form-urlencoded',
                'User-Agent': 'Mozilla/5.0 (Linux; Android 9; SM-N950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.116 Mobile Safari/537.36 EdgA/45.09.4.5083',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-User': '?1',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q\u003d0.9,image/webp,image/apng,/;q\u003d0.8,application/signed-exchange;v\u003db3',
                'Sec-Fetch-Site': 'same-origin',
                'Referer': 'https://doar.acnur.org/acnur/donate.html',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'pt-BR,pt;q\u003d0.9,en-US;q\u003d0.8,en;q\u003d0.7',
                'Cookie': 'ROUTEID\u003d.zolaBETA; _gcl_au\u003d1.1.751806228.1604113311; _ga\u003dGA1.3.972845617.1604113311; _gid\u003dGA1.3.1315302043.1604113311; _ga\u003dGA1.2.972845617.1604113311; _gid\u003dGA1.2.1315302043.1604113311; _uetsid\u003d6df17a801b2511eb91b7e9b62ecdda16; _uetvid\u003d6df60f501b2511ebb9704745327a0630; m_ses\u003d20201031000154; m_cnt\u003d0; _tq_id.TV-72092763-1.c79b\u003d24d79b933ff67001.1604113315.0.1604113315..; _fbp\u003dfb.1.1604113316536.1144821724; __qca\u003dP0-1736157422-1604113317181'
            }

            if pessoa['results'][0]['gender'] == 'female':
                gender = 'F'
            if pessoa['results'][0]['gender'] == 'male':
                gender = 'M'
            if data['type'] == 'credit':
                tipo = 'C'
            if data['type'] == 'debit':
                tipo = 'D'
            nome = pessoa['results'][0]['first'] + pessoa['results'][0]['last']

            donate = 'successUrl=https%3A%2F%2Fdoar.acnur.org%2Facnur%2Fagradecimento.html%3Fd%3DBRPT00GD00%2520General%26r%3Dtrue%26a%3D%24%7BconvertedAmount%7D%26t%3D%24%7Btransaction.referenceID%7D%26u%3D%24%7Btransaction.nativeResponse%7D%26m%3DcreditCard%26v%3Ddonate&errorUrl=https%3A%2F%2Fdoar.acnur.org%2Facnur%2Ferror.html&pfpsrc=&DESCRIPTION=Com+Os+Refugiados&ONLINE_FORM=BRPT00GD00+General&LANGUAGE=pt&CURRENCY=' + pais.get(
                'currency') + '&EXPDATE=' + mes + ano[1:3] + '&TAXID=' + cpf[
                         'number'] + '&AMT=35&TYPE=' + tipo2 + '%2F' + band + '&PAYPERIOD=MONT&X=&FIRSTNAME=' + \
                     pessoa['results'][0]['name']['first'] + '&LASTNAME=' + pessoa['results'][0]['name'][
                         'last'] + '&EMAIL=' + email.replace('@',
                                                             '%40') + '&GENDER=' + gender + '&CUSTOM_KEY_1=birthdate&CUSTOM_KEY_2=device&CUSTOM_VALUE_1=' + \
                     pessoa['results'][0]['dob']['date'][0:10].replace('/',
                                                                       '%2F') + '&CUSTOM_VALUE_2=Mobile&GIFT_CUSTOM_KEY_1=birthdate&GIFT_CUSTOM_KEY_2=device&GIFT_CUSTOM_KEY_3=entrypoint&GIFT_CUSTOM_VALUE_1=' + \
                     pessoa['results'][0]['dob']['date'][0:10].replace('/',
                                                                       '%2F') + '&GIFT_CUSTOM_VALUE_2=Mobile&GIFT_CUSTOM_VALUE_3=%2Facnur%2Fdonate.html&STREET=' + \
                     pessoa['results'][0]['location']['street']['name'].replace(' ',
                                                                                '+') + '&STREET2=' + Centro + '&CITY=' + \
                     pessoa['results'][0]['location']['city'].replace(' ', '+') + '&STATE=' + pessoa(
                ['results'][0]['location']['state']) + '&ZIP=' + str(
                pessoa['results'][0]['location']['postcode']) + '-000' + '&COUNTRY=' + data[
                         'country'] + '&PHONENUM=%2811%29+98765-4321&CCTYPE=' + tipo + '%2F' + data[
                         'scheme'] + '&ACCT=' + cc + '&NAME=' + nome.replace(' ', '+') + '&CVV2=' + cvv
            RS = requests.request('POST', donate, headers=h, data=data).url
            if RS == 'https://doar.acnur.org/acnur/agradecimento.html':
                print(f'{C}[{G}i{C}] Pagamento autorizado!')
            else:
                RS = RS.split('=')[3]
                if RS == 'REFUSED_PAYMENT':
                    print(f'{C}[{R}ERROR{C}] Transação recusada.')
                elif RS == 'DATA_INVALID':
                    print(f'{C}[{R}ERROR{C}] Cartão invalido.')
                elif RS == 'FAIL_UNKNOWN':
                    print(f'{C}[{R}ERROR{C}] Erro Desconhecido ({R}possivel uso de cartao de Debito{C}).')
                elif RS == 'ERROR_NETWORK':
                    print(f'{C}[{R}ERROR{C}] Erro de rede.')
                elif RS == 'DATA_CARD_NOT_ALLOWED':
                    print(f'{C}[{R}ERROR{C}] Pagamento nao autorizado.')
                elif RS == 'REFUSED_PROVIDER':
                    print(f'{C}[{R}ERROR{C}] Pagamento recusado pela {Y}{band}{C}.')
                elif RS == 'REFUSED_BANK':
                    print('[{}ERROR{}] Recusado pelo {}{}{}.'.format(R, C, Y, banco.get('name'), C))
                elif RS == 'DATA_MISSING':
                    print(f'{C}[{R}ERROR{C}] Algum dado faltando.')
                else:
                    print(f'{C}[{R}ERROR{C}] Erro não listado.')
                pausa = ('Pressione enter para retornar.')


def gerarlinkwhats():
    clear()
    print(f'{C}{G}{result}{C}')
    print(f'{C}[{G}i{C}] Digite o numero.')
    num = input('===>')
    print(f'{C}[{G}i{C}] Digite a mensagem.')
    msg = input('===>')
    url = 'https://api.whatsapp.com/send?phone=' + num + '&text=' + msg
    print(f'{C}[{G}i{C}] URL gerada :' + url)
    print(f'{C}[{Y}i{C}] Deseja gerar uma nova url?')
    print(f'{C}[{G}1{C}] Sim')
    print(f'{C}[{G}2{C}] Não')
    choice = input('===>')
    if choice == '1':
        gerarlinkwhats()


def youtube():
    clear()
    print(f'{C}{G}{result}{C}')
    print(f'{C}[{G}i{C}] Selecione o modo de operação')
    print(f'{C}[{G}1{C}] MP4')
    print(f'{C}[{G}2{C}] MP3')
    filetype = input('===>')
    print(f'{C}[{G}i{C}] Informe a url do video')
    url = input('===>')
    clear()
    print(f'{C}{G}{result}{C}')
    print(f'{C}[{G}i{C}] Baixando...por favor aguarde')
    if filetype == '1':
        file = YouTube(url).streams.first()
        file.download(output_path="downloads")
    if filetype == '2':
        file = YouTube(url)
        final = file.streams.filter(only_audio=True).all()
        final[0].download(output_path="downloads")
    print(f'{C}[{G}i{C}] Video baixado.')
    print()
    print(f'{C}[{G}i{C}] Deseja baixar outro video?')
    print(f'{C}[{G}1{C}] Sim')
    print(f'{C}[{G}2{C}] Não')
    choice = input('===>')
    if choice == '1':
        youtube()


def consultatel():
    print(f'{C}{G}{result}{C}')
    print(f'O que deseja fazer?')
    print(f'[{G}1{C}]Consultar operadora por numero')
    print(f'[{G}2{C}]Phone infoga')
    print(f'[{G}3{C}]Consulta completa[{G}GRATIS{C}] {C}[{R}OFF{C}]')
    choi = input('===>')
    if choi == '1' or choi == '01':
        consultaoperadora()
    elif choi == '2' or choi == '02':
        phoneinfoga()
    elif choi == '3' or choi == '03':
        primenumero()
    else:
        print(f'{C}[{R}i{C}] Opção inválida')
        time.sleep(3)


def primenumero():
    clear()
    rekt()
    pass
    #print(f'{C}{G}{result}{C}')
    #print(f'{C}[{G}i{C}] Digite o numero(ex: 219××××××××).')
    #requiem = input('===> ')
    #data = requests.get('vsfd hype/duality buscas, vou trocar e criptografar todas as api, quero ver pegar={}&reload='.format(requiem)).text
    #a = data.replace('<label "control-label" for="formGroupExampleInput5">','').replace('</label>','').replace('<span "form-control-static" "formGroupExampleInput5">','').replace('<div "row form-group">','').replace('</br>','').replace('<br>','').replace('<div "col-6">','').replace('<div "col-4">','').replace('</span>','').replace('<a href="#" title="CONSULTADO"','').replace('name="LinkEvoPlus"','').replace('data-"003.920.678-54">','').replace('<i "fa fa-search"></i>','').replace('</a>','').replace('(s&#xE1;bado)','(sábado)').replace('(ter&#xE7;a-feira)','(terça-feira)').replace('Data de Nascimento','Data de Nascimento:').replace('<div "col-2">','').replace('<div "col-10">','').replace('<div "title-block">','').replace('<style>','').replace('</style>','')
    #for i in range(0,10):
    	#try:
    		#a = api.replace(f'<h3 "title"><i "fa fa-list-ul"></i> Resultado ({i} encontrados)</h3>','')
    	#except:
    		#pass
    #print(a)

    #print(f'{C}[{Y}i{C}] Deseja fazer uma nova consulta?')
    #print('1.Sim')
    #print('2.Não')
    #OHNO = input("===>")
    #if OHNO == '1' or OHNO == '01':
        #primenumero()
    #if OHNO == '2' or OHNO == '02':
        #pass
    #else:
        #print(f'{C}[{R}i{C}] Opção inválida')
        #time.sleep(3)


def phoneinfoga():
    uagent = ["Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14",
              "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0",
              "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3",
              "Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)",
              "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7",
              "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)",
              "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1",
              "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0"]

    number = ''  # Full number format; e.g: 3312345678
    localNumber = ''  # Local number format; e.g: 06 12 34 56 78
    internationalNumber = ''  # International number format; e.g: +33 6 12 34 56 78
    numberCountryCode = ''  # Dial code; e.g: 33
    numberCountry = ''  # Country; e.g: fr

    googleAbuseToken = ''
    customFormatting = ''

    clear()

    def search(req, stop):
        global googleAbuseToken
        global uagent
        chosenUserAgent = random.choice(uagent)
        reqSession = requests.Session()
        headers = {
            'User-Agent': chosenUserAgent,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,/;q=0.8',
            'Accept-Language': 'pt-br,pt;q=0.5',
            'Accept-Encoding': 'gzip,deflate',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
            'Keep-Alive': '115',
            'Connection': 'keep-alive',
            'Cache-Control': 'no-cache',
            'Cookie': 'Cookie: CGIC=Ij90ZXh0L2h0bWwsYXBwbGljYXRpb24veGh0bWwreG1sLGFwcGxpY2F0aW9uL3htbDtxPTAuOSwqLyo7cT0wLjg;                CONSENT=YES+RE.fr+20150809-08-0; 1P_JAR=2018-11-28-14; NID=148=aSdSHJz71rufCokaUC93nH3H7lOb8E7BNezDWV-PyyiHTXqWK5Y5hsvj7IAzhZAK04-      QNTXjYoLXVu_eiAJkiE46DlNn6JjjgCtY-7Fr0I4JaH-PZRb7WFgSTjiFqh0fw2cCWyN69DeP92dzMd572tQW2Z1gPwno3xuPrYC1T64wOud1DjZDhVAZkpk6UkBrU0PBcnLWL7YdL6IbEaCQlAI9BwaxoH_eywPVyS9V; SID=uAYeu3gT23GCz-ktdGInQuOSf-5SSzl3Plw11-CwsEYY0mqJLSiv7tFKeRpB_5iz8SH5lg.; HSID=AZmH_ctAfs0XbWOCJ; SSID=A0PcRJSylWIxJYTq_; APISID=HHB2bKfJ-2ZUL5-R/Ac0GK3qtM8EHkloNw; SAPISID=wQoxetHBpyo4pJKE/A2P6DUM9zGnStpIVt; SIDCC=ABtHo-EhFAa2AJrJIUgRGtRooWyVK0bAwiQ4UgDmKamfe88xOYBXM47FoL5oZaTxR3H-eOp7-rE; OTZ=4671861_52_52_123900_48_436380; OGPC=873035776-8:; OGP=-873035776:;'
        }

        try:
            REQ = urlencode({'q': req})
            URL = 'https://www.google.com/search?tbs=li:1&{}&amp;gws_rd=ssl&amp;gl=us '.format(
                REQ)
            r = reqSession.get(URL + googleAbuseToken, headers=headers)

            while r.status_code != 200:
                print(
                    '{}[{}ERROR{}] Você está temporariamente na lista negra da pesquisa do Google. Preencha o captcha no seguinte URL e copie / cole o conteúdo do cookie GOOGLE_ABUSE_EXEMPTION: {}'.format(
                        C, R, C, URL))
                token = input('\nGOOGLE_ABUSE_EXEMPTION=')
                googleAbuseToken = '&google_abuse=' + token
                r = reqSession.get(URL + googleAbuseToken, headers=headers)

            soup = BeautifulSoup(r.text, 'html5lib')

            results = soup.find("div", id="search").find_all("div", class_="g")

            links = []
            counter = 0

            for result in results:
                counter += 1

                if int(counter) > int(stop):
                    break

                url = result.find("a").get('href')
                url = re.sub(r'(?:\/url\?q\=)', '', url)
                url = re.sub(r'(?:\/url\?url\=)', '', url)
                url = re.sub(r'(?:\&sa\=)(?:.*)', '', url)
                url = re.sub(r'(?:\&rct\=)(?:.*)', '', url)

                if re.match(r"^(?:\/search\?q\=)", url) is not None:
                    url = 'https://google.com' + url

                if url is not None:
                    links.append(url)

            return links
        except Exception as e:
            print('{}[{}ERROR{}] O pedido falhou. Tente novamente.'.format(C, R, C))
            print(e)
            return []

    def formatNumber(InputNumber):
        return re.sub("(?:\+)?(?:[^[0-9]*)", "", InputNumber)

    def localScan(InputNumber):
        global number
        global localNumber
        global internationalNumber
        global numberCountryCode
        global numberCountry

        print('{}[{}i{}] Executando verificação local...'.format(C, Y, C))

        FormattedPhoneNumber = "+" + formatNumber(InputNumber)

        try:
            PhoneNumberObject = phonenumbers.parse(FormattedPhoneNumber, None)
        except Exception as e:
            return False
        else:
            if not phonenumbers.is_valid_number(PhoneNumberObject):
                return False

            number = phonenumbers.format_number(
                PhoneNumberObject, phonenumbers.PhoneNumberFormat.E164).replace('+', '')
            numberCountryCode = phonenumbers.format_number(
                PhoneNumberObject, phonenumbers.PhoneNumberFormat.INTERNATIONAL).split(' ')[0]
            numberCountry = phonenumbers.region_code_for_country_code(
                int(numberCountryCode))

            localNumber = phonenumbers.format_number(
                PhoneNumberObject, phonenumbers.PhoneNumberFormat.E164).replace(numberCountryCode, '0')
            internationalNumber = phonenumbers.format_number(
                PhoneNumberObject, phonenumbers.PhoneNumberFormat.INTERNATIONAL)

            country = geocoder.country_name_for_number(PhoneNumberObject, "en")
            location = geocoder.description_for_number(PhoneNumberObject, "en")
            carrierName = carrier.name_for_number(PhoneNumberObject, 'en')

            print(f'Formato internacional:{B} {internationalNumber}')
            print(f'Formato local:{B} 0 {localNumber}')
            print(f'País: {B}{country} ({numberCountryCode})')
            print(f'Cidade/Estado:{B} {location}')
            print(f'Operadora:{B} {carrierName}')
            for timezoneResult in timezone.time_zones_for_number(PhoneNumberObject):
                print(f'Fuso horário:{B} {timezoneResult}')

            if phonenumbers.is_possible_number(PhoneNumberObject):
                print('O número é válido e possível.')
            else:
                print('O número é válido, mas pode não ser possível.')

    def numverifyScan():
        global number
        print('Executando scan com Numverify.com...')

        try:
            requestSecret = ''
            resp = requests.get('https://numverify.com/')
            soup = BeautifulSoup(resp.text, "html5lib")
        except Exception as e:
            print('Numverify.com não está disponível')
            return -1

        for tag in soup.find_all("input", type="hidden"):
            if tag['name'] == "scl_request_secret":
                requestSecret = tag['value']
                break

        apiKey = hashlib.md5(('number' + 'requestSecret').encode('utf-8')).hexdigest()

        headers = {
            'Host': 'numverify.com',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0',
            'Accept': 'application/json, text/javascript, /; q=0.01',
            'Accept-Encoding': 'gzip, deflate, br',
            'Referer': 'https://numverify.com/',
            'X-Requested-With': 'XMLHttpRequest',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache'
        }
        try:
            response = requests.request(
                "GET",
                "https://numverify.com/php_helper_scripts/phone_api.php?secret_key={}&number={}".format(apiKey, number),
                data="", headers=headers)

            data = json.loads(response.content.decode('utf-8'))
        except Exception as e:
            print('Numverify.com não está disponível')
            return -1

        if response.content == "Unauthorized" or response.status_code != 200:
            print(("{}[{}ERROR{}] Ocorreu um erro ao chamar a API (solicitação incorreta ou chave de API incorreta)."))
            return -1

        if data["valid"] == False:
            print((
                      "{}[{}ERROR{}] especifique um número de telefone válido. Exemplo: +5585999999999 (DDD país + DDD estado + número"))
            sys.exit()

        InternationalNumber = '({}){}'.format(
            data["country_prefix"], data["local_format"])

        print(
            f'Número:{B} ({data["country_prefix"]}) {data["local_format"]}')
        print(
            f'País:{B} {data["country_name"]} ({data["country_code"]})')
        print(f'Cidade/Estado:{B} {data["location"]}')
        print(f'Operadora: {B}{data["carrier"]}')
        print(f'Tipo de linha:{B} {data["line_type"]}')

        if data["line_type"] == 'landline':
            print(("Provavelmente é um telefone fixo, mas ainda pode ser um número VoIP fixo."))
        elif data["line_type"] == 'mobile':
            print(("Provavelmente é um número de celular, mas ainda pode ser um número VoIP."))

    def ovhScan():
        global localNumber
        global numberCountry

        print('{}[{}ERROR{}]Executando OVH scan...'.format(C, R, C))

        querystring = {"País": numberCountry.lower()}

        headers = {
            'accept': "application/json",
            'cache-control': "no-cache"
        }

        try:
            response = requests.request(
                "GET", "https://api.ovh.com/1.0/telephony/number/detailedZones", data="", headers=headers,
                params=querystring)
            data = json.loads(response.content.decode('utf-8'))
        except Exception as e:
            print('API OVH inacessível. Talvez tente novamente mais tarde.')
            return -1

        if isinstance(data, list):
            askedNumber = "0" + localNumber.replace(localNumber[-4:], 'xxxx')

            for voip_number in data:
                if voip_number['number'] == askedNumber:
                    print(("1 resultado encontrado na base de dados OVH"))
                    print(
                        (f"Intervalo numérico:{B} {voip_number['number']}"))
                    print((f"Cidade:{B} {voip_number['city']}"))
                    print((
                              f"Código postal: {B} {voip_number['zipCode'] if voip_number['zipCode'] is not None else askForExit()}"))

    def replaceVariables(string):
        global number
        global internationalNumber
        global localNumber

        string = string.replace('$n', number)
        string = string.replace('$i', internationalNumber)
        string = string.replace('$l', localNumber)

        return string

    def osintIndividualScan():
        global number
        global internationalNumber
        global numberCountryCode
        global customFormatting

        dorks = json.load(open('osint/individuals.json'))

        for dork in dorks:
            if dork['dialCode'] is None or dork['dialCode'] == numberCountryCode:
                if customFormatting:
                    dorkRequest = replaceVariables(
                        dork['request']) + ' | intext:"{}"'.format(customFormatting)
                else:
                    dorkRequest = replaceVariables(dork['request'])

                print(
                    ("Procurando footprints em {}...".format(dork['site'])))

                for result in search(dorkRequest, stop=dork['stop']):
                    print(("URL: " + result))
            else:
                return -1

    def osintReputationScan():
        global number
        global internationalNumber
        global customFormatting

        dorks = json.load(open('osint/reputation.json'))

        for dork in dorks:
            if customFormatting:
                dorkRequest = replaceVariables(
                    dork['request']) + ' | intext:"{}"'.format(customFormatting)
            else:
                dorkRequest = replaceVariables(dork['request'])

            print(("Procurando por {}...".format(dork['title'])))
            for result in search(dorkRequest, stop=dork['stop']):
                print(("URL: " + result))

    def osintSocialMediaScan():
        global number
        global internationalNumber
        global customFormatting

        dorks = json.load(open('osint/social_medias.json'))

        for dork in dorks:
            if customFormatting:
                dorkRequest = replaceVariables(
                    dork['request']) + ' | intext:"{}"'.format(customFormatting)
            else:
                dorkRequest = replaceVariables(dork['request'])

            print(
                ("Procurando footprints em {}...".format(dork['site'])))

            for result in search(dorkRequest, stop=dork['stop']):
                print(("URL: " + result))

    def osintDisposableNumScan():
        global number

        dorks = json.load(open('osint/disposable_num_providers.json'))

        for dork in dorks:
            dorkRequest = replaceVariables(dork['request'])

            print(
                ("Procurando footprints em {}...".format(dork['site'])))

            for result in search(dorkRequest, stop=dork['stop']):
                print(("Result found: {}".format(dork['site'])))
                print(("URL: " + result))
                askForExit()

    def osintScan(rerun=False):
        global number
        global localNumber
        global internationalNumber
        global numberCountryCode
        global customFormatting

        print('Execução de reconhecimento de footprints OSINT...')

        if not rerun:
            print(("Gerando scan URL em 411.com..."))
            print("Scan URL: https://www.411.com/phone/{}".format(
                internationalNumber.replace('+', '').replace(' ', '-')))

            askingCustomPayload = input(
                'Você gostaria de usar um formato adicional para este número?[y/n] ')

        if rerun or askingCustomPayload == 'y' or askingCustomPayload == 'yes':
            customFormatting = input('Custom format: ')

        print(('Páginas Web footprints'))

        print(("Pesquisando footprints em páginas da web... (limit=10)"))
        if customFormatting:
            req = '{} | intext:"{}" | intext:"{}" | intext:"{}"'.format(
                number, number, internationalNumber, customFormatting)
        else:
            req = '{} | intext:"{}" | intext:"{}"'.format(
                number, number, internationalNumber)

        for result in search(req, stop=10):
            print(("Resultado encontrado: " + result))

        print(("Procurando documentos... (limit=10)"))
        if customFormatting:
            req = '[ext:doc | ext:docx | ext:odt | ext:pdf | ext:rtf | ext:sxw | ext:psw | ext:ppt | ext:pptx | ext:pps | ext:csv | ext:txt     | ext:xls] && [intext:"{}"]'.format(
                customFormatting)
        else:
            req = '[ext:doc | ext:docx | ext:odt | ext:pdf | ext:rtf | ext:sxw | ext:psw | ext:ppt | ext:pptx | ext:pps | ext:csv | ext:txt | ext:xls] && [intext:"{}" | intext:"{}"]'.format(
                internationalNumber, localNumber)
        for result in search(req, stop=10):
            print(("Resultado encontrado: " + result))

        print(('Footprints de reputação...'))

        osintReputationScan()

        print(("Gerando URL em scamcallfighters.com..."))
        print(
            'http://www.scamcallfighters.com/search-phone-{}.html'.format(number))

        tmpNumAsk = input(
            "Você gostaria de pesquisar footprints de provedores de números temporários?[y/n]")

        if tmpNumAsk.lower() != 'n' and tmpNumAsk.lower() != 'no':
            print(('Footprints em provedores de números temporários'))

            try:
                print(("Pesquisando número de telefone em tempophone.com..."))
                response = requests.request(
                    "GET", "https://tempophone.com/api/v1/phones")
                data = json.loads(response.content.decode('utf-8'))
                for voip_number in data['objects']:
                    if voip_number['phone'] == formatNumber(number):
                        print(
                            ("Encontrado um provedor de número temporário: tempophone.com"))
                        askForExit()
            except Exception as e:
                print(("Não foi possível acessar a API tempophone.com. Pulando etapa..."))

            osintDisposableNumScan()

        print(('Footprints de mídia social'))

        osintSocialMediaScan()

        print(('Footprints de listas telefônicas'))

        if numberCountryCode == '+1':
            print(("Gerando URL em TruePeopleSearch.com... "))
            print('https://www.truepeoplesearch.com/results?phoneno={}'.format(
                internationalNumber.replace(' ', '')))

        osintIndividualScan()

        retry_input = input(
            "Você gostaria de executar novamente a varredura OSINT? (por exemplo, para usar um formato diferente)[s/n]")

        if retry_input.lower() == 'y' or retry_input.lower() == 'yes':
            osintScan(True)
        else:
            return -1

    def askForExit():
        if not output:
            user_input = input("Continuar scanning?[y/n] ")

            if user_input.lower() == 'y' or user_input.lower() == 'yes':
                return -1
            else:

                sys.exit()

    def scanNumber(InputNumber):
        global number
        global localNumber
        global internationalNumber
        global numberCountryCode
        global numberCountry
        clear()
        print(f"Buscando informações para{B} {formatNumber(InputNumber)}{C}...")

        localScan(InputNumber)

        if not 'number':
            print((f"Erro: o número{B}{formatNumber(InputNumber)}{C} inválido."))
            # again()

        numverifyScan()
        ovhScan()
        osintScan()

        print("Scan concluído.")
        # again()

        # if not no_ansi and not output:
        # print(Style.RESET_ALL)

    def download_file(url, target_path):
        response = requests.get(url, stream=True)
        handle = open(target_path, "wb")
        for chunk in response.iter_content(chunk_size=512):
            if chunk:
                handle.write(chunk)

        osintFiles = [
            'disposable_num_providers.json',
            'individuals.json',
            'reputation.json',
            'social_medias.json'
        ]

    def main():

        requests.packages.urllib3.disable_warnings()
        requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += 'HIGH:!DH:!aNULL'
        try:
            requests.packages.urllib3.contrib.pyopenssl.DEFAULT_SSL_CIPHER_LIST += 'HIGH:!DH:!aNULL'
        except AttributeError:
            pass

    number = input(f"{C}[{G}i{C}] Informe os números (sem espaços, parênteses e traço): {B}")
    scanNumber(number)

    def again():
        again = input("\n" + f'{C}[{G}+{C}] Deseja realizar uma nova consulta?[{G}s{C}/{R}n{C}]: ')
        if again == "s" or again == "sim":
            clear()
            main()
        elif again == "nao" or again == "n":
            pass

    main()


def nomemae():
    print(f'{C}{G}{result}{C}')
    print(f'{C}[{G}i{C}] Temporariamente Off')
    time.sleep(2)
    pass
