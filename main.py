from ListaSimplesmenteEncadeada import *
from PilhaSimplesmenteEncadeada import *
import random

class Jogo:
    def __init__(self):
        self.jogo = None
        
    
    def __criar__(self):
        rodada = Lista.inserir
        return rodada


    def __inicializador__(self, qtdJogadores, qtdVencedores):
        while qtdVencedores < (qtdJogadores - 1) and qtdVencedores > 0:
            temp = random.randint(4, 16)
            for rodada in range(temp):
                if temp == rodada[i]:
                    removido = rodada.remove(i)
                    Pilha.empilha(removido)


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
        jogo.write (str)
        jogo.close()

    

rodada1 = Jogo()
"""
Instancia o primeiro objeto da classe lista. Aqui definido como a primeira rodada do jogo.

"""

try:
    qtdJogadores = int(input('Diga a quantidade de jogadores: ')) 
    qtdVencedores = int(input('Diga a quantidade de vencedores no jogo: '))
    for i in range(1, qtdJogadores+1):
        rodada1.__criar__ = (i, input('Jogador: '))
    rodada1.__inicializador__(qtdJogadores, qtdVencedores)
    print(rodada1)
    
except ListaException as ae:
    print(ae)


# carga = rodada1.remover(1)
# print('Jogador removido:', carga)
# print(rodada1)

# conteudo = rodada1.elemento(3)
#     print(f'Elemento(3): {conteudo}')
#     posicao = rodada1.busca(50)
#     print(f'Posicao do elemento 50: {posicao}')

#     for i in range(15):
#         print('removendo:', rodada1.remover(1))
#     print(rodada1)
#print(rodada1)

# print('Tamanho de rodada1:', len(rodada1))


# try:
#     for i in range(1,11):
#         rodada1.empilha(i*10)

#     print(rodada1)

#     print('Tamanho: ',len(rodada1))

    

#     posicao = 4
#     print(f'Elemento({posicao}):',rodada1.elemento(posicao))
#     print('busca(40):', rodada1.busca(40))

#     print('Removendo os 3 primeiros elementos do topo da pilha')
#     for i in range(3):
#         print(rodada1.desempilha())
#     print(rodada1)

    
# except PilhaException as pe:
#     print('ERRO:',pe)
# except Exception as e:
#     print('Erro:',e,'Classe: ',e.__class__.__name__)




