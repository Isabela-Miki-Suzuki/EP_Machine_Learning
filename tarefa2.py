from math import *
import numpy as np
import tarefa1

EPSILON = pow(10, -5)


# ------------------------------------------------
# troca valores negativos de uma matriz por EPSILON
def pos(w):
    # não tenho certeza se pode isso, seria bom perguntar pro Saulo
    return np.where(w <= 0, EPSILON, w)


# ------------------------------------------------
# normalização das colunas de uma matriz
def normalize_col(w, n, p):
    for j in range(p):
        w[0:n, j] = w[0:n, j] / sqrt((w[0:n, j] ** 2).sum())
    return w


# ------------------------------------------------
def mmq_alternado(a, w, n, m, p):
    itmax = 100
    count = 0
    err = 0.

    while True:
        normalize_col(w, n, p)
        # resolução do sistema A=W*H, H é uma matriz pxm não negativa
        h = pos(tarefa1.resol_sist(a.copy(), w.copy(), n, m, p))
        err_anterior = err
        err = ((a - w @ h) ** 2).sum()  # cálculo do novo erro
        count += 1  # incrementa o contador
        if (abs(err - err_anterior) < EPSILON) or (count >= itmax):
            break
        # resolução do sistema At=Ht*Wt, nova aproximação de W não negativa
        w = pos(tarefa1.resol_sist(a.T.copy(), h.T, m, n, p).T)
    return h


# ------------------------------------------------
def main():
    a = np.loadtxt(input("Digite o nome do arquivo com a matriz A: "))
    n = a.shape[0]
    if a.ndim == 1:
        a = a.reshape(n, 1)
    m = a.shape[1]
    p = int(input("Digite o valor de p: "))

    # Inicialização aleatória da matriz W nxp
    w = np.random.rand(n, p)
    h = mmq_alternado(a, w, n, m, p)
    print(h)
    #print(w)
    #print(w @ h)
    
    
# ------------------------------------------------
if __name__ == "__main__":
    main()
