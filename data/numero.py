import requests, phonenumbers
from phonenumbers import geocoder, carrier
from data import ui
def consultar():
	Sair = False
	while(Sair == False):
		numero = ui.input_dialog()
		if len(numero) < 1:
			ui.error_dialog('Digite algo para consultar')
		if len(numero) > 1 and len(numero) < 12:
			ui.error_dialog('Formato incorreto')
		if '+55' not in numero:
			ui.error_dialog('Digite o numero no formato +55219××××××××')
			pass
		try:
			pm = phonenumbers.parse(numero)
			op = carrier.name_for_number(pm, 'pt-br')
			es = geocoder.description_for_number(pm, 'pt-br')
		except Exception as e:
			ui.error_dialog('Ocorreu um erro: ',e)
		msg = f'''
Numero: {pm}
Estado: {es}
Operadora: {op}
'''
		choice = int(ui.dialog_choice(msg))
		if choice == 1:
			pass
		elif choice == 2:
			Sair = True
		else:
			ui.error_dialog()
