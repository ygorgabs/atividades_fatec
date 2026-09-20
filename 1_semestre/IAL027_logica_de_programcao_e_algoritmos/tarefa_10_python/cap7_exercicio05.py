'''
File: cap7_exercicio05.py
Author: Ygor Gabriel
Description: Exibe os valores de posições menores de 5
'''
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
posicao = 0

while posicao < len(numeros):
    
    if posicao < 5 and posicao != 2:
        print(numeros[posicao])
    
    posicao += 1