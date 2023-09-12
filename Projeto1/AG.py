# Dado um conjunto de itens, cada item com um peso e valor associados a ele. O
# problema da mochila consiste em encontrar o conjunto de itens tal que o peso total seja
# menor ou igual a um determinado limite (tamanho da mochila) e o valor total obtido seja
# o maior possível. Como restrição, os itens não podem ser “quebrados”, ou seja, a decisão
# consiste apenas em inserir ou não inserir um item na mochila.

import random
import numpy as np
import re
import time

POPULACAO = 50
GERACOES = 25
MUTACAO = 15
TORNEIO = 3

class ITEM:
    def __init__(self, id, valor, peso):
        self.id = id
        self.valor = valor
        self.peso = peso
    
    def __lt__(self, outro):
        return self.peso < outro.peso

class MOCHILA:
	def __init__(self, tamanho, capacidade):
		self.tamanho = tamanho
		self.capacidade = capacidade
  
class INDIVIDUO:
	def __init__(self, vetorBinario):
		self.vetorBinario = vetorBinario
		self.fitness = 0
		self.pesoAtual = 0

def gerarNumAleatorio(N):
    return random.randint(0, N-1)
 
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
  
	itens.sort()
	mochila = MOCHILA(tamanho, capacidade)
	return mochila, itens

def incializaPopulacao(mochila, itens):
    # Estou assumindo que a quantidade de itens e o tamanho da mochila podem ser diferentes
    vetorBinario = [0 for i in range(len(itens))]
    populacao = []
    
    for i in range(POPULACAO):
        peso = 0; valor = 0; tamanho = 0
        individuo = INDIVIDUO(vetorBinario)
        
        for j in range(mochila.tamanho):
            pos = gerarNumAleatorio(len(itens))
            individuo.vetorBinario[pos] = 1
            
            tamanho+=1
            peso += itens[pos].peso
            valor += itens[pos].valor
            
            # Assim que o peso máx for atingido paramos
            if peso > mochila.capacidade:
                peso -= itens[pos].peso
                valor -= itens[pos].valor
                tamanho -=1
                individuo.vetorBinario[pos] = 0
                break
        
        individuo.fitness = valor
        individuo.pesoAtual = peso    
        populacao.append(individuo)
        
    return populacao
   
def fitness(individuo, mochila, itens):
    peso = 0; valor = 0;  tamanho = 0
    
    for i in range(len(itens)):
        if individuo.vetorBinario[i] == 1:
            tamanho +=1
            peso += itens[i].peso
            valor += itens[i].valor
            
    if tamanho <= mochila.tamanho and peso <= mochila.capacidade: 
        individuo.pesoAtual = peso
        individuo.fitness = valor
        
    return individuo

def selecaoPorTorneio(populacao, melhor):
    for i in range(1,TORNEIO-1):
        individuo = populacao[gerarNumAleatorio(POPULACAO)]
        if(individuo.fitness > melhor.fitness):
            melhor = individuo
    return melhor

def recombinacaoUniforme(pai, mae, filho, itens, mochila):
    for i in range(len(pai.vetorBinario)):
        
        if filho.pesoAtual >= mochila.capacidade:
            break
        
        if gerarNumAleatorio(2) == 1:
            filho.vetorBinario[i] = pai.vetorBinario[i]
        else:
            filho.vetorBinario[i] = mae.vetorBinario[i] 
            
        if filho.vetorBinario[i] == 1:
            filho.pesoAtual += itens[i].peso
    
    return filho
        
def mutacao(filho, mochila, itens):
    probabilidade = gerarNumAleatorio(100)
    
    if probabilidade <= MUTACAO:
        if filho.pesoAtual > mochila.capacidade:
            for i in range(len(itens)):
                if filho.vetorBinario[i] == 1:
                    filho.vetorBinario[i] = 0
                    filho.pesoAtual -= itens[i].peso
                    break
        
        else:
            for i in range(len(itens)):
                if filho.vetorBinario[i] == 0:
                    filho.vetorBinario[i] = 1
                    filho.pesoAtual += itens[i].peso
                    break
        
    return filho

def reproducao(populacao, mochila, itens):
    vetorBinario = [0 for i in range(len(itens))]
    melhor = INDIVIDUO(vetorBinario)
    novaPopulacao = []
    
    for i in range(POPULACAO):
        pai = selecaoPorTorneio(populacao, INDIVIDUO(vetorBinario))
        mae = selecaoPorTorneio(populacao, INDIVIDUO(vetorBinario))
        filho = recombinacaoUniforme(pai,mae, INDIVIDUO(vetorBinario), itens, mochila)
        filho = mutacao(filho, mochila, itens)
        filho = fitness(filho, mochila, itens)
        
        
        if filho.fitness > melhor.fitness:
            melhor = filho
            
        novaPopulacao.append(filho)
        
    return melhor, novaPopulacao

def algoritmoGenetico(arquivoDeEntrada):
    mochila, itens = defineMochila(arquivoDeEntrada)
    populacao = incializaPopulacao(mochila, itens)
    melhor = 0
    
    for i in range(GERACOES):
        melhor, novaPopulacao = reproducao(populacao, mochila, itens)
        populacao = novaPopulacao
        print(f"Melhor resultado: {melhor.fitness}")
        
    return melhor.fitness
        
def main():
	melhorResultado = 0

	for i in range(1, 17):
		arquivoDeEntrada = f"input/input{i}.in"
		melhorResultado = algoritmoGenetico(arquivoDeEntrada)
		saida = f"Instancia {i} : {melhorResultado}\n"
		with open("output/AG.out", "a+") as arquivoDeSaida:
			arquivoDeSaida.write(saida)

if __name__ == '__main__': 
    random.seed(0)
    tempoInicial = time.time()
    main()
    tempoExecucao = time.time() - tempoInicial
    print(f"Tempo gasto para execução: {tempoExecucao} segundos")