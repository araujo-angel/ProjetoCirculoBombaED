from ListaEncadeadaCircular import *
from PilhaSimplesmenteEncadeada import *
import random

class Jogo:
    def __init__(self):
        """
        No construtor da classe jogo, criamos os atributos jogadores e removidos e instanciamos a lista e a pilha nos mesmos.
        """
        self.__jogadores = Lista() #Aqui nossa lista é instanciada
        self.__removidos = Pilha() #Aqui nossa pilha é instanciada
        self.__qtdVencedores = 0

    def addParticipantes(self, posicao, participante):
        """
        Método que adiciona os participantes na lista.
        """
        self.__jogadores.inserir(posicao, participante)#aqui nossa objeto da classe lista insere os jogadores
    
    def addQtdVencedores(self, qtdVencedores):
        """
        Método que recebe a quantidade de vencedores.
        """
        self.__qtdVencedores = qtdVencedores

    def rodada(self, num):
        """
        Método que gera as rodadas do jogo de acordo com as regras do mesmo.
        """
        temp = random.randint(4, 16)
        print(f'Participantes: {self.__jogadores}') #nossa lista de jogadores
        print(f'Rodada: {num}') #numero da rodada
        print(f'Pointer: {self.__jogadores.pointer()}') #jogador/a da vez
        print(f'K {temp}')#numero de voltas
        for i in range(temp):
            carga = self.__jogadores.pedirProximo()
            if i+1 == temp:
                posicao = self.__jogadores.busca(carga)
                self.__removidos.empilha(carga)#aqui quem foi removido é passado pra pilha de removidos
                print(f'Removido: {carga}')
                self.__jogadores.remover(posicao)#aqui ele/ela é deletado


    def executar(self):
        """
        Método que executa jogo.
        """
        self.__jogadores.preparaPercurso(1)#prepara o ponteiro para percorrer a lista a partir do nó correspondente à posicao indicada, no caso, 1.
        num_rodada = 0 #contador das rodadas
        while len(self.__jogadores) > self.__qtdVencedores: #laço que controla as iterações da jogada de acordo com a regra estabelecida.
            num_rodada += 1
            self.rodada(num_rodada)#nossa função rodada é chamada aqui, de forma que nela, o jogo de fato começa a funcionar de acordo com as regras pré-estabelecidas.

        print(f'Vencedores apos {num_rodada} rodadas: {self.__jogadores}')
        print(f'Percurso para vitoria: {self.__removidos}')


#
#     def __str__(self)->str:
#         s = 'Eliminados: '
#         cursor = self.__topo
#         while( cursor is not None ):
#             s += f'{cursor.carga}, '
#             cursor = cursor.prox
#         s = s.rstrip('< ')
#         s += ' '
#         return s
#
#     def salvar_jogo(nome):
#         """
#         Método que salva a rodada do jogo atual.
#         """
#         jogo = open('jogo.txt','a')
#         jogo.write (str) # o que é isso? esta certo mesmo?
