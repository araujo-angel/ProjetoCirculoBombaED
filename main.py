from jogo import *
"""
Aqui é instanciado o objeto da classe Jogo.
"""
rodada = Jogo()


try:
    qtdJogadores = int(input('Diga a quantidade de jogadores: '))
    qtdVencedores = int(input('Diga a quantidade de vencedores no jogo: '))
    for i in range(1, qtdJogadores+1):
        rodada.__criar__(i, input('Jogador: '))
        rodada.__inicializador__(qtdVencedores)
    print(rodada)
    print(pilha)

except ListaException as ae:
    print(ae)
