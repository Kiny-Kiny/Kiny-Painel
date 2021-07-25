import requests,re
from data import ui
# Api - https://github.com/gav1x/FullP
def consultar():
    Sair = False
    while(Sair==False):
        cpf = ui.input_dialog()
        url: str = 'https://consulta-cpf2.p.rapidapi.com/apis/astrahvhdeus/Consultas%20Privadas/HTML/cpf.php'
        params: str = {'consulta': cpf}
        headers: str = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36',
        'x-rapidapi-key': '0d66cf70c4msh8e71af69887c685p1a9b2fjsn8fc892e8b730',
        'x-rapidapi-host': 'consulta-cpf2.p.rapidapi.com'
        }
        req: str = requests.get(url=url, headers=headers, params=params)
        ret = req.text
        if 'A Consulta Esta Funcionando Normalmente' in ret:
        	msg='A consulta está funcionando normalmente, porém, o CPF inserido não foi encontrado.'
        else:
        	arquivo = open(f'ConsultaCPF_{cpf}.html', 'w', encoding='utf-8')
        	arquivo.writelines(ret)
        	arquivo.close()
        	msg='Sua consulta foi salvo em um arquivo HTML'
        choice = ui.dialog_choice(msg)
        if choice == '1':
        	pass
        elif choice == '2':
        	Sair=True
        else:
        	ui.error_dialog()
