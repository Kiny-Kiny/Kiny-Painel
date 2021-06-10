import requests
from data import ui
def consultar():
    Sair = False
    while(Sair == False):
        bin_input = ui.input_dialog()
        headers = {"Accept-Version": "3",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
        req_data = requests.get('https://lookup.binlist.net/' + bin_input, headers=headers).json()
        try:
            msg=f'''
Bandeira: {req_data['scheme']}
Marca: {req_data['brand']}
Tipo: {req_data['type']}
Pais: {req_data['country']['name']}
Latitude: {req_data['country']['latitude']}
Longitude: {req_data['country']['longitude']}
Moeda: {req_data['country']['currency']}
            '''
            #Emoji: {req_data['country']['emoji']}  
        except:
            msg='Erro! BIN não encontrada!'
        choice = ui.dialog_choice(msg)
        if choice == '1':
            pass
        elif choice == '2':
            Sair = True
        else:
            ui.error_dialog()