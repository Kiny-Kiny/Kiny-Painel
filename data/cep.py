import requests
from data import ui
def consultar():
    Sair = False
    while (Sair == False):
        cep_input = ui.input_dialog()
        if len(cep_input) != 8:
            msg = 'QUANTIDADE DE DIGITOS INVALIDA'
        else:
            request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))
            adress_data = request.json()
            try:
                msg=f'''
Cep: {adress_data['cep']}
Logradouro: {adress_data['logradouro']}
Complemento: {adress_data['complemento']}
Bairro: {adress_data['bairro']}
Cidade: {adress_data["localidade"]}
Estado: {adress_data['uf']}
IBGE: {adress_data['ibge']}
GIA: {adress_data['gia']}
SIAFI: {adress_data['siafi']}
DDD: {adress_data['ddd']}
                '''
            except:
                msg = 'CEP INVALIDO'
        choice = int(ui.dialog_choice(msg))
        if choice == 1:
            pass
        elif choice == 2:
            Sair = True
        else:
            ui.error_dialog('Opção inválida')
