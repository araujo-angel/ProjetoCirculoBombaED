import numpy as np

class PilhaException(Exception):
    def __init__(self,msg):
        super().__init__(msg)


class PilhaDeRemovidos:
    def __init__(self, size:int=10):
        self.__dado = np.full(size,None)
        self.__topo = -1

    def estaVazia(self)->bool:
        return True if self.__topo==-1 else False
    
    def __len__(self)->int:        
        return self.__topo + 1

    def elemento(self, posicao:int)->any:
        try:
            if self.estaVazia():
                raise PilhaException(f'Ninguém perdeu, ainda!')
            assert posicao > 0 and posicao <= self.__topo + 1
            return self.__dado[posicao-1]
        except TypeError:
            raise PilhaException(f'O tipo de dado para posicao não é um número inteiro')
        except AssertionError:
            raise PilhaException(f'A posicao deve ser um número maior que zero e menor igual a {self.__topo+1}')
        except:
            raise

    def topo(self)->any:
        try:
            return self.__dado[-1]
        except IndexError:
            raise PilhaException(f'Não há perdedores até o momento!')
        except:
            raise


    def empilha(self, carga:any):
        #if self.__topo == len(self.__dado) - 1:
            #raise PilhaException(f'.') Sai?
        self.__topo += 1
        self.__dado[self.__topo] = carga

    
    def __str__(self):
        s = 'Removidos: ['
        for i in range(self.__topo+1):
            s += str(self.__dado[i]) + ','
        s = s.rstrip(',') # remove a última vírgula
        s += ']<-topo'
        return s