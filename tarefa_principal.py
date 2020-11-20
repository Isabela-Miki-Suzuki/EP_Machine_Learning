from math import *
from sys import float_info

import numpy as np
import tarefa1
import tarefa2
import matplotlib.pyplot as plt
import time
#--------------------------------------------------------------------------------------------------
def estatisticas(digitos, n_test):
	'''(array, int) -> (float, array, array)
	RECEBE uma array de inteiros de tamanho n_test chamada digitos
	RETORNA uma tupla:
	 A porcentagem total de acertos;
	 Uma array com cada posição representando um dígito e indicando quantas classificações foram corretas
	dentre o total de ocorrências deste dígito no arquivo de testes;
	 Uma array com cada posição representando um dígito e indicando o correspondente percentual de acertos
	para este dígito
	(comparando o array digitos com test_index.txt)
	'''
	test_index = np.loadtxt("test_index.txt", dtype=int)
	acertos = np.zeros((10), dtype=int)
	total = np.zeros((10), dtype=int)
	for i in range(n_test): # para cada imagem
		if test_index[i] == digitos[i]:
			acertos[test_index[i]]+=1
		total[test_index[i]]+=1
	percentual = 100 * acertos.sum()/n_test
	percentual_digito = 100 * acertos[0:10]/total[0:10]
	return percentual, acertos, percentual_digito
#--------------------------------------------------------------------------------------------------
def error(w):
	'''(array 2D) -> (array 1D)
	RECEBE uma array w e calcula a norma euclidiana de cada coluna
	DEVOLVE uma array contendo as normas
	'''
	return np.sqrt(np.sum(w ** 2, axis=0))
#--------------------------------------------------------------------------------------------------
def main():
	ndig_treino = int((input("Digite o valor de ndig_treino: "))) # n° de colunas das matrizes train_dig(n° de imagens para o treinamento)
	n_test = int((input("Digite o valor de n_test: "))) # n° de colunas da matriz A(quantidade de imagens a serem testadas)
	p = int(input("Digite o valor de p: ")) # n° de colunas das matrizes Wd
	n = int(input("Digite o valor de n: ")) # n° de linhas das matrizes Wd

	method = False 
	if input("Digite o método que deseja utilisar: ") == "g": # método utilizado será a rotação de givens("g") ou householder("h") dependendo do input
		method = True

	start = time.time()

	# Treinamento dos dígitos
	w_digitos = np.empty((10,n,p)) # array 3D com as matrizes Wd
	for i in range(10):
		start_time_w = time.time()
		train = np.loadtxt("train_dig"+str(i)+".txt")
		train_dig = train[0:n, 0:ndig_treino]/255

		# decomposição da matriz train_dig
		w_digitos[i] = np.random.rand(n, p)

		h,w_digitos[i] = tarefa2.mmq_alternado(train_dig, w_digitos[i], n, ndig_treino, p, method)

		elapsed_time_w = time.time() - start_time_w
		print("  Tempo para o treinamento do dígito " + str(i) + ": " + str(elapsed_time_w) + " segundos")

		#imprime imagens
		#for k in range(p):
		#	matriz = w_digitos[i,:,k].reshape(int(sqrt(n)),int(sqrt(n))).copy()*255
		#	plt.imshow(matriz)
		#	plt.imshow(matriz, cmap=plt.get_cmap("gray"))
		#	plt.show()

	# Classificação das imagens teste
	t_i = np.loadtxt("test_images.txt") # matriz 2D contendo as imagens testes nas suas colunas
	test_images = t_i[0:n,0:n_test]/255 # redimensionando para uma matriz 784 x n_test
	digitos = np.zeros((n_test),dtype=int) # array que armazena o dígito mais provável que a imagem seja
	erros = np.repeat(float_info.max, n_test) # o erro da imagem para o dígito mais provável

	for i in range(10): # para cada dígito
		h = tarefa1.resol_sist(test_images.copy(), w_digitos[i].copy(), n, n_test, p, method) # a solução do sistema para cada dígito
		erro_dig = error(test_images - w_digitos[i]@h) # o erro da imagem para o dígito
		for j in range(n_test): # para cada imagem
			if erro_dig[j] < erros[j]: # armazena o menor erro e o dígito com menor erro
				digitos[j] = i
				erros[j] = erro_dig[j]
	
	print("  Tempo total de execução: " +str(time.time() - start)+ " segundos")

	# Estatísticas
	percentual, acertos, percentual_digito = estatisticas(digitos, n_test)
	print("percentual total: ", percentual, "%")
	print("acertos por dígito", acertos)
	print("percentual de acertos por dígito", percentual_digito)
# ------------------------------------------------
if __name__ == "__main__":
    main()
