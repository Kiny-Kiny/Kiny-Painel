import requests, os, time, base64, json, re
from requests import get
requests = requests.Session()
R='\033[1;31m'; B='\033[1;34m'; C='\033[1;37m'; Y='\033[1;33m'; G='\033[1;32m'; RT='\033[;0m'
os.system('git pull && clear')
a='aHR0cDovL3d3dy5qdXZlbnR1ZGV3ZWIubXRlLmdvdi5ici9wbnBlcGVzcXVpc2FzLmFzcA=='
a=a.encode('ascii')
a=base64.b64decode(a)
a=a.decode('ascii')

def tipos():
  os.system('clear')
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
  try:
    h={
    'Content-Type': "text/xml, application/x-www-form-urlencoded;charset=ISO-8859-1, text/xml; charset=ISO-8859-1",
    'Cookie': "ASPSESSIONIDSCCRRTSA=NGOIJMMDEIMAPDACNIEDFBID; FGTServer=2A56DE837DA99704910F47A454B42D1A8CCF150E0874FDE491A399A5EF5657BC0CF03A1EEB1C685B4C118A83F971F6198A78",
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
      quit()
  except(AttributeError):
    print(f'{R}CPF Gerado nao existe{C}')
    print(f'{R}Pressione enter para retornar{C}')
    lo = input("===>")
    tipos()

def consultacnpj():
    global requests
    import requests, os, time, base64, json, re
    from requests import get
    os.system("clear")
    print("\033[32m######\033[m")
    print("\033[32m#KINY#\033[m")
    print("\033[32m######\033[m")
    print("DIGITE O CNPJ SEM / . OU -")
    cnpj_input = input("\033[32m=====> \033[m")
    requests = requests.get('https://www.receitaws.com.br/v1/cnpj/{}'.format(cnpj_input))
    cnpj_data = requests.json()
    if 'message' not in cnpj_data:
        print("CNPJ: {}".format(cnpj_data['cnpj']))
        print("Nome: {}".format(cnpj_data['nome']))
        print("CEP: {}".format(cnpj_data['cep']))
        print("Telefone: {}".format(cnpj_data['telefone']))
        print("Email: {}".format(cnpj_data['email']))
        print("Situação: {}".format(cnpj_data['situacao']))
        print("Logradouro: {}".format(cnpj_data['logradouro']))
        print("Numero: {}".format(cnpj_data['numero']))
        print("Porte: {}".format(cnpj_data['porte']))
        print("Natureza: {}".format(cnpj_data['natureza_juridica']))
        print("Data de abertura: {}".format(cnpj_data['abertura']))
        print("Tipo: {}".format(cnpj_data['tipo']))
        print("UF: {}".format(cnpj_data['uf']))
        print("Capital: {}".format(cnpj_data['capital_social']))
    else:
        print('{}: CNPJ INVALIDO.'.format(cnpj_input))
    del requests
    print("\nDESEJA CONSULTAR UM NOVO CNPJ? \n{1}Sim\n{2}Nao\n")

    lo = input('===> ')
    if lo == '1' or lo == '01':
        consultacnpj()
    else:
        quit()

def bank():
            global requests
            import requests, os, time, base64, json, re
            from requests import get
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
            del requests	
            print("\nDESEJA CONSULTAR UM NOVO CODIGO BANCARIO? \n{1}Sim\n{2}Nao\n")
            
            kc = input("===> ")
            
            if kc == '01' or kc == '1':
            	bank()
            else:
                os.system("clear")
                quit()

def quit():
        os.system("clear")
        print("\033[32m Arrivederci\033[m")
        exit()

def geradorcnpj():
    global requests
    global cnpj_input
    import requests, os, time, base64, json, re
    from requests import get
    os.system("clear")
    os.system("figlet KINY")
    print(f'{C}[{G}*{C}] Gerando CNPJ...')
    time.sleep(1)
    cnpj=requests.request('GET','http://geradorapp.com/api/v1/cpf/generate?token=f01e0024a26baef3cc53a2ac208dd141').json()
    cnpj2=cnpj['data']['number_formatted']
    cnpj=cnpj['data']['number']
    print(f'{C}[{Y}i{C}] O CNPJ gerado foi: {B}'+cnpj2)
    time.sleep(1)
    print(f'{C}[{G}*{C}] Consultando CNPJ gerado...')
    cnpj_input = cnpj
    consultacnpj()