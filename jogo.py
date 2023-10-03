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


    def __criar__(self):
        rodada = Lista.inserir # o que está sendo inserido? Onde está sendo inserido?
        return rodada


    def __inicializador__(self, qtdVencedores):
        """
        Função que têm a lógica do jogo e todo seu funcionamento.
        """
        j = 1
        r = 0 # rodada do jogo

        while len(rodada) > qtdVencedores:
            r += 1
            print(f'Participantes {rodada}')
            print(f'Rodada: {r}')

            temp = random.randint(4, 16)
            for i in range(temp):
                if j > len(rodada):
                    j = 1
                # como volto para o 0 se o temp for maior que o tamanho da lista?
                if temp == i+1:
                    removido = rodada.remover(j)
                    pilha.empilha(removido)
                    print(f'Removido: {removido}')
                j += 1


    def __str__(self)->str:
        s = 'Eliminados: '
        cursor = self.__topo
        while( cursor is not None ):
            s += f'{cursor.carga}, '
            cursor = cursor.prox
        s = s.rstrip('< ')
        s += ' '
        return s

    def salvar_jogo(nome):
        """
        Método que salva a rodada do jogo atual.
        """
        jogo = open('jogo.txt','a')
        jogo.write (str) # o que é isso? esta certo mesmo?