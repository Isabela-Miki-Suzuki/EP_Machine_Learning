import math
import numpy as np
#------------------------------------------------------------------
def rot_givens(w,i,j,k,c,s):
    ''' ( array, array, int, int, int, float, float )
    RECEBE uma matriz w no formato de numpy.array de floats, de n linhas
    e m colunas e realiza a rotação de givens nas linhas i e j da matriz, 
    a partir da coluna k, com c sendo o cosseno e s, o seno do ângulo
    '''
    for r in range(k, w.shape[1]):
        aux = c * w[i,r] - s * w[j,r]
        w[j,r] = s * w[i,r] + c * w[j,r]
        w[i,r] = aux
#------------------------------------------------------------------
def sist_simult(w,a):
    ''' ( array, array ) -> (array)/(bool)
    RECEBE uma matriz w e uma matriz a, ambas no formato de numpy.array
    de floats.
    RETORNA uma matriz no formato numpy.array de floats que representa a
    aproximação para a solução do sistema W*x=A ou false caso o sistema 
    seja indeterminado
    '''
    # triangularização
    n = w.shape[0]
    p = w.shape[1]
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
                rot_givens(w, i, j, k, c, s)
                rot_givens(a, i, j, k, c, s)
    # resolução
    h = np.zeros((p,m)) # a matriz resolução já preenchida com zeros
    for k in range(p-1,-1,-1):
        for j in range(m):    
            somatorio=0.
            for i in range(k+1,p):
                somatorio+=w[k,i]*h[i,j]
            if w[k,k] != 0:
                h[k,j]=(a[k,j] - somatorio)/w[k,k]
            else:
                print("sistema indeterminado")
                return False
    return h
#------------------------------------------------------------------
def leia_matriz():
    ''' -> (array)
    RETORNA um numpy.array de floats a partir de uma matriz lida do arquivo dado
    '''
    ## leitura do arquivo
    nome = input("Digite o nome do arquivo com a matriz: ")
    #with open(nome, 'r', encoding='utf-8') as arq:
    #    texto = arq.read() #texto é string
    #linhas = texto.strip().split('\n') #linhas é uma array com cada elemento sendo uma linha da matriz na forma de string
    #transformando cada linha em uma array com os elementos sendo os elementos da linha
    #for i in range(len(linhas)):
    #    linhas[i] = np.fromstring(linhas[i], dtype=float, sep=' ')
    np.loadtxt(nome)
    return linhas
#------------------------------------------------------------------
def main():
    w = np.loadtxt(input("Digite o nome do arquivo com a matriz W: "))
    a = np.loadtxt(input("Digite o nome do arquivo com a matriz A: "))
    h = sist_simult(w,a)
    if h != False:
        for i in range(h.shape[0]):
            print("x",i+1," = ", h[i,0])
#------------------------------------------------------------------

#######################################################
###                 FIM                             ###
#######################################################

if __name__ == "__main__":
    main()
