import os
import sys
import base64, json, re
import time
import requests
from time import sleep as timeout
requests = requests.Session()

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
    print("\033[32m{7} CONSULTA CNS\033[m")
    print("\033[32m{8} CONSULTA PLACA\033[m")
    print("\033[32m{9} CONSULTA CRM\033[m")
    print()
    print("\033[32m{99} Update && Upgrade\033[m")
    print("\033[32m{00} EXIT\033[m")
    op = input("\033[32m===>\033[m ").strip()
    if op == '9' or op == '09':
        def consultacrm():
            import os,time,base64,json,re,requests
            clear()
            os.system("figlet KINY")
            global requests
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
                print('CRM: {}'.format(crm_data["item"][0]["numero"]))
                print('Nome: {}'.format(crm_data["item"][0]["nome"]))
                print('UF: {}'.format(crm_data["item"][0]["uf"]))
                print('Situacao: {}'.format(crm_data["item"][0]["situacao"]))
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
        def consultaplaca():
            clear()
            os.system("figlet KINY")
            print(f'{C}[{G}i]{C}Digite o numero da placa.')
            placa_input = input("===>")
            from requests import get
            req = requests.get('https://apicarros.com/v1/consulta/{}/json'.format(placa_input), verify = False) # JSQ7436
            placa_data = req.json()
            clear()
            os.system('figlet KINY')
            if (placa_data['codigoRetorno']) == "0":
                print('Placa: {}'.format(placa_data['placa']))
                print('Marca: {}'.format(placa_data['marca']))
                print('Modelo: {}'.format(placa_data['modelo']))
                print('Ano: {}'.format(placa_data['ano']))
                print('Cor: {}'.format(placa_data['cor']))
                print('UF: {}'.format(placa_data['uf']))
                print('Municipio: {}'.format(placa_data['municipio']))
                print('Chassi: {}'.format(placa_data['chassi']))
                print('Situacao: {}'.format(placa_data['situacao']))
            else:
                print(f'{C}[{R}i]{C} Ocorreu um erro,tente novamente mais tarde.')
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
            clear()
            os.system('figlet KINY')
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
                nova=input(f'{C}[{G}+{C}]Deseja realizar uma nova consulta?[{G}s{C}/{R}n{C}]: ').lower()
                if nova=='s' or nova=='sim':
                    tipos()
                else:
                    menu()
            except(AttributeError):
                print(f'{R}CPF Gerado nao existe{C}')
                print(f'{R}Pressione enter para retornar{C}')
                lo = input("===>")
                tipos()
        def tipos():
            clear()
            os.system('figlet KINY')
            print(f'''
{C}[{G}i{C}] Formas de operação: 
[{G}1{C}] Consultar CPF.
[{G}2{C}] Gerar CPF e consultar.
''')
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
        def geradorcnpj():
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
    user = input("USERNAME:  ")
    snh = 'VirtualInsanity' 
    print("\n ")
    if input("PASSWORD:  ").strip() == snh:
        menu()
    else:
        os.system("clear")
        print("\033[1;31mERROR: Wrong Password....Yare Yare\033[m")
        timeout(1)
#menu()
password()
