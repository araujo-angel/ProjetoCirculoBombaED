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
        '''
        Função para a construção da rodada como uma lista.
        '''
        rodadaParticipantes = Lista.inserir # o que está sendo inserido? Onde está sendo inserido?
        return rodada


    def __inicializador__(self, qtdVencedores):
        """
        Função que têm a lógica do jogo e todo seu funcionamento.
        """
        j = 1 #o que é esse j?
        rodada = 0 #contador de rodadas no jogo

        while len(rodada) > qtdVencedores:
            rodada += 1 
            print(f'Participantes: {rodadaParticipantes}')
            print(f'Rodada: {rodada}')

            Lista.preparaPercurso(1)
            temp =  random.randint(4, 16)
            while (temp > qtdVencedores):
                cont = 0
                while(Lista.temProximo()):
                    carga = Lista.pedirProximo()
                    print(carga)
                    cont += 1
                    if (cont < len(Lista)-1):
                        break
                posicao = Lista.busca(carga)
                Pilha.empilha(carga)
                print(f'Removido: {carga}')
                Lista.remover(posicao)
                #print(f'Participantes: {Lista}')
                temp += 1
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



#professor aula remota
# pilha = []
#     lst.preparaPercurso(1)
#     step = 0
#     while (step < 3): # A musica vai tocar e parar 3 vezes
#         cont = 0
#         while(lst.temProximo()):
#             carga = lst.pedirProximo()
#             print(carga)
#             cont += 1
#             if (cont == 5):
#                 break
#         posicao = lst.busca(carga)
#         pilha.append(carga)
#         lst.remover(posicao)
#         print(lst)
#         step += 1



