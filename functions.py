from Classe import *

dog = []
pessoa = []

def criar_cachorro():
    nome = input("Nome do animal: ")
    tamanho = int(input("Tamanho em cm: "))
    raca = input("Raça: ")
    patas = int(input("Quantidade de patas: "))
    cor = input("Cor: ")
    cachorro = Cachorro(nome,cor,tamanho,raca,patas)
    dog.append(cachorro)
    # return cachorro

def criar_humano():
    nome = input("Nome: ")
    idioma = input("Idioma desejado: ")
    cor = input("Informe a cor: ")
    humano = Humano(nome,cor,idioma)
    pessoa.append(humano)
    # return humano

# def listar_cachorro(dog:list):
#     if len(dog) > 0:
#         for cachorro in dog:
#             print(cachorro.info())
#     else:
#         print("Nenhum foi criado ainda!")

def  listar(lista):
    if lista:
        cont = 1
        for i in lista:
            print(f'==== {cont}° ====')
            print(i.info_H())
            cont+=1
            '\n'
    else:
        print("Nenhum foi cachorro criado ainda!")

def  listar_H(lista):
    if lista:
        for i in lista:
            print(i.info_H(),'\n')
    else:
        print("Nenhum foi humano criado ainda!") 

    
def buscar_humano(nome):
 
    for i in pessoa:
        if i.nome == nome:
            print('---------------------')
            print (i.info_H())
            print('---------------------')
        else:
            print('fora')

def buscar_cachorro(nome):

    for i in pessoa:
        if i.nome == nome:
            print (i.info_C())
        else:
            print('fora')
    