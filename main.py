from jogo import *
import os
"""
Aqui é instanciado o objeto da classe Jogo.
"""
jogo = Jogo()


try:
    jogar = True
    while jogar:
        
        print('Bem vindo(a) ao jogo "Círculo da bomba"!')
        
        puxarArquivo = input('Deseja ver os dados dos participantes? (S)im/(N)ão: ').upper()
        if puxarArquivo != 'S' and puxarArquivo != 'N':
            raise JogoException(f'A resposta deve ser S ou N.')

        if puxarArquivo == "S":
            if os.path.isfile('jogo.txt'):
                with open('jogo.txt', 'r') as arq:
                    arquivo = arq.readlines()
                    listaJogadores = arquivo[0].split(',')
                    for i in range(len(listaJogadores)):
                        jogo.addParticipantes(i+1, listaJogadores[i])
                        arq.close()
                try:
                    qtd_vencedores = int(input('Diga a quantidade de vencedores no jogo: '))
                    jogo.addQtdVencedores(qtd_vencedores)
                except ValueError:
                    raise JogoException(f'A quantidade de vencedores deve ser um número inteiro.')
        if puxarArquivo == "N":
            try:
                qtd_jogadores = int(input('Diga a quantidade de jogadores: '))
            except ValueError:
                    raise JogoException(f'A quantidade de jogadores deve ser um número inteiro.')
            for i in range(1, qtd_jogadores+1):
                jogo.addParticipantes(i, input('Jogador: '))#i é a posição e o input é o/a participante, ou seja, são os parametros que exigidos na função addParticipantes lá da classe jogo.
            try:
                qtd_vencedores = int(input('Diga a quantidade de vencedores no jogo: '))
                jogo.addQtdVencedores(qtd_vencedores)
            except ValueError:
                raise JogoException(f'A quantidade de vencedores deve ser um número inteiro.')


        jogo.executar()#aqui o jogo é executado

        jogo.__strPilha__()#mostra a pilha de removidos

        continuar = input('Deseja jogar novamente? (S)im/(N)ão: ').upper()#quando o jogo acaba, sai do laço e entra nesse input para saber se o/a jogador/a quer jogar novamente
        if continuar != 'S' and continuar != 'N':
            raise JogoException(f'A resposta deve ser S ou N.')
        if continuar == "N":
            jogar = False
    
except JogoException as ae:
    print(ae)
