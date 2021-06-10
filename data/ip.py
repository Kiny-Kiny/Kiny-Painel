import requests
from data import ui
def consultar(token='25d800a8b8e8b99d77c809567aa291b8',self=0):
    Sair = False
    while(Sair == False):
        if self == 1:
            ip_input = ''
        else:
            ip_input = ui.input_dialog()
            if len(ip_input) < 1:
                ui.error_dialog('Insira algo para consultar.');break
    
        try:
            api=requests.get('http://ipwhois.app/json/'+ip_input).json()
            #lat = api['latitude']
            #lon = api['longitude']
            #api2 = requests.get('http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={token[2]}')
        except:
            msg = "erro no servidor"
        try:
            msg=f'''
IP: {api['ip']}
TIPO: {api['type']}
CONTINENTE: {api['continent']}
C?DIGO DO CONTINENTE: {api['continent_code']}
PAIS: {api['country']}
C?DIGO DO PA?S: {api['country']}
CAPITAL DO PAIS: {api['country_capital']}
C?DIGO TELEF?NICO DO PA?S: {api['country_phone']}
PAISES VIZINHOS: {api['country_neighbours']}
REGI?O: {api['region']}
CIDADE: {api['city']}
LATITUDE: {api['latitude']}
LONGITUDE: {api['longitude']}
ASN: {api['asn']}
ORG: {api['org']}
ISP: {api['isp']}
HOR?RIO PADR?O: {api['timezone']}
NOME DO HOR?RIO PADR?O: {api['timezone_name']}
GMT: {api['timezone_gmt']}
MOEDA: {api['currency']}
CODIGO DA MOEDA: {api['currency_code']}
SIMBOLO DA MOEDA: {api['currency_symbol']}
            '''
            #TEMPERATURA: {api2["weather"][0]["main"]}
        except:
            msg = 'Ip invalido.'
        choice = int(ui.dialog_choice(msg))
        if choice == 1:
            pass
        elif choice == 2:
            Sair = True
        else:
            ui.error_dialog()