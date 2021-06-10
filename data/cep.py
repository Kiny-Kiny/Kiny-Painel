import requests, phonenumbers
from phonenumbers import geocoder, carrier
from data import ui
def consultar():
	Sair = False
	while(Sair == False):
				numero_input = ui.input_dialog()
				if len(numero_input) < 1:
					ui.error_dialog('Digite algo para consultar')
					
				if '55' not in number_input:
					ui.error_dialog('Digite o numero no formato 55219××××××××')
				
				pm = phonenumbers.parse(numero_input)
				op = carrier.name_for_number(pm, 'pt-br')
				es = geocoder.description_for_number(pm, 'pt-br')
				
				numero = f'''
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
