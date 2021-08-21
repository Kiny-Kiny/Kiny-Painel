# -*- coding: utf-8 -*-
import sys,os,logging,json
#Pedro gordola
#Necessários
try:import requests;from TerminalButtons import *
except:
    print('Instalando Dependencias')
    os.system(sys.executable + ' -m pip install requests TerminalButtons')
    
try:import curses
except:os.system(sys.executable + ' -m pip install windows-curses')

os.system('cls' if os.name=='nt' else 'clear')

APIS= requests.get('https://raw.githubusercontent.com/Kiny-Kiny/Kiny-Painel/main/source/apis/apis.json').json()
logo= requests.get('https://raw.githubusercontent.com/Kiny-Kiny/Kiny-Painel/main/source/banner/logo').text.split('\n')



class PainelClicavel:
    def Reiniciar(self):
        self.Tb.ClearScreen()
        self.Iniciar()

    def EfetuarRequest(self,api,requested):
        self.Tb.ClearScreen()
        
        if len(APIS[api]) > 2:
            a = APIS[api]
        else:
            self.Tb.CreateButton(text='Realizando Consulta...' + APIS[api][0] + requested)
            a = requests.get(APIS[api][0] + requested).text.replace('<br>','\n')
            self.Tb.ClearScreen()
            a = a.split('\n')
            
        count = 0
        self.Tb.CreateButton(text='Voltar',row=count,commmand=lambda:self.Reiniciar(),fg=curses.COLOR_RED)
        
        for i in a:
            self.Tb.CreateButton(text=i,row=count,positionx=CENTER,fg=curses.COLOR_GREEN)
            count = count + 1

    def reqInputCon(self,api):
        req = None
        if len(APIS[api]) < 3:
            self.Tb.ClearScreen()
            self.Tb.CreateButton(text='Digite o %s :' % api ,fg=curses.COLOR_GREEN)
            self.Tb.CreateButton(text='>' ,fg=curses.COLOR_BLUE,row=1)
            req = self.Tb.ReqInput(1,1)
        self.EfetuarRequest(api,req)

    def CreateConsultasButton(self,text,row,bg):
        self.Tb.CreateButton(text=text.capitalize(),row=row,commmand=lambda:self.reqInputCon(text),positionx=CENTER,fg=bg)

    def CreateConsultas(self,count):
        global APIS
        count = count + 5
        for text in APIS:
            if APIS[text][1] == 'ON':bg=curses.COLOR_GREEN
            else:bg=curses.COLOR_RED
            
            self.CreateConsultasButton(text,count,bg)
            count = count + 1

    #Iniciar GUI
    def Iniciar(self):
        global logo
        
        count = 0
        for i in logo:
            self.Tb.CreateButton(text=i,row=count)
            count = count + 1
        
        self.Tb.CreateButton(text='Coded By:',row=count-1)
        self.Tb.CreateButton(text='None',row=count-1,col=10,fg=curses.COLOR_BLUE)
        self.Tb.CreateButton(text='Versão Touch 1',bg=curses.COLOR_BLUE,row=count,col=10)
        self.Tb.CreateButton(text='Esse programa foi disponibilizado gratuitamente, se você pagou, foi enganado.',bg=curses.COLOR_RED,row=count+2)
        self.Tb.CreateButton(text='Sair',row=count,commmand=self.Tb.Exit,fg=curses.COLOR_RED)
        self.CreateConsultas(count)


    def IniciarGUI(self,std):
        self.Tb = TerminalButtons(std)
        self.Iniciar()
        self.Tb.mainLoop()

    def __init__(self):
        curses.wrapper(self.IniciarGUI)

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
PainelClicavel()



