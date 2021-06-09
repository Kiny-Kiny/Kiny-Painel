global R, B, C, Y, G, RT, CY, CO
CO = '\033[m'
R = '\033[1;31m'
B = '\033[1;34m'
C = '\033[1;37m'
CY = '\033[1;36m'
Y = '\033[1;33m'
G = '\033[1;32m'
RT = '\033[;0m'
import requests
import os
import sys
import pyfiglet
result = pyfiglet.figlet_format("Kiny", font = "cosmic"  )

def kiny_infoga():
    os.system("apt install nmap whois -y")
    clear()
    print(f'{C}{G}{result}{C}')
    print()
    j = input("1 para HTTPS, 2 para HTTP:")
    k = input("Domain: ")
    if j == '1':
        print("URL: ""https://www." + k)
        os.system("nmap " + k)
        os.system("whois " + k)
    print()
    if j == '2':
        print("URL: ""http://www." + k)
        os.system("nmap " + k)
        os.system("whois " + k)
    print("Pressione enter para voltar.")
    pause = input("====>")
