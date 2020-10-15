
# Constantes
GAP = '_'
#
#------------------------------------------------------------------
def rot_givens(w,i,j,c,s):
    ''' ( list, int, int, float, float )
    RECEBE uma matriz w no formato de lista de listas de floats, de n linhas
    e m colunas e realiza a rotação de givens nas linhas i e j da matriz, com
    c sendo o cosseno do ângulo e s sendo o seno
    '''
    float aux
    for r in range(len(w[0])):
        aux = c * w[i][r] - s * w[j][r]
        w[j][r] = s * w[i][r] + c * w[j][r]
        w[i][r] = aux
        
#------------------------------------------------------------------
def resol_sist(w):
    ''' ( list ) -> (list)
    RECEBE uma matriz w no formato de lista de listas de floats, de n linhas
    e m colunas, a triangulariza por sucessivas rotações de givens e resolve
    o sistema
    RETORNA uma matriz no formato list de 
    '''

    float t
    float c
    float s
    for k in range(len(w[0])): #para cada coluna
        for j in range(len(w)-1,k+2,-1): #varrendo as linhas da última até chegar no elemento anterior ao da diaginal
            i=j-1
            if w[j][k] != 0:
                if abs(w[i][k]) > abs(w[j][k]):
                    t = - w[j][k] / w[i][k]
                    c = 1/(sqrt(1+t*t))
                    s = c*t
                else:
                    t = - w[i][k] / w[j][k]
                    s = 1/(sqrt(1+t*t))
                    c = s*t
                rot_givens(w, i, j,c,s)
                    
#------------------------------------------------------------------
def main():
    
    ## leitura do arquivo
    ## w e b já estão como listas de listas

    print("teste 1:")
    print(pontuacao(5, 5, 3, 'T_CGTAC', 'ATCG___'))
    print("teste 2:")
    print(gera_gaps( 'T' ))
    print("Fim dos meus testes.")

#------------------------------------------------------------------

#######################################################
###                 FIM                             ###
#######################################################

if __name__ == "__main__":
    main()