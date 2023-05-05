import numpy as np #IMPORTA A BIBLIOTECA
from numpy.linalg import det,inv #FAZ AS OPERACOES

matrizes = []  #LISTA COM INFORMACOES DAS MATRIZES
matriz_nome = []  #NOME DA MATRIZ

with open ("matriz.txt") as arquivo:
    num_matrizes = int(arquivo.readline())
    print("Temos um total de :", num_matrizes, "matrizes" )
    print("Divididas em A , B , C e D !!", '\n')
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' #PARA IDENTIFICAR A MATRIZ

    linha = 1
    for chamado in range(num_matrizes):
        limM, colM = arquivo.readline().strip().split(';')

        listADD = []
        for i in range(int(limM)): #PERCORRE AS LINHAS
            elementos = arquivo.readline().strip().split(',')
            listADD.append(elementos) #ADD ELEMENTOS NA LISTA X
        matriz = np.array(listADD, dtype=float) #CRIA AS MATRIZES
        print('A matriz', alfabeto[chamado], 'possui os seguintes valores: \n', '=-=-=-=-=-=-=-=-=-=-=-=-= \n', matriz, '\n =-=-=-=-=-=-=-=-=-=-=-=-= ')
        if matriz.shape[0] == matriz.shape[1]: #VERIFICA SE O NUMERO DE LINHAS == COLUNAS
            determinante = np.linalg.det(matriz) # O NUMPY POSSUI O LINANG QUE DESCOBRE O DETERMINANTE DA MATRIZ
            print('A matriz', alfabeto[chamado], 'tem como determinante:', determinante)
            if determinante == 0:
                print('A matriz', alfabeto[chamado], 'possui determinante igual a zero, assim não é possível calcular a inversa')
            else:
                print('A matriz', alfabeto[chamado], 'possui sua inversa igual a: \n \n', np.linalg.inv(matriz), '\n')
        else:
            print('Não podemos calcular o determinante de', alfabeto[chamado])
            print('Não podemos calcular a inversa de', alfabeto[chamado], '\n')

        matrizes.append(matriz)#CONTABILIZADA AS MATRIZES QUE FORAM
        matriz_nome.append(alfabeto[chamado]) #MATRIZES QUE JA FORAM
        linha += 1#PROX LINHA

    for i in range(num_matrizes - 1):
        if matrizes[i].shape[1] == matrizes[i+1].shape[0]: #VERIFICA SE AS MATRIZES PODEM SER MULTIPLICADAS
            resultado = np.dot(matrizes[i], matrizes[i+1])
            matriz_nome.append(matriz_nome[i] + matriz_nome[i+1])
            matrizes.append(resultado)
            print('A multiplicação das matrizes', matriz_nome[i], 'e', matriz_nome[i+1], 'é igual a: ', matriz_nome[i] + matriz_nome[i+1], '\n', '=-=-=-=-=-=-=-=-=-=-=-=-= \n', resultado, '=-=-=-=-=-=-=-=-=-=-=-=-=') #RESULTADO DAS MATRIZES
        else:
            print('As matrizes', matriz_nome[i], 'e', matriz_nome[i+1], 'nao podem ser multiplicadas') #DEMONSTRA QUE AS MATRIZES EM QUESTAO NAO PODEM SER MULTIPLICADAS