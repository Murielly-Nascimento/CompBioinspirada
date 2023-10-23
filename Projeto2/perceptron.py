import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn import svm

def treina_perceptron(dadosTreino, classeTreino, learning_rate=0.01, epochs=300, ):
    pesos = np.zeros(dadosTreino.shape[1])
    vies = 0
    for epoch in range(epochs):
        for i in range(dadosTreino.shape[0]):
            produtoEscalar = np.dot(dadosTreino[i], pesos) + vies
            
            if produtoEscalar >= 0:
                predicao = 1
            else:
                predicao = 0
             
            error = classeTreino[i] - predicao
            pesos += learning_rate * error * vies
            vies +=  error * learning_rate
    
    return pesos, vies

def testa_perceptron(dadosTeste, classeTeste, pesos, vies):
	predicao = 0
	correto = 0
	valores = []
	for i in range(dadosTeste.shape[0]):
		produtoEscalar = np.dot(dadosTeste[i], pesos) + vies

		if produtoEscalar >= 0:
			predicao = 1
		else:
			predicao = 0
		if predicao == classeTeste[i]:
			correto+=1
		valores.append(predicao)
	acuracia = correto/ dadosTeste.shape[0]
	return acuracia, valores

def imprimeGrafico(dadosTestes, classeTeste, predicoes, pesosTreino, vies):
	setosa = []
	versicolour = []
	virginica = []
	for i in range(len(classeTeste)):
		if classeTeste[i] == 0:
			setosa.append(dadosTestes[i])
		elif classeTeste[i] == 1: 
			versicolour.append(dadosTestes[i])
		else: virginica.append(dadosTestes[i])
			

	setosa = np.array(setosa)
	versicolour = np.array(versicolour)
	virginica = np.array(virginica)

	plt.scatter(setosa[:,0], setosa[:,1], marker='o', label='Setosa')
	plt.scatter(versicolour[:,0], versicolour[:,1], marker='x', label='Versicolour')
	plt.scatter(virginica[:,0], virginica[:,1], marker='s', label='Virginica')

	decisaoX = np.linspace(int(dadosTestes[:,0].min()), int(dadosTestes[:,0].max()), 100)
	#decisaoY = (-pesosTreino[0] * decisaoX - vies) / pesosTreino[1] 
	decisaoY = -(pesosTreino[0]/pesosTreino[1]*decisaoX) - (vies/pesosTreino[1])

	plt.plot(decisaoX, decisaoY, color='red', linestyle='--', label='Limite de Decisão')

	plt.xlabel('Comprimento da Sépala')
	plt.ylabel('Largura da Sépala')
	plt.title('Limite de Decisão')
	plt.legend()
	plt.show()

def main():
	# Importando o dataset 'iris'.
	iris = load_iris()
 
	# Parametros sepal length and sepal width
	dados = iris.data[:100, :2] 
	classes = iris.target[:100]
 
	# Separamos os dados em treino e teste.
	dadosTreino, dadosTestes, classeTreino, classeTeste = train_test_split(dados, classes, test_size=0.7, random_state=42)
	pesosTreino, vies = treina_perceptron(dadosTreino, classeTreino)
 
	dados = iris.data[:,:2] 
	classes = iris.target
	dadosTreino, dadosTestes, classeTreino, classeTeste = train_test_split(dados, classes, test_size=0.7, random_state=42)
	
	# Testamos o perceptron
	acuracia, predicoes = testa_perceptron(dadosTestes, classeTeste, pesosTreino, vies)
	print(acuracia)
	imprimeGrafico(dadosTestes, classeTeste, predicoes, pesosTreino, vies)
	print("Fim")

 
 
if __name__ == "__main__":
    main()