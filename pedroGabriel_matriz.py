import numpy as np
from numpy.linalg import det,inv #FAZ AS OPERACOES

matrizes = []  # LISTA COM INFORMACOES DAS MATRIZES
matriz_x = []  #

with open ("matriz.txt") as arquivo:
    num_matrizes = int(arquivo.readline())
    print("Temos um total de :", num_matrizes, "matrizes" )
    print("Divididas em A , B , C e D !!", '\n')
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' #PARA IDENTIFICAR A MATRIZ

    matrizes = []
    matriz_x = []

    linha = 1
    for chamado in range(num_matrizes):
        limM, colM = arquivo.readline().strip().split(';')

        listADD = []
        for i in range(int(limM)):#PERCORRE AS LINHAS
            elementos = arquivo.readline().strip().split(',')
            listADD.append(elementos)#ADD ELEMENTOS NA LISTA X
        matriz = np.array(listADD, dtype=float) #CRIA AS MATRIZES
        print('A matriz', alfabeto[chamado], 'possui os seguintes valores: \n', '=-=-=-=-=-=-=-=-=-=-=-=-= \n', matriz, '\n =-=-=-=-=-=-=-=-=-=-=-=-= ')
        if matriz.shape[0] == matriz.shape[1]: #caso o número de linhas seja o mesmo número de colunas
            determinante = np.linalg.det(matriz) #descobrindo o determinante atraves do comando linalg (python sempre sendo bom com a gente)
            print('A matriz', alfabeto[chamado], 'tem como determinante:', determinante)
            if determinante == 0:
                print('A matriz', alfabeto[chamado], 'apresenta um determinante igual a zero, assim não é possível calcular a inversa')
            else:
                print('A matriz', alfabeto[chamado], 'apresenta sua inversa igual a: \n \n', np.linalg.inv(matriz), '\n')
        else:
            print('Não podemos calcular o determinante de', alfabeto[chamado])
            print('Não podemos calcular a inversa de', alfabeto[chamado], '\n')

        matrizes.append(matriz) #adção da matriz apos sua conversão
        matriz_x.append(alfabeto[chamado]) #contabilizando e tendo controle das matrizes que já foram
        linha += 1#indo pra proxima linha

    for i in range(num_matrizes - 1):
        if matrizes[i].shape[1] == matrizes[i+1].shape[0]: #caso as matrizes sejam possíveis de serem multiplicadas, seus resultados serão armazenados numa variável auxiliar
            resultado = np.dot(matrizes[i], matrizes[i+1])
            matriz_x.append(matriz_x[i] + matriz_x[i+1])
            matrizes.append(resultado)
            print('A multiplicação das matrizes', matriz_x[i], 'e', matriz_x[i+1], 'resultou na matriz', matriz_x[i] + matriz_x[i+1], '\n', '=-=-=-=-=-=-=-=-=-=-=-=-= \n', resultado, '=-=-=-=-=-=-=-=-=-=-=-=-=')
        else:
            print('As matrizes', matriz_x[i], 'e', matriz_x[i+1], 'nao podem ser multiplicadas')