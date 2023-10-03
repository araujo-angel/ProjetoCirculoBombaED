from ListaSimplesmenteEncadeada import *
from PilhaSimplesmenteEncadeada import *

class Jogo:
    def __init__(self, rodada):
        self.__rodada = rodada

    def salvar_jogo(nome, rodada):
    jogo = open('jogo.txt','w')
    for i in range(qtdJogadores):
        jogo.write('Eliminados: ', )

rodada1 = Lista()
"""
Instancia o primeiro objeto da classe lista. Aqui definido como a primeira rodada do jogo.

"""

try:
    qtdJogadores = int(input('Diga a quantidade de jogadores: ')) 
    qtdVencedores = int(input('Diga a quantidade de vencedores no jogo: '))
    if qtdVencedores > 0 and qtdVencedores <= (qtdJogadores - 1):
        for i in range(1, qtdJogadores+1):
            rodada1.inserir(i, input('Jogador: '))
    
    print(rodada1)
    
except ListaException as ae:
    print(ae)


carga = rodada1.remover(1)
print('Jogador removido:', carga)
print(rodada1)

conteudo = rodada1.elemento(3)
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




