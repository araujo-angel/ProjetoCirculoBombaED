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


#professor aula remota
pilha = []
    lst.preparaPercurso(1)
    step = 0
    while (step < 3): # A musica vai tocar e parar 3 vezes
        cont = 0
        while(lst.temProximo()):
            carga = lst.pedirProximo()
            print(carga)
            cont += 1
            if (cont == 5):
                break
        posicao = lst.busca(carga)
        pilha.append(carga)
        lst.remover(posicao)
        print(lst)
        step += 1


#relação professor -> nosso código
    Lista.preparaPercurso(1)
    temp =  random.randint(4, 16)
    while (temp < qtdVencedores):
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