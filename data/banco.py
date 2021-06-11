import requests
from data import ui
def consultar():
    Sair = False
    while(Sair == False):
        bank_input = ui.input_dialog()
        try:
            bank_data = requests.get('https://brasilapi.com.br/api/banks/v1/{}'.format(bank_input)).json()
            if 'message' not in bank_data:
                msg= f'''
Codigo bancário: {bank_data['code']}
Nome: {bank_data['name']}
Nome completo: {bank_data['fullName']}
ISPB: {bank_data['ispb']}
                '''
            else:
                msg = f'{bank_input}: C?digo banc?rio inv?lido.'
        except:
            msg='Erro no servidor'
        choice = ui.dialog_choice(msg)
        if choice == '1':
            pass
        elif choice == '2':
            Sair = True
        else:
            ui.error_dialog('Opção inválida')
