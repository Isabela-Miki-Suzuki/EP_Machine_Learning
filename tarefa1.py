import math
import numpy as np

# ------------------------------------------------------------------
def permut(w, linha1, linha2):
    '''(list, int, int) -> '''
    aux = w[linha1].copy()
    w[linha1] = w[linha2]
    w[linha2] = aux
# ------------------------------------------------------------------
def rot_givens(w, p, i, j, k, c, s):
    ''' ( array, array, int, int, int, float, float, int )
    RECEBE uma matriz W(nxp) no formato de numpy.array de floats e realiza a rotação 
    de givens nas linhas i e j,a partir da coluna k, com c e s, o cosseno e o seno do ângulo
    '''
    w[i, k:p], w[j, k:p] = c * w[i, k:p] - s * w[j, k:p], s * w[i, k:p] + c * w[j, k:p]
# ------------------------------------------------------------------
def resol_sist(a, w, n, m, p):
    ''' ( array, array, int, int, int) -> (array)/(bool)
    RECEBE uma matriz A(nxm) e uma matriz W(nxp), ambas no formato de numpy.array
    de floats.
    RETORNA uma matriz no formato numpy.array de floats que representa a
    aproximação para a solução do sistema W*H=A.
    '''
    # triangularização
    for k in range(p):  # para cada coluna de w
        # varrendo as linhas da última até chegar no elemento anterior ao da diaginal
        for j in range(n - 1, k, -1):
            i = j - 1
            if w[j, k] != 0:
                if abs(w[i, k]) > abs(w[j, k]):
                    t = - w[j, k] / w[i, k]
                    c = 1 / (math.sqrt(1 + t * t))
                    s = c * t
                else:
                    t = - w[i, k] / w[j, k]
                    s = 1 / (math.sqrt(1 + t * t))
                    c = s * t
                rot_givens(w, p, i, j, k, c, s)
                rot_givens(a, m, i, j, 0, c, s)
    h = np.empty((p, m))  # a matriz resolução
    for k in range(p - 1, -1, -1):
        for j in range(m):  # resolvendo os sistemas simultâneos
            if w[k, k] != 0:
                h[k, j] = (a[k, j] - (w[k, k+1:p] * h[k+1:p, j]).sum()) / w[k, k]
            else:
                print("sistema indeterminado")
                return np.array([False])  # devolve uma array de único elemento o boolean False
    return h
# ------------------------------------------------------------------
def matriz_coluna(nome):
    ''' (str)-> (bool)
    RECEBE o nome do arquivo
    RETORNA True caso o arquivo seje uma matriz coluna e False caso contrário
    '''
    ## leitura do arquivo
    # verificando se será uma matriz coluna:
    with open(nome, 'r', encoding='utf-8') as arq:
        linhaString = arq.readline()
    linhaArray = linhaString.strip().split(' ')
    if len(linhaArray) == 1:
        return True
# ------------------------------------------------------------------
def main():
    a = np.loadtxt(input("Digite o nome do arquivo com a matriz A: "))
    n = a.shape[0]
    if a.ndim == 1:  # converte array 1D em matriz coluna
        a = a.reshape(n, 1)
    m = a.shape[1]
    w = np.loadtxt(input("Digite o nome do arquivo com a matriz W: "))
    p = w.shape[1]

    h = resol_sist(a, w, n, m, p)
    if h.shape[0] > 1 or h[0] != False:
        print("matriz solução: ", h)
        #print("w*h: ", w@h)
# ------------------------------------------------------------------

#######################################################
###                 FIM                             ###
#######################################################

if __name__ == "__main__":
    main()
