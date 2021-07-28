import requests,re,os,sys
from data import ui
# Api - https://github.com/gav1x/FullP
def consultar():
    Sair = False
    while(Sair==False):
        nome = ui.input_dialog()
        r =requests.get(url='https://consulta-nome1.p.rapidapi.com/apis/astrahvhdeus/Consultas%20Privadas/HTML/nome.php', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36','x-rapidapi-key': '9353b1d886msh73e7a0771d6600dp14ec4cjsn883fd8b4cf13','x-rapidapi-host': 'consulta-nome1.p.rapidapi.com'}, params={'consulta': nome}).text
        if 'A Consulta Esta Funcionando Normalmente' in r:
        	msg='A consulta está funcionando normalmente, porém, o CPF inserido não foi encontrado.'
        else:
        	msg=r.replace('<br>', '\n').replace('<p>','')
        choice = ui.dialog_choice(msg)
        if choice == '1':
        	pass
        elif choice == '2':
        	Sair=True
        else:
        	ui.error_dialog()
