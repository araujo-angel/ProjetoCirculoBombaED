from ListaSimplesmenteEncadeada import *
from PilhaSimplesmenteEncadeada import *
import random

class Jogo:
    def __init__(self):
        self.jogo = None


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
        jogo = open('jogo.txt','a')
        jogo.write (str) # o que é isso? esta certo mesmo?
        jogo.close()


"""
Instancia os objetos da classe jogo, rodada e pilha.

"""

rodada1 = Jogo()
rodada = Lista()
pilha = Pilha()

#main


try:
    qtdJogadores = int(input('Diga a quantidade de jogadores: '))
    qtdVencedores = int(input('Diga a quantidade de vencedores no jogo: '))
    for i in range(1, qtdJogadores+1):
        rodada.inserir(i, input('Jogador: '))
    rodada1.__inicializador__(qtdVencedores)
    print(rodada)
    print(pilha)

except ListaException as ae:
    print(ae)