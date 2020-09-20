# Detecção do círculo mínimo envolvente em pontos gerados aleatoriamente

## Objetivos

O objetivo deste projeto é detalhar os fundamentos teóricos e relatar as abordagens práticas para a resolução do problema de detecção do círculo mínimo envolvente em pontos gerados aleatoriamente. Serão consideradas duas abordagens, sendo a primeira baseada em um algoritmo heurístico que fornece uma aproximação da solução exata e que deve obrigatoriamente envolver todos os pontos. A segunda abordagem será baseada em um algoritmo de detecção do círculo mínimo envolvente exato. Apesar de se esperar algum grau de imprecisão em comparação à solução exata, a solução baseada no algoritmo heurístico deve apresentar um ganho de performance, o que será também mostrado.  

## Métodos

O detalhamento teórico dos dois métodos utilizados está descrito no relatório contido neste repositório.

## Implementação

Ambos algoritmos foram implementados em linguagem Python, gerando uma massa randômica de pontos com distribuição normal e com diferentes tamanhos. As figuras abaixo ilustram os resultados gráficos para diferentes tamanhos de conjuntos de pontos:

![circles_1](/pictures/circles_1.jpg)

![circles_2](/pictures/circles_2.jpg)

![circles_3](/pictures/circles_3.jpg)

Conforme esperado, enquanto o algoritmo de cálculo do círculo mínimo envolvente é capaz de definir a solução exata, o algoritmo baseado na heurística definida retorna uma aproximação, que em alguns casos pode apresentar uma maior distorção, como mostrado na Figura 2. 
Abaixo, podemos visualizar a representação gráfica da comparação entre os tempos de execução de ambos algoritmos:

![runtime](/pictures/runtime.jpg)

Como podemos observar, ambos apresentam uma complexidade linear, como esperado. Porém, o algoritmo baseado em heurística mostra uma constante de inclinação menor, fazendo com que haja um ganho de performance em relação ao método de mínimo círculo envolvente.  
Abaixo, vemos mais um exemplo considerando pontos pré-definidos.

![circles_4](/pictures/circles_4.jpg)

## Conclusão

Mostrou-se neste projeto o detalhamento teórico dos dois métodos propostos, assim como a implementação dos algoritmos em linguagem Python e uma análise gráfica dos resultados, assim como uma comparação de performance computacional.
Ambos algoritmos explorados apresentam vantagens e desvantagens, a depender da aplicação. Enquanto o algoritmo de cálculo do círculo mínimo envolvente retorna a solução exata do problema, o algoritmo baseado em heurística retorna uma aproximação que pode ser suficiente em determinados casos, considerando que a aproximação não afeta a garantia de envolvência de 100% dos pontos.
Em contrapartida, apesar de ambos algoritmos apresentarem uma complexidade temporal assintótica proporcional a O_((n)), o método baseado em heurística mostra um ganho de desempenho em relação à alternativa de solução exata. Este ganho, por sua vez, pode não ser relevante para determinadas aplicações onde o conjunto de pontos seja pequeno e/ou onde o requerimento de tempo não seja altamente restrito.   

