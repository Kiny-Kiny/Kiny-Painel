from json import loads
from os import system,name
from time import sleep
#############
global R,B,C,G
R='\033[1;31m';B='\033[1;34m';C='\033[1;37m';G='\033[1;32m'
#############
# O código pode não estar limpo, mas tá rápido.
# Vou recodar em JavaScript ou em Ruby quando eu tiver tempo.
#############
try:
	from requests import get
except:
	try:
		from sys import executable
		system(executable+' -m pip install requests')
		from requests import get
	except:
		print('%s[ %s!%s ] Instale manualmente o(s) módulo(s) requests.'%(C,R,C));exit()
		
try:
	ipmenu=get('https://ipwhois.app/json/').text
	ipmenu=loads(ipmenu)
	ipmenu=ipmenu['ip']
except:
	print('%s[%s ! %s] Verifique sua conexão à Internet! \n%s'%(C,R,C))
	exit()

#Api Free pra quem quiser.
api={
'1':'https://brasilapi.com.br/api/ddd/v1/​',
'2':'https://www.receitaws.com.br/v1/cnpj/',
'3':'https://viacep.com.br/ws/',
'4':'https://ipwhois.app/json/',
'5':'https://brasilapi.com.br/api/banks/v1/',
'6':'https://covid19-brazil-api.now.sh/api/report/v1/brazil/uf/​',
'8':'https://lookup.binlist.net/',
'9':'https://www.consultacrm.com.br/api/',
'10':'http://ghostcenter.xyz/api/nome/'
}

'''
http://cnes.datasus.gov.br/pages/profissionais/consulta.jsp
'''

logo='''  __  __     __     __   __     __  __    
 /\ \/ /    /\ \   /\ "-.\ \   /\ \_\ \   
 \ \  _"-.  \ \ \  \ \ \-.  \  \ \____ \  
  \ \_\ \_\  \ \_\  \ \_\\"\_\   \/\_____\ 
   \/_/\/_/   \/_/   \/_/ \/_/   \/_____/ \n'''


########FUNÇÕES########
def req(api_req) -> str: return loads(get(api_req).text)
def clear(clean) -> None: return system(clean)
#######################
def cpf() -> str:
	result=loads(get(r'https://netinapi.space/Pkinyyp/Api%20json/Cpf.php?cpf='+input('%s%s%s\n%s>%s Digite o CPF : '%(B,logo,C,G,C)),verify=False).text)
	clear(clean)
	ban='%s%s%s\n'%(B,logo,C)
	try: return ban+'[ %sNome%s : %s ]\n[ %sCPF%s : %s ]\n[ %sAno de Nascimento%s : %s ]\n[ %sSexo %s: %s ]'%(G,C,result['retorno']['Nome'],G,C,result['retorno']['CPF'],G,C,result['retorno']['AnoNascimento'],G,C,result['retorno']['Sexo'])
	except: return ban+'[ %s!%s ] CPF não encontrado.'%(R,C)

def ip() -> str:
	api_req=api['4']+input('%s%s%s\n%s>%s Digite o Endereço de IP que deseja buscar : '%(B,logo,C,G,C))
	result=req(api_req)
	try:
		return '[%s IP %s: %s ]\n[%s Tipo %s: %s ]\n[%s Continente%s: %s ]\n[%s País %s: %s ]\n[%s Capital %s: %s ]\n[%s Região %s: %s ]\n[%s Cidade %s: %s ]\n[%s DDI %s: %s ]\n[%s Latitude %s: %s ]\n[ %sLongitude%s : %s ]'%(G,C,result['ip'],G,C,result['type'],G,C,result['continent'],G,C,result['country'],G,C,result['country_capital'],G,C,result['region'],G,C,result['city'],G,C,result['country_phone'],G,C,result['latitude'],G,C,result['longitude'])
	except:
		return '%s[ %s!%s ] Endereço de IP não encontrado.'%(C,R,C)
#from time import sleep
def ddd() -> str:
	api_req=req('https://brasilapi.com.br/api/ddd/v1/%s'%input('%s%s%s\n%s>%s Digite o DDD : '%(B,logo,C,G,C)))
	clear(clean)
	try:
		msg='%s%s%s[ %sEstado%s: %s ]\n[ %sCidades%s:'%(B,logo,C,G,C,api_req['state'],G,C)
		for i in api_req['cities']: msg+=str(' '+G+i+','+C)
		return msg
	except Exception:
		#print(r)
		return '[ %s!%s ] DDD não Encontrado.'%(R,C)

def placa() -> str:
	result=loads(get('https://apicarros.com/v2/consultas/%s/f63e1e63dd231083d38ce929984aac7d'%input('%s%s%s\n%s>%s Digite a Placa : '%(B,logo,C,G,C)),verify=False).text)
	msg='%s%s%s\n'%(B,logo,C)
	clear(clean)
	for i in result:
		msg+=str('[ '+G+str(i.upper())+C+ ' : ' + str(result[i]) + ' ]\n').replace('{','\n')
	return msg

def nome() -> str:
	result='http://ghostcenter.xyz/api/nome/%s'%input('%s%s%s\n%s>%s Digite o nome: '%(B,logo,C,G,C))
	result=req(result)
	msg=''
	try:
		for i in range(0, int(len(result['dados']))):
			msg+='''\n[ %sCPF%s : %s ]\n[ %sNome%s : %s ]\n[ %sNascimento%s : %s ]\n[ %sGênero%s : %s ]
'''%(G,C,result['dados'][i]['cpf'],G,C,result['dados'][i]['nome'],G,C,result['dados'][i]['nasc'],G,C,result['dados'][i]['sexo'])
	except Exception as e:
			msg='[ %s!%s ] Nome inválido ou pequeno demais.'%(R,C)
	return msg
def cep() -> str:
	try:
		result=req(api['3']+input('%s%s%s\n%s>%s Digite o CEP : '%(B,logo,C,G,C))+'/json')
		return '[ %sCEP%s : %s ]\n[ %sLogradouro%s : %s]\n[ %sComplemento%s : %s ]\n[ %sBairro%s : %s]\n[ %sLocalidade%s : %s]\n[ %sEstado(UF)%s : %s]\n[ %sIBGE%s : %s]\n[ %sGIA%s : %s]\n[ %sDDD%s : %s]\n[ %sSIAFI%s : %s]'%(G,C,result['cep'],G,C,result['logradouro'],G,C,result['complemento'],G,C,result['bairro'],G,C,result['localidade'],G,C,result['uf'],G,C,result['ibge'],G,C,result['gia'],G,C,result['ddd'],G,C,result['siafi'])
	except:
		error ='[ %s!%s ] CEP Inválido.'%(R,C)
		return error

def covid() -> str:
	result=req(str("https://covid19-brazil-api.now.sh/api/report/v1/brazil/uf/")+str(input('%s%s\n%s>%s Digite o UF : '%(B,logo,G,C))))
	try: return '[ %sEstado%s : %s ]\n[ %sCasos%s : %s ]\n[ %sMortes%s : %s ]\n[ %sSuspeitas%s : %s ]\n[ %sCasos Recusados%s : %s]'%(G,C,result['state'],G,C,result['cases'],G,C,result['deaths'],G,C,result['suspects'],G,C,result['refuses'])
	except Exception: return '[ %s!%s ] Nenhum resultado encontrado para esse UF.'%(R,C)
	
def bank() -> str:
	result=req(api['5']+input('%s%s%s\n%s>%s Digite o código bancário : '%(B,logo,C,G,C)))
	try: return '[ %sISPB%s : %s ]\n[ %sNome%s : %s ]\n[ %sCódigo%s : %s ]\n[ %sNome Completo%s : %s ]'%(G,C,result['ispb'],G,C,result['name'],G,C,result['code'],G,C,result['fullName'])
	except Exception: return '[ %s!%s ] Código bancário inválido.'%(R,C)

def bin() -> str:
	try: result=req('https://lookup.binlist.net/%s'%input('%s%s%s\n%s>%s Digite a BIN : '%(B,logo,C,G,C)));return '[ %sTipo%s : %s ]\n[ %sMarca%s : %s ]\n[ %sPré-Pago%s : %s ]\n[ %sPaís%s : %s ]\n[ %sNome do Banco%s : %s ]\n[ %sTelefone%s : %s ]\n[ %sCidade%s : %s ]'%(G,C,result['type'],G,C,result['brand'],G,C,str(result['prepaid']),G,C,result['country']['name'],G,C,result['bank']['name'],G,C,result['bank']['phone'],G,C,result['bank']['city'])
	except: return '[ %s!%s ] BIN Inválida.'%(R,C)

def cnpj() -> str:
	# preguica ativada
	result=req('https://www.receitaws.com.br/v1/cnpj/%s'%input('%s%s%s\n%s>%s Digite o CNPJ : '%(B,logo,C,G,C)))
	msg=''
	for i in result:
		msg+=str('[ '+G+str(i.upper())+C+ ' : ' + str(result[i]) + ' ]\n')
	return msg

grupo_dict={
'Grupo do WhatsApp': 'https://chat.whatsapp.com/Dnjs8guT97wAJgcZSI6e3c',
'Grupo do Telegram':'https://t.me/kinycrimson',
'Grupo de Consultas - Telegram':'https://t.me/kinycrimsonconsultas',
'Grupo de Consultas - WhatsApp':'https://chat.whatsapp.com/Clfx2AcM7QY8pa5UznUQib',
'Instagram' : '@parziovanni',
'Twitter': 'KinyBruno',
'Youtube': 'https://youtube.com/c/reKINYCRIMSONLOL'}

def grupo() -> str:
	msg=''
	for i in grupo_dict: msg+=str('{ '+G+str(i)+G+' : '+str(grupo_dict[i])+C+' }\n')
	input('%s%s%s\n%s%s'%(B,logo,C,msg,'%s<%s Aperte Enter para voltar ao Menu. %s>%s'%(G,C,G,C)))
	
#######################
def exit() -> None:
	global Exit
	Exit=True

def show_api() -> str:
	msg=''
	for i in api: i='%s{%s '%(B,C)+api[i]+' %s}%s\n'%(B,C);msg+=i
	input('%s%s%s\n === Lista de APIs ===\n%s%s<%s APERTE ENTER PARA VOLTAR AO MENU %s>%s'%(B,logo,C,msg,G,C,G,C))

Exit=False

MatchCase={
'1':ddd,
'2':cnpj,
'3':cep,
'4':ip,
'5':bank,
'6':covid,
'7':placa,
'8':bin,
'9':cpf,
'10':nome}
MatchCase_Function={
'98':grupo,
'99':show_api,
'00':exit
}

def menu() -> None:
	while Exit==False:
		clear(clean)
		option=str(input('''%s%s%s
Bem-Vindo(a) ao %sKinyPainel|Free%s
Seu Endereço de IP : %s%s%s

%s[%s PIX : %s06acdbe2-ccf2-4c14-b8c1-7f0c965f629d %s]

[Telegram : %s@K_iny%s | WhatsApp : %s+55 21 7918-0533%s]
____________________________
|{ %s1%s } Consulta de DDD      |
|{ %s2%s } Consulta de CNPJ     |
|{ %s3%s } Consulta de CEP      |
|{ %s4%s } Consulta de IP       |
|{ %s5%s } Consulta Bancária    |
|{ %s6%s } Covid-19             |
|{ %s7%s } Consulta de Placa    |
|{ %s8%s } Consulta de BIN      |
|{ %s9%s } Consulta de CPF      |
|{ %s10%s } Consulta de Nome    |
|___________________________|
|{ %s99%s } APIs                |
|{ %s98%s } Redes Sociais       |
|{ %s00%s } Sair                |
|___________________________|
>>> %s'''%(B,logo,C,B,C,B,ipmenu,C,C,C,B,C,B,C,B,C,B,C,B,C,B,C,B,C,B,C,B,C,B,C,B,C,B,C,B,C,B,C,B,C,R,C,G)))
		clear(clean)
		try:
			res='%s\n%s'%(MatchCase[option](),'%s<%s Aperte Enter para retornar ao menu %s>%s'%(G,C,G,C))
			input(res)
		except Exception:
			try:
				MatchCase_Function[option]()
			except:
				pass
if __name__=='__main__':
	global clean
	clean ={'nt':'cls','posix':'clear'}[name]
	menu()
