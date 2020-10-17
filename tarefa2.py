from math import *
import numpy as np
import tarefa1
# ------------------------------------------------
# zera valores negativos de uma matriz
def pos(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            m[i][j] = max(0, m[i][j])
    return m
# ------------------------------------------------
# calcula a norma de Frobenius ao quadrado de uma matriz
def norm(m):
    norm = 0.
    for i in range(len(m)):
        for j in range(len(m[0])):
            norm += pow(m[i][j], 2)
    return norm
# ------------------------------------------------
# normalização das colunas de uma matriz
def normalize_col(m):
    for j in range(len(m[0])):
        somatorio = 0.
        for i in range(len(m)):
            somatorio += pow(m[i][j], 2)
        somatorio = sqrt(somatorio)
        for i in range(len(m)):
            m[i][j] = m[i][j] / somatorio
# ------------------------------------------------
def mmq_alternado(a, w):
    epsilon = pow(10, -5)
    itmax = 100
    count = 0
    err = epsilon
    err_anterior = 0.
    a_copy = a.copy()  # cópia da matriz A

    while True:
        normalize_col(w)
        a = a_copy
        # resolução do sistema A=W*H, H é uma matriz pxm não negativa
        h = pos(tarefa1.sist_simult(w, a))
        # cálculo do novo erro
        err = norm((np.array(a) - np.array(w) @ np.array(h)).tolist())
        count += 1  # incrementa o contador
        if (abs(err - err_anterior) < epsilon) or (count >= itmax):
            break
        err_anterior = err
        # transpotas das matrizes
        h = np.array(h).T.tolist()
        a = np.array(a_copy).T.tolist()
        # resolução do sistema At=Ht*Wt, nova aproximação de W não negativa
        w = np.array(pos(tarefa1.sist_simult(h, a))).T.tolist()
    return h
# ------------------------------------------------
def main():
    # leitura da matriz A nxm
    print("Matrix A")
    n = int(input("number of rows, n = "))
    m = int(input("number of columns, m = "))
    a = []
    for i in range(0, n):
        a.append([float(j) for j in input().split()])

    p = int(input("p = "))

    # Inicialização aleatória da matriz W nxp
    w = np.random.rand(n, p).tolist()
    h = mmq_alternado(a, w)
    print(h)
# ------------------------------------------------
if __name__ == "__main__":
    main()
