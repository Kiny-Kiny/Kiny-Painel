import requests, os, sys
from data import ui
#Api - https://github.com/gav1x/FullP
def consultar():
	Sair = False
	while(Sair == False):
		msg=''
		numero = ui.input_dialog('Digite o número[Formato: DDD+Numero]: ')
		data = requests.get(url='https://consulta-numero.p.rapidapi.com/apis/astrahvhdeus/Consultas%20Privadas/HTML/numero.php', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36','x-rapidapi-key':'e01238c690msh74f20bdc84d5dcfp122562jsnc9921fa7c4c1','x-rapidapi-host': 'consulta-numero.p.rapidapi.com'}, params={'consulta': numero}).text
		if 'A Consulta Esta Funcionando' in data:
			msg='A consulta está funcionando normalmente, porém, o Telefone inserido não foi encontrado.'
		else:
			msg=data.replace('<p>', '').replace('<br>', '\n').replace('DDD:', 'DDD: ').replace('NOME:', 'Nome completo: ').replace('FONE:', 'Telefone: ').replace('INST:', 'Data de Compra: ').replace('PESSOA:', 'Pessoa: ').replace('CPF:', 'CPF: ').replace('PESSOA:', 'Pessoa: ')
		choice = int(ui.dialog_choice(msg))
		if choice == 1:
			pass
		elif choice == 2:
			Sair = True
		else:
			ui.error_dialog()
