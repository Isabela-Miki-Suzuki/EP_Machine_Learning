
import math
#------------------------------------------------------------------
def rot_givens(w,b,i,j,c,s):
    ''' ( list,list,int, int, float, float )
    RECEBE uma matriz w no formato de lista de listas de floats, de n linhas
    e m colunas e uma matriz b (lista de floats) e realiza a rotação de 
    givens nas linhas i e j das matrizes, com c sendo o cosseno do ângulo e s sendo o seno
    '''
    aux=float
    for r in range(len(w[0])):
        aux = c * w[i][r] - s * w[j][r]
        w[j][r] = s * w[i][r] + c * w[j][r]
        w[i][r] = aux
    aux = c * b[i] - s * b[j]
    b[j] = s * b[i] + c * b[j]
    b[i] = aux
        
#------------------------------------------------------------------
def resol_sist(w,b):
    ''' ( list, list ) -> (list)
    RECEBE uma matriz w no formato de lista de listas de floats, de n linhas
    e m colunas e uma matriz b no formato de lista de floats a triangulariza 
    por sucessivas rotações de givens e resolve o sistema
    RETORNA uma matriz no formato list de 
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
                rot_givens(w, b, i, j,c,s)
    # resolução
    lista = [] # a matriz resolução
    for i in range(len(w[0])):
        lista+=[0]
    lista[len(w[0])-1]=b[len(w[0])-1]/w[len(w[0])-1][len(w[0])-1]
    for k in range(len(w[0])-2,-1,-1):
        somatorio=0.
        for j in range(k+1,len(w[0])):
            somatorio+=w[k][j]*lista[j]
        lista[k]=(b[k] - somatorio)/w[k][k]
    return lista
#------------------------------------------------------------------
def main():
    
    ## leitura do arquivo
    ## w e b já estão como listas de listas/floats

    resolucao = resol_sist(w,b)
#------------------------------------------------------------------

#######################################################
###                 FIM                             ###
#######################################################

if __name__ == "__main__":
    main()