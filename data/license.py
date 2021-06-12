from data import ui
def license():
	cu = 'eminel.txt'
	file = open(f'{cu}', 'r')
	file.seek(0, 0)
	print(file.read())
	file.close()
	pause = input('   PRESS ENTER')
	pass
