# Dado um conjunto de itens, cada item com um peso e valor associados a ele. O
# problema da mochila consiste em encontrar o conjunto de itens tal que o peso total seja
# menor ou igual a um determinado limite (tamanho da mochila) e o valor total obtido seja
# o maior possível. Como restrição, os itens não podem ser “quebrados”, ou seja, a decisão
# consiste apenas em inserir ou não inserir um item na mochila.

import numpy as np
import re
import time

POPULACAO = 100
GERACOES = 50
MUTACAO = 15
TORNEIO = 3

class ITEM:
    def __init__(self, id, valor, peso):
        self.id = id
        self.valor = valor
        self.peso = peso
        self.flag = 0

class MOCHILA:
	def __init__(self, tamanho, capacidade, itens):
		self.fitness = 0
		self.tamanho = tamanho
		self.capacidade = capacidade
		self.itens = itens
 
def defineMochila(arquivoDeEntrada):
	with open(arquivoDeEntrada, "r") as arquivo:
		linhas = arquivo.readlines()

	tamanho = int(linhas[0].strip())
	capacidade = int(linhas[-1].strip())

	itens = []
	for linha in linhas[1:-1]:
		numeros = re.findall(r"[0-9]+", linha) 
		id = int(numeros[0]) - 1
		valor = int(numeros[1])
		peso = int(numeros[2])
		item = ITEM(id,valor,peso)
		itens.append(item)
  
	mochila = MOCHILA(tamanho, capacidade, itens)
	return mochila

def reproducao(arquivoDeEntrada):
    mochila = defineMochila(arquivoDeEntrada)

def main():
	melhorResultado = 0

	for i in range(1, 6):
		arquivoDeEntrada = f"input/input{i}.in"
		melhorResultado = reproducao(arquivoDeEntrada)
		saida = f"Instancia {i} : {melhorResultado}\n"
		with open("output/dynamic.out", "a+") as arquivoDeSaida:
			arquivoDeSaida.write(saida)

if __name__ == '__main__': 
	tempoInicial = time.time()
	main()
	tempoExecucao = time.time() - tempoInicial
	print(f"Tempo gasto para execução: {tempoExecucao} segundos")