import requests,time
from data import ui
def consultar():
    Sair = False
    while(Sair == False):
        cpf = str(ui.input_dialog()).replace('.','').replace('-','')
        if len(cpf) != 11 or len(cpf) < 1:
            msg = "error"
        else:
            api = requests.get('https://api.isaaclock.site/data/v1/'+cpf).json() # 00000000272
            try:
                msg=f"""
Nome : {api['fullName']}
CPF : {api['docNumber']}
Nome da Mãe : {api['mae']}
Aniversário : {api['nascAt']}
Estado : {api['uf']}
Cidade : {api['city']}
CEP : {api['cep']}
Logradouro : {api['logra']}
Bairro : {api['bairro']}
Número da Casa: {api['number']}
Complemento : {api['compl']}"""
            except(AttributeError):
                msg = 'Erro no servidor'
            choice = ui.dialog_choice(msg)
            if choice == '1':
                pass
            elif choice == '2':
                Sair = True
            else:
                ui.error_dialog()