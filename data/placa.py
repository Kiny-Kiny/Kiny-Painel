import requests
from data import ui
def consultar():
    Sair = False
    while(Sair == False):
        placa_input = ui.input_dialog()
        placa_data = requests.get('https://apicarros.com/v1/consulta/{}/json'.format(placa_input), verify = False).json() # JSQ7436
        try:
            if (placa_data['codigoRetorno']) == "0":
                msg=f'''
Ano: {placa_data['ano']}
Data: {placa_data['data']}
Modelo:  {placa_data['modelo']}
Ano do modelo:  {placa_data['anoModelo']}
Cor:  {placa_data['cor']}
Marca:  {placa_data['marca']}
Roubo/furto:  {placa_data['dataAtualizacaoRouboFurto']}
Situa??o:  {placa_data['situacao']}
Placa:  {placa_data['placa']}
Chassi:  {placa_data['chassi']}
UF:  {placa_data['uf']}
Munic?pio:  {placa_data['municipio']}
Modificada em:  {placa_data['dataAtualizacaoCaracteristicasVeiculo']}
Alarme atualizado:  {placa_data['dataAtualizacaoAlarme']}
Mensagem de retorno:  {placa_data['mensagemRetorno']}
C?digo de retorno:  {placa_data['codigoRetorno']}'''
            else:
                msg = 'Limite de consultas atingido ou placa invalida'
        except:
            msg = 'Placa invalida'
        choice = ui.dialog_choice(msg)
        if choice == '1':
            pass
        elif choice == '2':
            Sair = True
        else:
            ui.error_dialog('Opção inválida')