global R, B, C, Y, G, RT, CY, CO
CO = '\033[m'
R = '\033[1;31m'
B = '\033[1;34m'
C = '\033[1;37m'
CY = '\033[1;36m'
Y = '\033[1;33m'
G = '\033[1;32m'
RT = '\033[;0m'

import os
import sys
import pyfiglet
result = pyfiglet.figlet_format("Kiny", font = "cosmic"  )
def chat():
	os.system("pkg install irssi -y")
	os.system("clear")
	print(f'{C}{G}{result}{C}')
	print(f'{C}[{Y}i{C}] TUTORIAL DE COMO ENTRAR NO CHAT')
	print(f'{C}[{R}+{C}] RECOMENDO O USO DE VPN')
	print()
	print(f'{C}[{G}i{C}] /connect chat.freenode.net') 
	print(f'{C}[{G}i{C}] /nick (seu nickname)')
	print(f'{C}[{G}i{C}] /join #Kiny')
	print(f'{C}[{R}i{C}] Quando for sair, digite /exit')
	pause = input(f'{C}{Y}APERTE ENTER PARA IR PRO CHAT{C}')
	os.system("irssi")
	pass
