import requests,time
from data import ui
# Pq tá olhando aqui? Veio roubar a API?
def consultar():
    Sair = False
    while(Sair == False):
        cpf = str(ui.input_dialog()).replace('.','').replace('-','')
        if len(cpf) != 11 or len(cpf) < 1:
            msg = "error"
        else:
            api = requests.get('http://45.56.74.86:9547/'+cpf).json() # 00000000272
            try:
                msg=f"""
Nome : {api['nomeCompleto']}
CPF : {api['cpf']}
Nome da Mãe : {api['nomeMae']}
Aniversário : {api['dataNascimento']}
Estado : {api['estado']}
Cidade : {api['cidade']}
CEP : {api['cep']}
Logradouro : {api['logradouro']}
Bairro : {api['bairro']}
Número da Casa: {api['numero']}
Complemento : {api['complemento']}"""
            except(AttributeError):
                msg = 'Erro no servidor'
            choice = ui.dialog_choice(msg)
            if choice == '1':
                pass
            elif choice == '2':
                Sair = True
            else:
                ui.error_dialog()
