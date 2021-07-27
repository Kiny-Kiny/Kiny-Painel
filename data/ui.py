import os,sys,time
global R,B,C,Y,G,RT,CY,CO
CO='\033[m';R='\033[1;31m';B='\033[1;34m';C='\033[1;37m';CY='\033[1;36m';Y='\033[1;33m';G='\033[1;32m';RT='\033[;0m'
error=f'{C}[{R}ERROR{C}]';warning=f'{C}[{Y}!{C}]';info=f'{C}[{G}i{C}]'
result = os.popen('figlet KINY').read()
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
	clear()
	print(f'''
{result}
-- P  A  I  N  E  L --
{info} Recodado por YATO com a API Thanatos {info}
{warning} Este painel foi disponibilizado gratuitamente. Se pagou por isso, foi enganado. {warning}
       ''')

def restart():
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def dialog(text='',tiled='='):
  clear();banner()
  text = text.split('\n')
  maior = 0
  for txt in text:
    tamanho = len(txt)
    if tamanho > maior:
      maior = tamanho
  print(str(C)+str(G)+tiled+tiled+tiled*maior+tiled+tiled+str(C))
  for txt in text:
    print(str(warning)+' '+txt)
  print(str(C)+str(G)+tiled+tiled+tiled*maior+tiled+tiled+str(C))
  time.sleep(3)

def menu(text='Sem Itens para mostrar.\nModo de teste',messg = 'Digite o numero da opção que deseja.',tiled='='):
  clear();banner()
  text = text.split('\n')
  number = 0
  for txt in text:
    number = number + 1
    if '::' in txt:
      riped = txt.split('::')
      print(str(C)+'['+str(G)+str(number)+str(C)+'] '+riped[0])
      print()
      number = number + 1
      print(str(C)+'['+str(G)+str(number)+str(C)+'] '+riped[1])
    else:
      print(str(C)+'['+str(G)+str(number)+str(C)+'] '+txt)
  print(info+' '+messg)
  return input('===>')

def dialog_choice(text='',messg='Deseja realizar uma nova consulta?',tiled='='):
  clear();banner()
  text = text.split('\n');maior = 0
  for txt in text:
    tamanho = len(txt)
    if tamanho > maior:
      maior = tamanho
  if maior > 2:
    print(tiled+tiled*maior+tiled+tiled)
    for txt in text:
      print(txt)
    print(tiled+tiled*maior+tiled+tiled)
  print(info+' '+messg)
  print(str(C)+'['+str(G)+str(1)+str(C)+']'+' Sim')
  print(str(C)+'['+str(G)+str(2)+str(C)+']'+' Não')
  return input('===>')

def input_dialog(text='',tiled='='):
  clear();banner()
  text = text.split('\n');maior = 0
  for txt in text:
    tamanho = len(txt)
    if tamanho > maior:
      maior = tamanho
  if maior > 2:
    messg = text[0]
  else:
    messg = 'Digite o número ou nome que deseja consultar.'
  print(info+' '+messg)
  return input('===>')

def error_dialog(text='',tiled='='):
  clear();banner()
  text = text.split('\n')
  maior = 0
  for txt in text:
    tamanho = len(txt)
    if tamanho > maior:
      maior = tamanho
  print(str(C)+str(R)+tiled*8+tiled*maior+tiled*8+str(C))
  for txt in text:
    print(str(error)+' '+txt+' '+str(error))
  print(str(C)+str(R)+tiled*8+tiled*maior+tiled*8+str(C))
  time.sleep(3)
