from ListaSimplesmenteEncadeada import circulo, circuloException

rodada1 = circulo()
"""
Instancia o primeiro objeto da classe circulo. Aqui definido como a primeira rodada do jogo.

"""

try:
    qtdVencedores = int(input('Diga a quantidade de vencedores no jogo: '))

    qtdJogadores = int(input('Diga a quantidade de jogadores: '))
    for i in range(1,qtdJogadores+1):
        rodada1.inserir(i, input('Jogador: '))
    print(rodada1)
    
except circuloException as ae:
    print(ae)

#if rodada1.estaVazia():
#  print('rodada1 esta vazia.')
#     carga = rodada1.remover(1)
#     print('Carga removida:', carga)
#     print(rodada1)

#     conteudo = rodada1.elemento(3)
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




