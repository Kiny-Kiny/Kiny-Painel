import requests,re,os,sys
from data import ui
# Api - N3X0
def consultar():
    Sair = False
    while(Sair==False):
        cpf = ui.input_dialog()
        r = requests.get(f'http://172.105.159.43/{cpf}').text
        if 'pipo' in r:
        	msg='CPF INVÁLIDO!'
        else:
        	# A preguiça ainda vai me matar
        	msg=a.replace('''"''', '').replace(',','\n').replace('}', '').replace('{', '')
        choice = ui.dialog_choice(msg)
        if choice == '1':
        	pass
        elif choice == '2':
        	Sair=True
        else:
        	ui.error_dialog()

