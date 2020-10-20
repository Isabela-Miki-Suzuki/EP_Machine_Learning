import math
import numpy as np
#------------------------------------------------------------------
def rot_givens(w,i,j,k,c,s,m):
    ''' ( array, array, int, int, int, float, float, int )
    RECEBE uma matriz w no formato de numpy.array de floats, de n linhas
    e m colunas e realiza a rotação de givens nas linhas i e j da matriz, 
    a partir da coluna k, com c sendo o cosseno e s, o seno do ângulo
    m é o número de colunas da matriz
    '''
    for r in range(k, m):
        if m > 1:
            aux = c * w[i,r] - s * w[j,r]
            w[j,r] = s * w[i,r] + c * w[j,r]
            w[i,r] = aux
        else:
            aux = c * w[i] - s * w[j]
            w[j] = s * w[i] + c * w[j]
            w[i] = aux
#------------------------------------------------------------------
def sist_simult(w,a, matrizEhColuna):
    ''' ( array, array, bool ) -> (array)/(bool)
    RECEBE uma matriz w e uma matriz a, ambas no formato de numpy.array
    de floats e um boolean indicando se A é uma matriz coluna.
    RETORNA uma matriz no formato numpy.array de floats que representa a
    aproximação para a solução do sistema W*x=A ou false caso o sistema 
    seja indeterminado
    '''
    # triangularização
    n = w.shape[0]
    p = w.shape[1]
    if matrizEhColuna:
        m = 1
    else:
        m = a.shape[1]

    for k in range(p): #para cada coluna
        #varrendo as linhas da última até chegar no elemento anterior ao da diaginal
        for j in range(n-1,k,-1): 
            i=j-1
            if w[j,k] != 0:
                if abs(w[i,k]) > abs(w[j,k]):
                    t = - w[j,k] / w[i,k]
                    c = 1/(math.sqrt(1+t*t))
                    s = c*t
                else:
                    t = - w[i,k] / w[j,k]
                    s = 1/(math.sqrt(1+t*t))
                    c = s*t
                rot_givens(w, i, j, k, c, s, p)
                rot_givens(a, i, j, k, c, s, m)
    # resolução
    h = np.zeros((p,m)) # a matriz resolução já preenchida com zeros
    for k in range(p-1,-1,-1):
        for j in range(m):    
            somatorio=0.
            for i in range(k+1,p):
                somatorio+=w[k,i]*h[i,j]
            if w[k,k] != 0:
                if m > 1:
                    h[k,j]=(a[k,j] - somatorio)/w[k,k]
                else:
                    h[k,j]=(a[k] - somatorio)/w[k,k]
            else:
                print("sistema indeterminado")
                return np.array() #devolve uma array vazia
    return h
#------------------------------------------------------------------
def matriz_coluna(nome):
    ''' -> (bool)
    RETORNA True caso o arquivo seje uma matriz coluna e False caso contrário
    '''
    ## leitura do arquivo
    #verificando se será uma matriz coluna:
    with open(nome, 'r', encoding='utf-8') as arq:
        linhaString = arq.readline()
    linhaArray = linhaString.strip().split(' ')
    if len(linhaArray)==1:
        return True
#------------------------------------------------------------------
def main():
    w = np.loadtxt(input("Digite o nome do arquivo com a matriz W: "))
    arqA = input("Digite o nome do arquivo com a matriz A: ")
    matrizEhColuna = matriz_coluna(arqA)
    a = np.loadtxt(arqA)
    h = sist_simult(w,a, matrizEhColuna)
    if h.shape[0]>0:
        print("matriz solução: ", h)
#------------------------------------------------------------------

#######################################################
###                 FIM                             ###
#######################################################

if __name__ == "__main__":
    main()
