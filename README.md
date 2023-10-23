## Computação Bioinspirada

Este repositório é dedicado a matéria (optativa) de Computação Bioinspirada do curso de Sistemas de Informação da UFU.

### Projeto 1

O Projeto 1 consiste na implementação de um Algoritmo Genético de representação binária para resolver o Problema da Mochila.

>Dado um conjunto de itens, cada item com um peso e valor associados a ele. O problema da mochila 
>consiste em encontrar o conjunto de itens tal que o peso total seja menor ou igual a um determinado 
>limite (tamanho da mochila) e o valor total obtido seja o maior possível. Como restrição, os itens não 
>podem ser “quebrados”, ou seja, a decisão consiste apenas em inserir ou não inserir um item na mochila.

O seu desempenho é comparado com um Algoritmo de Programação Dinâmica. A implementação de ambos está na pasta projeto1, juntamente
com o arquivo Relatório.pdf com as análises dos resultados obtidos com ambos os programas.

### Projeto 2

O objetivo deste trabalho é explorar a implementação e os diferentes parâmetros da rede neural perceptron. Para isso, será utilizada a base de dados Iris, disponível aqui.
Trata-se de um conjunto de dados de uma espécie de planta florida. Essa base contém as características de três variedades de iris: Setosa, Versicolour e Virginica. Para cada variedade, são apresentadas quatro característica: comprimento da sépala (sepal length), largura da sépala (sepal width), comprimento da pétala (petal length) e largura da pétala (petal
width). A partir dessas características, é possível classificar as plantas em uma das três variedades. 

Você deve implementar um perceptron de uma camada (single layer perceptron, como
visto em aula. As classes da iris podem ser consideradas linearmente separáveis duas a duas; logo, você deve selecionar duas espécies de iris para fazer sua classificação. Treine
sua rede neural iniciando com pesos aleatórios e com uma parte do conjunto de dados. Em seguida, usando os pesos encontrados pela rede, classifique o restante do conjunto de
dados.
