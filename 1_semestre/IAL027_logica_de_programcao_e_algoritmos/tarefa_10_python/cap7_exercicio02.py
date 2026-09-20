'''
File: cap7_exercicio02.py
Author: Ygor Gabriel
Description: Exibe os valores pares entre 1 e 10 usando while
'''
numeros = [1,2,3,4,5,6,7,8,9,10]
contador = 0

while contador < len(numeros):

    if numeros[contador] % 2 == 0:
        print(numeros[contador])
        
    contador += 1
