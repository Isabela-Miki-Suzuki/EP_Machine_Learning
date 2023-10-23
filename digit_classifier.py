from math import *
from sys import float_info

import numpy as np
import rotations_and_system_solving
import decomposition
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
def visualize_images(image, w_d, n, p, method): 
	''' ( array 1D, array 2D, int, int, Boolean ) ->
	RECEBE uma imagem i e um classificador Wd (nxp). Calcula a imagem
	mais próxima pela combinação linear das imagens em Wd pelo método indicado. Imprime ambas imagens
	'''
	axes=[]
	fig=plt.figure()
	
	h = rotations_and_system_solving.resol_sist(image.copy(), w_d.copy(), n, 1, p, method)
	image_approx = (w_d@h).reshape(int(sqrt(n)),int(sqrt(n)))*255
	axes.append(fig.add_subplot(1, 2, 2))
	subplot_title=("Approximate image")
	axes[-1].set_title(subplot_title)
	plt.imshow(image_approx, cmap=plt.get_cmap("gray"))
	
	image = image.reshape(int(sqrt(n)),int(sqrt(n)))*255 
	axes.append(fig.add_subplot(1, 2, 1))
	subplot_title=("Test image")
	axes[-1].set_title(subplot_title)
	plt.imshow(image, cmap=plt.get_cmap("gray"))
	
	fig.tight_layout()
	plt.show()
		
#--------------------------------------------------------------------------------------------------
def main():
	ndig_treino = int((input("Enter the number of images for training (suggestions are 100, 1000 or 4000): "))) # n° de colunas das matrizes train_dig(n° de imagens para o treinamento)
	n_test = int((input("Enter the number of images to be tested (suggestion is 10000): "))) # n° de colunas da matriz A(quantidade de imagens a serem testadas)
	p = int(input("Enter the number of columns of the classifier matrices (suggestions are 5, 10 or 15): ")) # n° de colunas das matrizes Wd
	n = int(input("Enter the number of rows of the classifier matrices (n = 784 for the files in this repository): ")) # n° de linhas das matrizes Wd

	method = False 
	if input("Enter the method you want to use (g for givens and h for householder): ") == "g": # método utilizado será a rotação de givens("g") ou householder("h") dependendo do input
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

		h,w_digitos[i] = decomposition.mmq_alternado(train_dig, w_digitos[i], n, ndig_treino, p, method)

		elapsed_time_w = time.time() - start_time_w
		print("  Time for digit training " + str(i) + ": " + str(elapsed_time_w) + " seconds")

	# Classificação das imagens teste
	t_i = np.loadtxt("test_images.txt") # matriz 2D contendo as imagens testes nas suas colunas
	test_images = t_i[0:n,0:n_test]/255 # redimensionando para uma matriz 784 x n_test
	digitos = np.zeros((n_test),dtype=int) # array que armazena o dígito mais provável que a imagem seja
	erros = np.repeat(float_info.max, n_test) # o erro da imagem para o dígito mais provável

	for i in range(10): # para cada dígito
		h = rotations_and_system_solving.resol_sist(test_images.copy(), w_digitos[i].copy(), n, n_test, p, method) # a solução do sistema para cada dígito
		erro_dig = error(test_images - w_digitos[i]@h) # o erro da imagem para o dígito
		for j in range(n_test): # para cada imagem
			if erro_dig[j] < erros[j]: # armazena o menor erro e o dígito com menor erro
				digitos[j] = i
				erros[j] = erro_dig[j]

	print("  Total execution time: " + str(time.time() - start) + " seconds")
 	
	# Impressão da imagem i e sua aproximação
	#i = 0 # imagem i que será impressa
	#d = digitos[i] # dígito d ao qual ela foi classificada
	#visualize_images(test_images[:, i].copy().reshape(n, 1), w_digitos[d].copy(), n, p, method)
	
	# Estatísticas
	percentual, acertos, percentual_digito = estatisticas(digitos, n_test)
	print("Total percentage of correct answers: ", percentual, "%")
	print("Number of correct answers by digit", acertos)
	print("Percentage of correct answers per digit", percentual_digito)
# ------------------------------------------------
if __name__ == "__main__":
    main()
