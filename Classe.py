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

    # def info(self):
    #     return {'nome': self.nome},{'cor':self.cor}

class Humano (Animal):

    idioma = ''
    
    def __init__(self,_nome, _cor,_idioma = None):
        super().__init__(True,_nome,_cor,False)
        
        self.idioma = _idioma

    def info_H(self):
        return f'nome: {self.nome}\ncor: {self.cor}\nidioma: {self.idioma}'
    def andar(self):
        print('Você está andando!')
        
    
    def correr(self):
        print('Você está correndo!' )
    
    def parar(self):
        print('Você parou!')

    def dormir(self):
        print('Você foi dormir')



# Homos001 = Humano('João','Pardo','Libras')
# Homos002 = Humano('Maria','Branco','Português')

class Cachorro(Animal):
    tamanho = float
    raca = str
    patas = int

    def __init__(self,_nome,_cor, _tamanho = float, _raca = None, _patas = int):
        super().__init__(True,_nome,_cor,False)
        self.tamanho = _tamanho
        self.raca = _raca
        self.patas = _patas
    
    def info_C(self):
        return {f'nome: {self.nome}\ncor: {self.cor}tamanho: {self.tamanho},raca: {self.raca},patas: {self.patas}'}

    def andar(self):
        print('Seu dog está andando!')
        
    def latir(self):
        print('Seu dog está latindo!')
        
    def brincar(self):
        print('Seu dog está brincando!')

    def comer(self):
        print('Seu dog está comendo!')
    
    def dormir(self):
        print('Seu dog foi dormir!')
    

# cobaia_001 = Cachorro('Jack',30,'Branco','Sheltie',3)
# cobaia_002 = Cachorro('Canino',25,'Preto','vira-lata',4)


# print(cobaia_001.nome)
# print(cobaia_002.nome)

# print(Homos001.nome)
# print(Homos002.nome)

        
        
