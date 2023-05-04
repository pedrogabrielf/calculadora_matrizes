import numpy as np
from numpy.linalg import det, inv #biblioteca para operações nas matrizes
from colorama import Fore, Style #deixa mais organizado e esteticamene agradavel

print(Fore.RED, "------ATENÇÃO----- \n", Style.RESET_ALL,  "Cada cor representa um resultado")
print(Fore.RED, "Respresenta o número de matrizes totais", Style.RESET_ALL)
print(Fore.GREEN, "Represenra o número de linhas e colunas", Style.RESET_ALL)
print(Fore.BLUE, "Representa o nome e os elementos das matrizes", Style.RESET_ALL)
print(Fore.YELLOW, "Representa caso não seja possível calcular a inversa da matriz", Style.RESET_ALL)
print(Fore.MAGENTA, "Representa se o determinante da matriz",Style.RESET_ALL)
print(Fore.LIGHTYELLOW_EX, "Representa quando não é possível calcular a inversa, pois det=0",Style.RESET_ALL)
print(Fore.LIGHTBLUE_EX, "Representa quando não é possível calcular o determinante",Style.RESET_ALL)
print(Fore.LIGHTRED_EX, "Represena quando não é possível multiplicar as matrizes",Style.RESET_ALL)
print(Fore.LIGHTMAGENTA_EX, "Representa o resultado de uma multiplicação \n \n \n",Style.RESET_ALL)

with open("matriz.txt") as arquivo: #abrindo um arquivo com as infos
    num_matrizes = int(arquivo.readline()) #quantidade de matrizes no total, num=número
    print(Fore.RED + "O número de matrizes é", num_matrizes,":" + Style.RESET_ALL)
    nomenclatura = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' #nome que cada matriz irá receber
    
    matrizes = [] #lista que irá ser preenchida com as infos das matrizes
    matriz_x = []#aqui será o nome da matriz, para saber a letra que setá colocada (x é o número)
    
    linha = 1#definir a linhas que o for vai começar 
    for chamado in range(num_matrizes):#vai analizar de acordo com o número de matrizes totais
        limM, colM = arquivo.readline().strip().split(';')
        print(Fore.GREEN + "O número de linhas e colunas da matriz", nomenclatura[chamado], "é:", limM, "-", colM + ":", Style.RESET_ALL)

        m = [] #lista auxliar
        for i in range(int(limM)):#percorrerá o número de linhas
            elementos = arquivo.readline().strip().split(',')
            m.append(elementos)#adicionará os elementos na lista auxiliar
        matriz = np.array(m, dtype=float) #reaizando uma coversão em um array numpy de floats(temos que fazer isso para criar matrizes e realizar operações)
        print(Fore.BLUE, 'Temos a matriz', nomenclatura[chamado], 'com os seguintes valores: \n', '-------------------- \n', matriz, '--------------------' + Style.RESET_ALL)
        if matriz.shape[0] == matriz.shape[1]: #caso o número de linhas seja o mesmo número de colunas
            determinante = np.linalg.det(matriz) #descobrindo o determinante atraves do comando linalg (python sempre sendo bom com a gente)
            print(Fore.MAGENTA, 'a matriz', nomenclatura[chamado], 'tem como determinsnte:', determinante, Style.RESET_ALL)
            if determinante == 0:
                print(Fore.LIGHTYELLOW_EX, 'a', nomenclatura[chamado], 'apresenta um determinante igual a zero, assim não é possível calcular a inversa', Style.RESET_ALL)
            else:
                print(Fore.CYAN, 'a matriz', nomenclatura[chamado], 'apresenta sua inversão sendo igual a', np.linalg.inv(matriz), Style.RESET_ALL)
        else:
            print(Fore.LIGHTBLUE_EX, 'Não é possível calcular o determinante de', nomenclatura[chamado], Style.RESET_ALL)
            print(Fore.YELLOW, 'Não é possível calcular a inversa de', nomenclatura[chamado], Style.RESET_ALL)

        matrizes.append(matriz) #adção da matriz apos sua conversão
        matriz_x.append(nomenclatura[chamado]) #contabilizando e tendo controle das matrizes que já foram
        linha += 1#indo pra proxima linha

    for i in range(num_matrizes - 1):
        if matrizes[i].shape[1] == matrizes[i+1].shape[0]: #caso as matrizes sejam possíveis de serem multiplicadas, seus resultados serão armazenados numa variável auxiliar
            resultado = np.dot(matrizes[i], matrizes[i+1])
            matriz_x.append(matriz_x[i] + matriz_x[i+1])
            matrizes.append(resultado)
            print(Fore.GREEN, 'A multiplicação das matrizes', matriz_x[i], 'e', matriz_x[i+1], 'resultou na matriz', matriz_x[i] + matriz_x[i+1], '\n', '-------------------- \n', resultado, '--------------------' + Style.RESET_ALL)
        else:
            print(Fore.LIGHTRED_EX, 'Não foi possível multiplicar as matrizes', matriz_x[i], 'e', matriz_x[i+1], Style.RESET_ALL)