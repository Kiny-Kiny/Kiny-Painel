from data import ui
def show():
	file = open('eminel.txt','r')
	print(file.read());
	file.close()
	pause = ui.input_dialog('pressione enter para retornar')
