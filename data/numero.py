import requests
from data import ui
#Api - https://github.com/gav1x/FullP
def consultar():
	Sair = False
	while(Sair == False):
		msg=''
		numero = str(ui.input_dialog())
		url: str = 'https://consulta-numero.p.rapidapi.com/apis/astrahvhdeus/Consultas%20Privadas/HTML/numero.php'
		params: str = {'consulta': numero}
		headers: str = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36',
		'x-rapidapi-key':'0d66cf70c4msh8e71af69887c685p1a9b2fjsn8fc892e8b730',
		'x-rapidapi-host': 'consulta-numero.p.rapidapi.com'
		}
		req: str = requests.get(url=url, headers=headers, params=params)
		ret = req.text
		if len(str(numero)) < 1:
			ui.error_dialog('Digite algo para consultar')
		elif len(str(numero)) > 1 and	len(str(numero)) <= 11:
			ui.error_dialog('Formato incorreto')
		else:
		      if 'A Consulta Esta Funcionando Normalmente' in ret:
		      	ui.error_dialog('A Consulta Esta Funcionando Normalmente, Porem O Telefone Inserido Nao Foi Encontrado.')
		      else:
		      	arquivo = open(f'numero {numero}.html', 'w', encoding='utf-8')
		      	arquivo.writelines(ret)
		      	arquivo.close()
		      	msg='Sua consulta foi salva em um arquivo HTML'
		choice = int(ui.dialog_choice(msg))
		if choice == 1:
			pass
		elif choice == 2:
			Sair = True
		else:
			ui.error_dialog()
