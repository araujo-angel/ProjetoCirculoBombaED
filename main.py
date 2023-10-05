from jogo import *
"""
Aqui é instanciado o objeto da classe Jogo.
"""
jogo = Jogo()


try:
    jogar = True
    while jogar:

        qtd_jogadores = int(input('Diga a quantidade de jogadores: '))
        for i in range(1, qtd_jogadores+1):
            jogo.addParticipantes(i, input('Jogador: '))#i é a posição e o input é o/a participante, ou seja, são os parametros que exigidos na função addParticipantes lá da classe jogo.
        qtd_vencedores = int(input('Diga a quantidade de vencedores no jogo: '))
        jogo.addQtdVencedores(qtd_vencedores)

        jogo.executar()#aqui o jogo é executado

        jogo.__str__()

        #jogo.salvar() #salva as informações dos jogadores

        resposta = input('Deseja jogar novamente?: (S)im/(N)ão: ').upper()#quando o jogo acaba, sai do laço e entra nesse input para saber se o/a jogador/a quer jogar novamente
        if resposta != 'S' and resposta != 'N':
                raise JogoException(f'A resposta deve ser S ou N.')
        if resposta == "N":
            jogar = False

except JogoException as ae:
    print(ae)
