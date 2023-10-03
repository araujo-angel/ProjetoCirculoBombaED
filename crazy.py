from ListaSimplesmenteEncadeada import *
from PilhaSimplesmenteEncadeada import *
import random

def __inicializador__(self, qtdJogadores, qtdVencedores):
        while qtdVencedores < (qtdJogadores - 1) and qtdVencedores > 0:
            temp = random.randint(4, 16)
            for i in range(temp):
                if temp == Lista[i]:
                    removido = Lista.remove(i)
                    Pilha.empilha(removido)


rodada1 = Lista()

try:
    qtdJogadores = int(input('Diga a quantidade de jogadores: ')) 
    qtdVencedores = int(input('Diga a quantidade de vencedores no jogo: '))
    for i in range(1, qtdJogadores+1):
        rodada1.inserir(i, input('Jogador: '))
    print(rodada1)
    
except ListaException as ae:
    print(ae)