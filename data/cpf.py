import requests,re,json
from data import ui
# Api - https://github.com/p0isonBR/ConsultaCPF
def consultar():
    Sair = False
    while(Sair==False):
        cpf = ui.input_dialog()
        cpf = re.sub("[^0-9]+", "", cpf)
        if len(cpf)!=11:
        	ui.error_dialog('CPF INVÁLIDO')
        	Sair=True
        try:
        	r = json.loads(requests.get("https://sherlockconsulta.herokuapp.com/cpf/" + cpf).content.decode())
        	for k, v in r["result"].items():
        		msg=k.replace("_", " ").title() + ": " + v.title()
        except:
        	msg='API offline ou servidor fora do ar.'
        choice = ui.dialog_choice(msg)
        if choice == '1':
            pass
        elif choice == '2':
            Sair = True
        else:
            ui.error_dialog()
