
import math
import numpy
#------------------------------------------------------------------
def rot_givens(w,i,j,c,s,k):
    ''' ( list,list,int, int, float, float )
    RECEBE uma matriz w no formato de lista de listas de floats, de n linhas
    e m colunas e realiza a rotação de givens nas linhas i e j da matriz, com
    c sendo o cosseno do ângulo e s sendo o seno
    '''
    aux=float
    for r in range(k, len(w[0])):
        aux = c * w[i][r] - s * w[j][r]
        w[j][r] = s * w[i][r] + c * w[j][r]
        w[i][r] = aux
#------------------------------------------------------------------
def sist_simult(w,a):
    ''' ( list, list ) -> (list)/(bool)
    RECEBE uma matriz w e uma matriz a, ambas no formato de lista de listas
    de floats.
    RETORNA uma matriz no formato lista de listas de floats que representa a
    solução do sistema W*x=A ou false caso o sistema seja indeterminado
    '''
    # triangularização
    t=float
    c=float
    s=float
    for k in range(len(w[0])): #para cada coluna
        for j in range(len(w)-1,k,-1): #varrendo as linhas da última até chegar no elemento anterior ao da diaginal
            i=j-1
            if w[j][k] != 0:
                if abs(w[i][k]) > abs(w[j][k]):
                    t = - w[j][k] / w[i][k]
                    c = 1/(math.sqrt(1+t*t))
                    s = c*t
                else:
                    t = - w[i][k] / w[j][k]
                    s = 1/(math.sqrt(1+t*t))
                    c = s*t
                rot_givens(w, i, j, c, s, k)
                rot_givens(a, i, j, c, s, k)
    # resolução
    lista = [] # a matriz resolução
    for i in range(len(w[0])): #já formando as linhas
        lista+=[[]]
        for j in range(len(a[0])): #já preenchendo com zeros
            lista[i]+=[0]
    for k in range(len(w[0])-1,-1,-1):
        for j in range(len(a[0])):    
            somatorio=0.
            for i in range(k+1,len(w[0])):
                somatorio+=w[k][i]*lista[i][j]
            if w[k][k] != 0:
                lista[k][j]=(a[k][j] - somatorio)/w[k][k]
            else:
                print("sistema indeterminado")
                return False
    return lista
#------------------------------------------------------------------
def leia_matriz():
    ''' -> (list)
    RETORNA uma lista de listas de floats lida de um arquivo dado
    '''
    ## leitura do arquivo
    nome = input("Digite o nome do arquivo com a matriz: ")
    with open(nome, 'r', encoding='utf-8') as arq:
        texto = arq.read()
    linhas = texto.strip().split('\n') #linhas é uma array com cada elemento sendo uma linha da matriz na forma de string
    #transformando cada linha em uma array com os elementos sendo os elementos da linha
    for i in range(len(linhas)):
        linhas[i] = numpy.fromstring(linhas[i], dtype=float, sep=' ')
    return linhas
#------------------------------------------------------------------
def main():
    w = leia_matriz()
    a = leia_matriz()
    resolucao = sist_simult(w,a)
    if resolucao != False:
        for i in range(len(resolucao)):
            print("x",i+1," = ", resolucao[i][0])
#------------------------------------------------------------------

#######################################################
###                 FIM                             ###
#######################################################

if __name__ == "__main__":
    main()
