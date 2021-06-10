import requests
from data import ui
def consultar():
    Sair = False
    while(Sair == False):
        crm_input = ui.input_dialog('Digite o CRM.')
        uf_input = ui.input_dialog('Digite o UF.')
        token = 5072097263
        try:
            crm_data = requests.get('https://www.consultacrm.com.br/api/index.php?tipo=crm&uf='+uf_input+'&q='+str(crm_input)+'&chave='+str(token)+'&destino=json').json()
        except:
            msg =  'CRM ou UF invalido'
            limite = int(crm_data['api_limite']);consultas= int(crm_data['api_consultas']);restantes = int(limite - consultas) 
        if (crm_data['status']) == "true":
            try:
                msg = f'''
CRM: {crm_data["item"][0]["numero"]}
Nome: {crm_data["item"][0]["nome"]}
UF: {crm_data["item"][0]["uf"]}
Situacao: {crm_data["item"][0]["situacao"]}
Profiss?o: {crm_data["item"][0]["profissao"]}
Consultas restantes = {restantes}
                '''
            except:
                msg = 'Erro! dados invalidos!'
        else:
            msg = 'CRM invalido'
        choice = ui.dialog_choice(msg)
        if choice == '1':
            pass
        elif choice == '2':
            Sair = True
        else:
            ui.error_dialog()