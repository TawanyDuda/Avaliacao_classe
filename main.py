from Classe import *
from Views import *

dog = []
pessoa = []

def criar_cachorro():
    nome = input("Nome do animal: ")
    tamanho = int(input("Tamanho em cm: "))
    raca = input("Raça: ")
    patas = int(input("Quantidade de patas: "))
    cor = input("Cor: ")
    cachorro = Cachorro(nome,cor,tamanho,raca,patas)
    dog.append(cachorro.nome)
    # return cachorro

def criar_humano():
    nome = input("Nome: ")
    idioma = input("Idioma desejado: ")
    cor = input("Informe a cor: ")
    humano = Humano(nome,cor,idioma)
    pessoa.append(humano.nome)
    # return humano

def listar():
    for cachorro in dog:
        print(cachorro.info())

def listar_cachorros():
    print(dog)
def listar_humanos():
    print(pessoa)
# -------INTERAÇOES CACHORRO-------------
def andar():
    print('Seu dog está andando!')
        
def latir():
    print('Seu dog está latindo!')
        
def brincar():
    print('Seu dog está brincando!')

def comer():
    print('Seu dog está comendo!')
    
def dormir():
    print('Seu dog foi dormir!')

# ----------INTERAÇOES HUMANO-------------
    
def andar(self):
    print('Você está andando!')
    
def correr(self):
    print('Você está correndo!' )
    
def parar(self):
    print('Você parou!')

def dormir(self):
    print('Você foi dormir')

while True:

    menu_principal()
    op = int(input("Informe sua escolha: "))
    if op == 0:
        print("Sua sessão foi encerrada!\n    Volte sempre!")
        break 
    elif op == 1:
        menu_humano()
        op = int(input("Informe sua escolha: "))
        if op ==1:
            result = criar_humano()
            print("Seu humaninho foi criado!")
        elif op == 2 :
            result = listar_humanos()
        elif op == 3:
            result = interacoes_humano()
            op = int(input("Informe sua escolha: "))

    elif op == 2:
        menu_cachorro()
        op = int(input("Informe sua escolha: "))
        if op == 0:
            pass
        elif op == 1:
            result = criar_cachorro()
            print("Seu cachorrinho foi criado!")
        elif op == 2:
            result = listar()
        elif op == 3:
            result = interacoes_cachorro()
            op = int(input("Informe sua escolha: "))
    else:
        pass