import requests,re,os,sys
from data import ui
# Api - Lukazinn
def consultar():
    Sair = False
    while(Sair==False):
        cpf = ui.input_dialog()
        r = requests.get(f'https://lukazinnapi.000webhostapp.com/Kiny-api/cpf.php?cpf={cpf}').text
        if 'A Consulta' in cpf:
        	msg='A consulta está funcionando normalmente, porém o CPF não foi encontrado.'
        else:
        	# Preguiça é o nome
        	msg=a.replace('''"''', '').replace(',','\n').replace('}', '').replace('{', '')
        choice = ui.dialog_choice(msg)
        if choice == '1':
        	pass
        elif choice == '2':
        	Sair=True
        else:
        	ui.error_dialog()

