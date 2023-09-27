from removidos import PilhaDeRemovidos

class circuloException(Exception):
    def __init__(self,mensagem):
        super().__init__(mensagem)

#classe que cria os links
class No:
    def __init__(self, carga:any):
        self.__carga = carga
        self.__prox = None
        self.__ant = None
    
    @property
    def carga(self):
        return self.__carga
    
    @property
    def ant(self):
        return self.__ant

    @property
    def prox(self):
        return self.__prox

    @carga.setter
    def carga(self, novaCarga):
        self.__carga = novaCarga

    @ant.setter
    def ant(self, novoAnt):
        self.__ant = novoAnt

    @prox.setter
    def prox(self, novoProx):
        self.__prox = novoProx

    def __str__(self):
        return f'{self.__carga}'




class circulo:

    def __init__(self):
        self.__head = None
        self.__tamanho = 0
        
    def estaVazia(self)->bool:
        return self.__head == None

    def __len__(self)->int:
        return self.__tamanho

    def elemento(self, posicao:int)->any:
        try:
            assert self.estaVazia() == False, 'Não há ninguém'
            assert posicao > 0 and posicao <= len(self), f'Posição {posicao} é inválida para o círculo com {len(self)} pessoas.'

            contador = 1
            cursor = self.__head
            while(len(self) > 1):
                if contador == posicao:
                    return cursor.carga
                cursor = cursor.prox
                contador += 1            
        except AssertionError as ae:
            raise circuloException(ae)

    def inserir(self, posicao:int, carga:any):
        try:
            assert posicao > 0 and posicao <= len(self)+1, f'Posição {posicao} é inválida para a circulo com {len(self)} pessoas'

            # CONDICAO 1: insercao se a circulo estiver vazio
            if (self.estaVazia()):
                self.__head = No(carga)
                self.__tamanho += 1
                return
            
            # CONDICAO 2: insercao na primeira posicao em uma circulo nao vazio
            if ( posicao == 1):
                novo = No(carga)
                novo.prox = self.__head
                self.__head = novo
                self.__tamanho += 1
                return

            # CONDICAO 3: insercao apos a primeira posicao em circulo nao vazio
            cursor = self.__head
            contador = 1
            while ( contador < posicao-1):
                cursor = cursor.prox
                contador += 1

            novo = No(carga)
            novo.prox = cursor.prox
            cursor.prox = novo
            self.__tamanho += 1

        except AssertionError:
            raise circuloException(f'A posicao não pode ser um número negativo ou 0 (zero)')


    def remover(self, posicao:int)->any:
        try:
            assert not self.estaVazia(), 'Círculo vazio'
            assert posicao > 0 and posicao <= len(self), f'Posição {posicao} é inválida para a circulo com {len(self)} pessoas.'

            cursor = self.__head
            contador = 1
            while( contador <= posicao-1) :
                anterior = cursor
                cursor = cursor.prox
                contador+=1

            carga = cursor.carga

            if( posicao == 1):
                self.__head = cursor.prox
            else:
                anterior.prox = cursor.prox

            self.__tamanho -= 1
            return carga
        
        except AssertionError as ae:
            raise circuloException(ae)
        
        
    def __str__(self)->str:
        s = 'head->[ '
        cursor = self.__head
        while( cursor is not None ):
            s += f'{cursor.carga}, '
            cursor = cursor.prox
        s = s.rstrip(', ')
        s += ' ]'
        return s