class PilhaException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class No:
    def __init__(self, carga:any):
        self.__carga = carga
        self.__prox = None
    
    @property
    def carga(self)->bool:
        return self.__carga
    
    @property
    def prox(self):
        return self.__prox
    
    @carga.setter
    def carga(self, novaCarga):
        self.__carga = novaCarga

    @prox.setter
    def prox(self, novaCarga):
        self.__prox = novaCarga    
    
    def elemento(self, posicao:int)->any:
        try:
            assert self.estaVazia() == False, 'A pilha está vazia.'
            assert posicao > 0 and posicao <= len(self), f'Posição {posicao} é inválida paara a pilha com {len(self)} elementos.'
            return self.__array[posicao-1]
        except AssertionError as ae:
            raise PilhaException(ae)
    
    def busca(self, key:any)->int:
        for i in range(len(self)):
            if self.__array[i] == key:
                return i+1
        raise PilhaException(f'A chave {key} não está presente na pilha.')
    
    def topo(self)->any:
        if self.estaVazia():
            raise PilhaException('Pilha vazia.')
        return self.__array[self.__topo]
    
    def empilha(self, carga:any):
        if self.__topo == len(self.__array)-1:
            raise PilhaException('Pilha cheia.')
        self.__topo += 1
        self.__array[self.__topo] = carga

    def desempilha(self):
        if self.estaVazia():
            raise PilhaException('Pilha vazia.')
        carga = self.__array[self.__topo]
        self.__topo -= 1
        return carga
    
    def __str__(self) -> str:
        s = '[ '
        for i in range(len(self)):
            s += f'{self.__array[i]}, '
        s = s.rstrip(', ')
        s += ' ]<-topo'
        return s
    
    
