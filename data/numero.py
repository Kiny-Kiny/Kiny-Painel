import requests, phonenumbers
from phonenumbers import geocoder, carrier
from data import ui
def consultar():
	Sair = False
	while(Sair == False):
		msg=''
		numero = str(ui.input_dialog())
		if len(str(numero)) < 1:
			ui.error_dialog('Digite algo para consultar')
		elif len(str(numero)) > 1 and	len(str(numero)) <= 12:
			ui.error_dialog('Formato incorreto')
		elif '+55' not in str(numero):
			ui.error_dialog('Digite o numero no formato +55219××××××××')
			Sair = True
		else:
			try:
				pm = phonenumbers.parse(numero)
				op = carrier.name_for_number(pm, 'pt-br')
				es = geocoder.description_for_number(pm, 'pt-br')
				msg = f'''
Numero: {pm}
Estado: {es}
Operadora: {op}
'''
			except Exception as e:
				ui.error_dialog('Ocorreu um erro: ',e)
		choice = int(ui.dialog_choice(msg))
		if choice == 1:
			pass
		elif choice == 2:
			Sair = True
		else:
			ui.error_dialog()
