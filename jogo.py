from ListaSimplesmenteEncadeada import *
from PilhaSimplesmenteEncadeada import *
import random

class Jogo:
    def __init__(self):
        """
        No construtor da classe jogo, criamos os atributos jogadores e removidos e instanciamos a lista e a pilha nos mesmos.
        """
        self.__jogadores = Lista()
        self.__removidos = Pilha()


    def __criar__(self, qtdJogadores):
        '''
        Função para a construção da rodada como uma lista.
        '''
        if len(self.__jogadores) <= qtdJogadores:
            rodadaParticipantes = self.__jogadores.inserir
            return rodada


    def __inicializador__(self, qtdVencedores):
        """
        Função que têm a lógica do jogo e todo seu funcionamento.
        """
        j = 1 #o que é esse j?
        rodada = 0

        while len(self.__jogadores) > qtdVencedores:
            rodada += 1 
            print(f'Participantes: {rodadaParticipantes}')
            print(f'Rodada: {rodada}')

            self.__jogadores.preparaPercurso(1)#alterar
            temp =  random.randint(4, 16)
            while (qtdVencedores != qtdJogadores):
                cont = 0
                while(self.__jogadores.temProximo()):
                    carga = self.__jogadores.pedirProximo()
                    print(carga)
                    cont += 1
                    if (cont < len(self.__jogadores)-1):
                        break
                posicao = self.__jogadores.busca(carga)
                self.__removidos.empilha(carga) #aqui teria que ser self.__removidos não? já que ele recebe a pilha/a mesma coia para a lista
                print(f'Removido: {carga}')
                self.__jogadores.remover(posicao)


    def __str__(self)->str:
        '''
        Método que mostra os eliminados 
        '''
        s = 'Eliminados: '
        cursor = self.__topo
        while( cursor is not None ):
            s += f'{cursor.carga}, '
            cursor = cursor.prox
        s = s.rstrip('< ')
        s += ' '
        return s

    def salvar_jogo(nome):
        '''
        Método que salva a rodada do jogo atual.
        '''
        jogo = open('jogo.txt','a')
        jogo.write (str)
        jogo.close()