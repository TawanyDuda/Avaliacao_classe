class Animal:
    vida = bool
    nome = ''
    cor = ''
    racional = bool

    def __init__(self,_vida,_nome,_cor,_racional):
        self.vida = _vida
        self.nome = _nome
        self.cor = _cor      
        self.racional = _racional
    
    def info(self):
        return {'nome': self.nome}

class Humano (Animal):

    idioma = ''
    
    def __init__(self,_nome, _cor,_idioma = None):
        super().__init__(True,_nome,_cor,False)
        
        self.idioma = _idioma


# Homos001 = Humano('João','Pardo','Libras')
# Homos002 = Humano('Maria','Branco','Português')

class Cachorro(Animal):
    tamanho = int
    raca = str
    patas = int

    def __init__(self,_nome,_cor, _tamanho = int, _raca = None, _patas = int):
        super().__init__(True,_nome,_cor,False)
        self.tamanho = _tamanho
        self.raca = _raca
        self.patas = _patas
    

# cobaia_001 = Cachorro('Jack',30,'Branco','Sheltie',3)
# cobaia_002 = Cachorro('Canino',25,'Preto','vira-lata',4)


# print(cobaia_001.nome)
# print(cobaia_002.nome)

# print(Homos001.nome)
# print(Homos002.nome)

        
        
