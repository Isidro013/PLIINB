from __future__ import print_function
from autenticacao import *
from reconhecimento import *
from eventos import *
from edit import *
from day import *
from criar import *
from web import *
from hours import *
import os                       #importa biblioteca do sistema operacional 

autenticacao_google()
lin()
lin()
print("Iniciando PLIINB")
lin()
print("")
print("")
lin()
SERVICE = autenticacao_google()
print("Bem vindo, PLIINB iniciado.")
lin()
sair = False
while not sair:
    print("")
    print("")
    lin()
    print("Como posso ajudar ?")
    print("Escolha um comando")
    lin()
    print("ABRIR, SAIR")
    lin()
    inicio = reconhecimento().lower()
    if inicio == 'abrir':        
        lin()
        print("Essas são as Opções disponíveis: ")
        lin()
        print("Criar Evento diga (Criar)")
        lin()
        print("Consultar compromissos diga (consulta)")
        lin()
        print("Sugestão de Filmes diga (filme)")
        lin()  
        print("Finalizar diga (Sair)")
        lin()
        text = reconhecimento().lower()
        print(text.lower().capitalize())
        if text == 'sair':
            sair = True
        elif text == 'criar':
            criar(SERVICE)
        elif text == 'filme':
            web()
        elif text == 'consulta':
            print("Qual data deseja consultar ?")
            text = reconhecimento().lower()
            SERVICE = autenticacao_google()
            print(text)
            lin()
            eventos(day(text), SERVICE)            
        lin()
    elif inicio == 'sair':
        sair = True
        print("Fechando o Sistema")
    else:
        print("Comando não reconhecido")