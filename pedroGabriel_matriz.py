import numpy as np
from numpy.linalg import det,inv #FAZ AS OPERACOES

matrizes = []  # LISTA COM INFORMACOES DAS MATRIZES
matriz_x = []  #

with open ("matriz.txt") as arquivo:
    num_matrizes = int(arquivo.readline())
    print("Temos um total de :", num_matrizes, "matrizes" )
    print("Divididas em A , B , C e D !!")
    nomenclatura = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    matrizes = []
    matriz_x = []

    linha = 1
    for chamado in range(num_matrizes):
        limM, colM = arquivo.readline().strip().split(';')

        m = []
        for i in range(int(limM)):#percorrerá o número de linhas
            elementos = arquivo.readline().strip().split(',')
            m.append(elementos)#adicionará os elementos na lista auxiliar
        matriz = np.array(m, dtype=float) #reaizando uma coversão em um array numpy de floats(temos que fazer isso para criar matrizes e realizar operações)
        print('A matriz', nomenclatura[chamado], 'possui os seguintes valores: \n', '=-=-=-=-=-=-=-=-=-= \n', matriz, '\n =-=-=-=-=-=-=-=-=-= ')
        if matriz.shape[0] == matriz.shape[1]: #caso o número de linhas seja o mesmo número de colunas
            determinante = np.linalg.det(matriz) #descobrindo o determinante atraves do comando linalg (python sempre sendo bom com a gente)
            print('A matriz', nomenclatura[chamado], 'tem como determinante:', determinante)
            if determinante == 0:
                print('A matriz', nomenclatura[chamado], 'apresenta um determinante igual a zero, assim não é possível calcular a inversa')
            else:
                print('A matriz', nomenclatura[chamado], 'apresenta sua inversa igual a: \n \n', np.linalg.inv(matriz))
        else:
            print('Não podemos calcular o determinante de', nomenclatura[chamado])
            print('Não podemos calcular a inversa de', nomenclatura[chamado])

        matrizes.append(matriz) #adção da matriz apos sua conversão
        matriz_x.append(nomenclatura[chamado]) #contabilizando e tendo controle das matrizes que já foram
        linha += 1#indo pra proxima linha

    for i in range(num_matrizes - 1):
        if matrizes[i].shape[1] == matrizes[i+1].shape[0]: #caso as matrizes sejam possíveis de serem multiplicadas, seus resultados serão armazenados numa variável auxiliar
            resultado = np.dot(matrizes[i], matrizes[i+1])
            matriz_x.append(matriz_x[i] + matriz_x[i+1])
            matrizes.append(resultado)
            print('A multiplicação das matrizes', matriz_x[i], 'e', matriz_x[i+1], 'resultou na matriz', matriz_x[i] + matriz_x[i+1], '\n', '-------------------- \n', resultado, '--------------------')
        else:
            print('Não foi possível multiplicar as matrizes', matriz_x[i], 'e', matriz_x[i+1])