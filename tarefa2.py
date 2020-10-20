from math import *
import numpy as np
import tarefa1

EPSILON = pow(10, -5)
# ------------------------------------------------
# zera valores negativos de uma matriz
def pos(m):
    print(m)
    for i in range(m.shape[0]):
        for j in range(m.shape[1]):
            m[i,j] = max(EPSILON,m[i,j])
    return m
# ------------------------------------------------
# calcula a norma de Frobenius ao quadrado de uma matriz
def norm(m):
    norm = 0.
    for i in range(m.shape[0]):
        for j in range(m.shape[1]):
            norm += pow(m[i,j], 2)
    return norm
# ------------------------------------------------
# normalização das colunas de uma matriz
def normalize_col(m):
    for j in range(m.shape[1]):
        somatorio = 0.
        for i in range(m.shape[0]):
            somatorio += pow(m[i,j], 2)
        somatorio = sqrt(somatorio)
        for i in range(len(m)):
            m[i,j] = m[i,j] / somatorio
# ------------------------------------------------
def mmq_alternado(a, w):
    itmax = 100
    count = 0
    err_anterior = 0.
    a_copy = a.copy()  # cópia da matriz A

    while True:
        normalize_col(w)
        a = a_copy
        # resolução do sistema A=W*H, H é uma matriz pxm não negativa
        h = pos(tarefa1.resol_sist(w, a, False))
        # cálculo do novo erro
        err = norm(a - w@h)
        count += 1  # incrementa o contador
        if (abs(err - err_anterior) <  EPSILON) or (count >= itmax):
            break
        err_anterior = err
        # transpotas das matrizes
        h = h.T
        a = a_copy.T
        # resolução do sistema At=Ht*Wt, nova aproximação de W não negativa
        w = pos(tarefa1.resol_sist(h, a, False)).T
    return h
# ------------------------------------------------
def main():
    a = np.loadtxt(input("Digite o nome do arquivo com a matriz A: "))
    p = int(input("p = "))
    
    # Inicialização aleatória da matriz W nxp
    w = np.ndarray(shape=(a.shape[0], p), dtype=float)
    h = mmq_alternado(a, w)
    print(h)
# ------------------------------------------------
if __name__ == "__main__": 
    main()
