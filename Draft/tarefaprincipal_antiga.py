from math import *
import numpy as np
import tarefa1_antiga
import tarefa2_antiga
import matplotlib.pyplot as plt
import time
import argparse
#--------------------------------------------------------------------------------------------------
def estatisticas(digitos, n_test):
	'''(array, int) -> (float, array, array)
	RECEBE uma array de inteiros de tamanho n_test chamada digitos
	RETORNA uma tupla:
	a porcentagem total de acertos;
	uma array com cada posição representando um dígito e indicando quantas classificações foram corretas
	dentre o total de ocorrências deste dígito no arquivo de testes;
	uma array com cada posição representando um dígito e indicando o correspondente percentual de acertos
	para este dígito
	(comparando o array digitos com test_index.txt)
	'''
	test_index = np.loadtxt("test_index.txt", dtype=int)
	acertos = np.zeros((10), dtype=int)
	total = np.zeros((10), dtype=int)
	for i in range(n_test):
		if test_index[i] == digitos[i]:
			acertos[test_index[i]]+=1
		total[test_index[i]]+=1
	percentual = 100 * acertos.sum()/n_test
	percentual_digito = 100 * acertos[0:10]/total[0:10]
	return percentual, acertos, percentual_digito
#--------------------------------------------------------------------------------------------------
def norm(w,col,n):
	'''(array, int, int) -> (float)
	RECEBE uma array w de n linhas e calcula o erro da sua coluna col, que é a norma euclidiana
	DEVOLVE a norma
	'''
	return sqrt((w[0:n, col] ** 2).sum())
#--------------------------------------------------------------------------------------------------
def main():
	ndig_treino = int((input("Digite o valor de ndig_treino: "))) # n° de colunas das matrizes Wd (n° de imagens para o treino)
	n_test = int((input("Digite o valor de n_test: "))) # n° de colunas da matriz A, com todas as imagens(quantidade de imagens a serem testadas)
	p = int(input("Digite o valor de p: "))
	n = int(input("Digite o valor de n: ")) #n° de linhas das matrizes Wd

	w_digitos = np.empty((10,n,p)) #array com a matriz 

	for i in range(10):
		start_time_w = time.time()
		t = np.loadtxt("train_dig"+str(i)+".txt")
		train_dig = t[0:n,0:ndig_treino]/255

		w_digitos[i] = np.random.rand(n, p)
		h,w_digitos[i] = tarefa2_antiga.mmq_alternado(train_dig, w_digitos[i].copy(), n, ndig_treino, p)

		elapsed_time_w = time.time() - start_time_w
		print("  Tempo de execucao treinamento: "+str(elapsed_time_w)+" segundos")

#TESTANDO:
#		for k in range(p):
#			matriz = w_digitos[i,:,k].reshape(int(sqrt(n)),int(sqrt(n))).copy()*255
#			plt.imshow(matriz)
#			plt.imshow(matriz, cmap=plt.get_cmap("gray"))
#			plt.show()

	start_time_teste_imagens = time.time()
	t_i = np.loadtxt("test_images.txt")#matriz 2D de 784 x n_test que apresenta as imagens testes nas suas colunas (queremos saber qual é o dígito)
	test_images = t_i[0:n,0:n_test]/255 #redimensionando 
	digitos = np.zeros((n_test),dtype=int) # o dígito mais provável de a imagem ser
	erros = np.empty((n_test)) # o erro de tal imagem para o dígito
	for i in range(10): #para cada dígito
		h = tarefa1_antiga.resol_sist(test_images.copy(), w_digitos[i].copy(), n, n_test, p) #a solução do sistema para cada dígito
		matriz_erro = test_images - w_digitos[i]@h
		for j in range(n_test):
			norma = norm(matriz_erro, j, n)
			if i == 0: #para ter um 1o valor
				erros[j] = norma
				digitos[j] = i
			if norma < erros[j]: #para ser o menor erro e o dígito com menor erro
				digitos[j]=i
				erros[j]=norma
	percentual, acertos, percentual_digito = estatisticas(digitos, n_test)
	print("percentual total: ", percentual, "%")
	print("acertos por dígito", acertos)
	print("percentual de acertos por dígito", percentual_digito)
	elapsed_time_teste_imagens = time.time() - start_time_teste_imagens
	print("  Tempo de execucao teste imagens: "+str(elapsed_time_teste_imagens)+" segundos")
# ------------------------------------------------
if __name__ == "__main__":
    main()