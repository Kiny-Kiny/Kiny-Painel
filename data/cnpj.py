import requests
from data import ui
def consultar():
    Sair = False
    while(Sair == False):
        cnpj_input = ui.input_dialog()
        msg=''
        try:
            cnpj_data = requests.get('https://www.receitaws.com.br/v1/cnpj/{}'.format(cnpj_input)).json()
        except:
            ui.error_dialog('Erro no servidor')
        if cnpj_data['status'] != "ERROR":
            msg=f"""
CNPJ: {cnpj_data['cnpj']}
            """
            message=f"""
Atividade principal: {cnpj_data['atividade_principal'][0]['text']}
Nome: {cnpj_data['nome']}
CEP: {cnpj_data['cep']}
            """
            msg = msg + message
            try:
                message=f"\nTelefone: {cnpj_data['telefone']}"
                msg = msg + message
            except:
                pass
            try:
                message=f"\nEmail: {cnpj_data['email']}"
                msg = msg + message
            except:
                pass
            message=f"""
Situa??o: {cnpj_data['situacao']}
UF: {cnpj_data['uf']}
Municipio: {cnpj_data['municipio']}
Logradouro: {cnpj_data['logradouro']}
Numero: {cnpj_data['numero']}
Complemento: {cnpj_data['complemento']}
Porte: {cnpj_data['porte']}
Natureza: {cnpj_data['natureza_juridica']}
Data de abertura: {cnpj_data['abertura']}
Tipo: {cnpj_data['tipo']}
Capital: {cnpj_data['capital_social']}
            """
            msg = msg + message
            for i in range(0,10):
                try:
                    message=f"""
\nPessoal: {cnpj_data['qsa'][i]['nome']}
Cargo: {cnpj_data['qsa'][i]['qual']}
                    """
                    msg = msg + message
                except:
                    pass
        else:
            mensage=cnpj_data['message']
            msg=f'ERRO!\nCNPJ: {cnpj_input}\nCNPJ invalido/Sem dados.\nMotivo: {mensage}'
        choice = ui.dialog_choice(msg)
        if choice == '1':
            pass
        elif choice == '2':
            Sair = True
        else:
            ui.error_dialog()