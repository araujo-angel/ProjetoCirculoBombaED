# ProjetoCirculoBombaED
 Mini projeto desenvolvido na disciplina de Estrutura de Dados (2023.2), utilizando a linguagem python, ministrada pelo professor Alex Cunha, no curso de Sistemas para Internet (IFPB).

 O jogo funciona da seguinte maneira:
 
A brincadeira do círculo da bomba começa com a definição das pessoas que irão participar (sem limite de quantidade). Os participantes vão se organizar em círculo. Determina-se, então, quantas pessoas serão vencedoras, com 0 < numVencedores <= nº participantes -1.  Uma pessoa é escolhida aleatoriamente para iniciar a passagem da bomba de confetes. A partir do inicializador, uma música será tocada e a bomba será deslocada para os participantes seguintes, da direita para a esquerda, até que a música pare. Neste momento, o participante que ficou com a bomba é eliminado do jogo e a partida recomeça a partir do jogador sucessor. Enquanto a música estiver tocando, a bomba estará circulando pela roda de participantes. Vamos considerar que a música vai ser tocada em uma quantidade de segundos 4 <= tempo <= 15 a cada iteração, e que cada segundo é o tempo da bola mudar de participante. Quando o programa identificar o(s) vencedor(es), será exibido o rastreamento dos participantes eliminados.

Estruturas de dados utilizadas:

Pilha Encadeada;
Lista Encadeada, com adaptações para funcionar de maneira circular.

