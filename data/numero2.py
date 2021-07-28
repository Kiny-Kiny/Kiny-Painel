import requests, os, sys
from data import ui
#Api - http://consultafree.com
def consultar():
	Sair = False
	while(Sair == False):
		msg=''
		numero = int(ui.input_dialog('Digite o número[Formato: DDD+Numero]: '))
		data =requests.get(url = f'http://consultafree.com/dashboard/bases/localize/telefone/api.php?telefone={numero}', headers=h = {'Host': 'consultafree.com','Connection': 'keep-alive','Upgrade-Insecure-Requests': '1','User-Agent': 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Mobile Safari/537.36','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','Sec-GPC': '1','Referer': 'http://consultafree.com/dashboard/bases/localize/cpf/index.php','Accept-Encoding': 'gzip, deflate','Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7','Cookie': 'PHPSESSID=emmnl6naec2drce61252kmi9h4'}).text
		data = data.split('<!DOCTYPE')[0]
		msg = data.replace('<br>','')
		choice = int(ui.dialog_choice(msg))
		if choice == 1:
			pass
		elif choice == 2:
			Sair = True
		else:
			ui.error_dialog()
