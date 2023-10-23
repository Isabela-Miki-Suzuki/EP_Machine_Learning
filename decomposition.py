from math import *
import numpy as np
import rotations_and_system_solving

EPSILON = pow(10, -5)

# ------------------------------------------------
# troca valores negativos de uma matriz por EPSILON
def pos(w):
    return np.where(w <= 0, EPSILON, w)
# ------------------------------------------------
# normalização das colunas de uma matriz
def normalize_col(w):
    return w / np.sqrt(np.sum(w ** 2, axis=0))
# ------------------------------------------------
def mmq_alternado(a, w, n, m, p, method):
    itmax = 100
    err_anterior = 0.

    for _ in range(itmax):
        w = normalize_col(w)
        # resolução do sistema W*H=A, H é uma matriz pxm não negativa
        h = pos(rotations_and_system_solving.resol_sist(a.copy(), w.copy(), n, m, p, method))

        err = ((a - w @ h) ** 2).sum()  # cálculo do novo erro
        if (abs(err - err_anterior) < EPSILON):
            break
        err_anterior = err

        # resolução do sistema Ht*Wt=At, nova aproximação de W não negativa
        w = pos(rotations_and_system_solving.resol_sist(a.T.copy(), h.T, m, n, p, method).T)
    return h,w
# ------------------------------------------------
def main():
    a = np.loadtxt(input("Enter the name of the file in this directory with the matrix A, which will be decomposed as the product of 2 matrices (A = W*H) : "))
    n = a.shape[0]
    if a.ndim == 1:
        a = a.reshape(n, 1)
    m = a.shape[1]
    p = int(input("Enter the value of p, the number of columns of the first matrix in the composition (Wnxp): "))

    method = False 
    if input("Enter the method you want to use (g for givens and h for householder): ") == "g": # método utilizado será a rotação de givens("g") ou householder("h") dependendo do input
        method = True

    # Inicialização aleatória da matriz W nxp
    w = np.random.rand(n, p)
    h,w = mmq_alternado(a, w, n, m, p, method)
    print("W: ", w)
    print("H: ", h)
    print("W*H: ", w@h)
# ------------------------------------------------
if __name__ == "__main__":
    main()


