import re
import time
import os
import platform

def clear():
   if platform.system() == "Windows":
      os.system("cls")
   elif platform.system() == "Linux":
      os.system("clear")
   else:
       os.system("clear")

R='\033[1;31m'; B='\033[1;34m'; C='\033[1;37m'; Y='\033[1;33m'; G='\033[1;32m'; RT='\033[;0m'

code_info = C + '[' + Y + 'i' + C + '] '
code_details = C + '[' + G + '*' + C + '] '
code_result = C + '[' + G + '+' + C + '] '
code_error = C + '[' + R + '!' + C + '] '

arquivo = r'banco.txt'
ler = open(arquivo, encoding="UTF-8")
conteudo_arquivo = ler.read()

def main():
   clear()
   print("\n" + code_info + "Nome.")
   print(f'''
{C}[{G}i{C}] Formas de operação: 

[{G}1{C}] Consultar nome.
[{G}2{C}] Banco de dados.
[{G}3{C}] Sair.
''')
   tool=input(f'{C}[{G}+{C}] Selecione a forma de operação:{B} ')
   if tool == "1":
        consultar()
   elif tool == "2":
        dados()
   elif tool == "3":
        import consulta
        pass()    
   else:
        clear()
        print(f'{C}[{R}-{C}] Seleção inválida.')
        time.sleep(0.2)
        main()

def dados():
   clear()
   print("\n" + code_info + "Banco de dados.")
   print(f'''
{C}[{G}i{C}] Formas de operação: 

[{G}1{C}] Geral.
[{G}2{C}] Todos os nomes.
[{G}3{C}] Buscar nome
[{G}4{C}] Voltar.
''')
   tool=input(f'{C}[{G}+{C}] Selecione a forma de operação:{B} ')
   if tool == "1":
        banco()
   elif tool == "2":
        nomes()
   elif tool == "3":
        buscar()
   elif tool == "4":
        pass
   else:
        clear()
        print(f'{C}[{R}-{C}] Seleção inválida.')
        time.sleep(0.2)
        main()

def nova():
    nova=input('\n' + f'{C}[{G}+{C}] Deseja realizar uma nova consulta?[{G}s{C}/{R}n{C}]: ').lower()
    if nova=='s' or nova=='sim':
       clear()
       main()
    else:
        clear()
        print(f'\n{G}[PAISLEY PARK]{C}\n')
        exit()

def nova2():
    nova=input('\n' + f'{C}[{G}+{C}] Deseja realizar uma nova consulta?[{G}s{C}/{R}n{C}]: ').lower()
    if nova=='s' or nova=='sim':
       clear()
       main()
    else:
        print(f'\n{G}[PAISLEY PARK]{C}\n')
        exit()

def banco():
    filtro = r'[A-Za-záàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ \S]+'
    banco = re.findall(filtro, conteudo_arquivo)
    converted_list = [x.upper() for x in banco]
    clear()
    print("\n" + code_info + f"Encontrados:{B}\n")
    string = '\n'.join([str (elem) for elem in converted_list])
    print(string)
    print("\n" + code_info + f"Banco de dados (Nome completo; CPF; Data de nascimento).{B}\n") 
    print(f'{code_result}Resultado:{G}', len(banco), f"{C}")
    nova()

def nomes():
    i = 1;
    filtro = r'[A-Za-zâáàâãêéèêíïóôõöúçñÂÁÀÂÃÊÉÈÍÏÓÔÕÖÚÇÑ ]+'
    nomes = re.findall(filtro, conteudo_arquivo)
    while i < len(nomes):
       del nomes[i]
       i=i+1
    converted_list = [x.upper() for x in nomes]
    clear()
    print("\n" + code_info + f"Encontrados:{B}\n")
    string = '\n'.join([str (elem) for elem in converted_list])
    print(string)
    print("\n" + code_info + "Banco de dados (todos os nomes).")
    print(f'{code_result}Resultado:{G}', len(nomes), f"{C}")
    nova()

def buscar():
    i = 1;
    filtro = r'[A-Za-zâáàâãêéèêíïóôõöúçñÂÁÀÂÃÊÉÈÍÏÓÔÕÖÚÇÑ ]+'
    nomes = re.findall(filtro, conteudo_arquivo)
    while i < len(nomes):
       del nomes[i]
       i=i+1
    converted_list = [x.upper() for x in nomes]
    string = '\n'.join([str (elem) for elem in converted_list])

    name = input(f'{C}[{G}*{C}] Informe o nome ({R}recomendação:{C} nome completo): {B}').upper()
    filtro = f'{name}[A-Za-záàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ \S]+'
    banco = re.findall(filtro, string)
    st = '\n'.join([str (elem) for elem in banco])
    clear()
    print("\n" + code_info + f"Encontrados:{B}\n")
    print(st)
    print("\n" + code_info + "Banco de dados (Nome completo).")
    print(f'{code_result}Resultado:{G}', len(banco), f"{C}")
    nova()

def consultar():
    filtro = r'[A-Za-záàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ \S]+'
    banco = re.findall(filtro, conteudo_arquivo)
    converted_list = [x.upper() for x in banco]
    string = '\n'.join([str (elem) for elem in converted_list])

    name = input(f'{C}[{G}*{C}] Informe o nome ({R}recomendação:{C} nome completo): {B}').upper()
    filtro = f'{name}[A-Za-záàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ \S]+'
    banco = re.findall(filtro, string)
    st = '\n'.join([str (elem) for elem in banco])
    clear()
    print("\n" + code_info + f"Encontrados:{B}\n")
    print(st)
    print("\n" + code_info + "Banco de dados (Nome completo; CPF; Data de nascimento).")
    print(f'{code_result}Resultado:{G}', len(banco), f"{C}")
    nova2()

main()
