import requests,os
from data import ui
def consultar():
    Sair = False
    while(Sair==False):
        cpf_input = ui.input_dialog()
        data = requests.get('http://api.trackear.com.br/basepv/cpf/{}/noip'.format(cpf_input)).json()
        try:
        	msg = f"""
CPF: {data['cpf']}
Nome: {data['nome']}
Sexo: {data['sexo']}
Data de Nascimento: {data['dtNascimento']}
Idade: {data['idade']}
Data da Consulta: {data['dtConsulta']}"""
        except:
            msg = "CPF INVÁLIDO OU SERVIDOR FORA DO AR."
        choice = ui.dialog_choice(msg)
        if choice == '1':
            pass
        elif choice == '2':
            Sair = True
        else:
            ui.error_dialog()
