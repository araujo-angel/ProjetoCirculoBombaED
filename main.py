from jogo import *
"""
Aqui é instanciado o objeto da classe Jogo.
"""
rodada1 = Jogo()


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
