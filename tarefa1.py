
# Constantes
DNA = 'ATCG'
GAP = '_'
#
def rot_givens(w,n,m,i,j,c,s):
    ''' ( list, int, int, int, int, float, float )
    RECEBE uma matriz w no formato de lista de listas de floats, de n linhas
    e m colunas e realiza a rotação de givens nas linhas i e j da matriz, com
    c sendo o cosseno do ângulo e s sendo o seno
    '''
    float aux
    for r in range(m):
        aux = c * w[i][r] - s * w[j][r]
        w[j][r] = s * w[i][r] + c * w[j][r]
        w[i][r] = aux
        
#------------------------------------------------------------------
def main():
    '''
        Modifique essa função, escrevendo os seus testes.
    '''

    ## Escreva aqui os testes para a função gera_gaps
    # 
    print("teste 1:")
    print(pontuacao(5, 5, 3, 'T_CGTAC', 'ATCG___'))
    print("teste 2:")
    print(gera_gaps( 'T' ))
    ## Escreva aqui os testes para a função pontuação
    #         
    print("Fim dos meus testes.")

#------------------------------------------------------------------

#######################################################
###                 FIM                             ###
#######################################################

if __name__ == "__main__":
    main()