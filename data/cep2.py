import requests,re,os,sys
from data import ui
def consultar():
    Sair = False
    while(Sair==False):
        cep = ui.input_dialog()
        r = requests.get(url='https://consulta-cep1.p.rapidapi.com/apis/astrahvhdeus/Consultas%20Privadas/HTML/cep.php', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36','x-rapidapi-key':'e01238c690msh74f20bdc84d5dcfp122562jsnc9921fa7c4c1','x-rapidapi-host': 'consulta-cep1.p.rapidapi.com'},params={'consulta': cep}).text
        if 'A Consulta' in r:
        	msg='CEP INVÁLIDO'
        else:
        	msg=r.replace('<br>', '\n').replace('<p>','')
        choice = ui.dialog_choice(msg)
        if choice == '1':
        	pass
        elif choice == '2':
        	Sair=True
        else:
        	ui.error_dialog()
