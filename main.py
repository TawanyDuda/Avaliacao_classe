from Classe import *
from Views import *
from functions import *
import os

while True:

    menu_principal()
    op = int(input("Informe sua escolha: "))
    if op == 0:
        print("Sua sessão foi encerrada!\n    Volte sempre!")
        break 
    elif op == 1:
        menu_humano()
        op = int(input("Informe sua escolha: "))
        if op == 0:
            continue
        elif op == 1:
            result = criar_humano()
            print("Seu humaninho foi criado!")
        elif op == 2 :
            print("==========Info==========")
            result = listar(pessoa)
            print("========================")
        elif op == 3:
            nome = input("Nome do humano: ")
            buscar_humano(nome)
        elif op == 4:
            esc = int(input('Escolha o Humano'))-1
            result = interacoes_humano()
            op = int(input("Informe sua escolha: "))
            if op == 1:
                print(f'A pessoa {pessoa[esc].nome}')
                humano = pessoa[esc]
                humano.andar()
            elif op == 2:
                humano = pessoa[esc]
                humano.correr()
            elif op == 3:
                humano = pessoa[esc]
                humano.parar()
            elif op == 4:
                humano = pessoa[esc]
                humano.dormir()
            else:
                print("Não existe essa opção!")
    elif op == 2:
        menu_cachorro()
        op = int(input("Informe sua escolha: "))
        if op == 0:
            pass
        elif op == 1:
            result = criar_cachorro()
            print("Seu cachorrinho foi criado!")
        elif op == 2:
            listar(dog)
        elif op == 3:
            nome = input("Nome do cachorro: ")
            buscar_cachorro(nome)
        elif op == 4:
            os.system('cls')
            
            result = interacoes_cachorro()
            op = int(input("Informe sua escolha: "))

            if op == 1:
                cachorro = dog[0]
                cachorro.andar()
            elif op == 2:
                cachorro = dog[0]
                cachorro.latir()
            elif op == 3:
                cachorro = dog[0]
                cachorro.brincar()
            elif op == 4:
                cachorro = dog[0]
                cachorro.comer()
            elif op == 5:
                cachorro = dog[0]
                cachorro.dormir()
            else:
                print("Não existe essa opção!")
    else:
        os.system('cls')
        print("Não ta certo!")
