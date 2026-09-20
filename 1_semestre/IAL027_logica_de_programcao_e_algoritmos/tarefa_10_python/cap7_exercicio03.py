'''
File: cap7_exercicio03.py
Author: Ygor Gabriel
Description: Cria uma lista de 10 valores impares digitados pelo usuário
'''

numeros = []
contador = 0

while contador <= 10:
    num = 0
    while num % 2 == 0:
        num = int(input('Digite um número impar: '))
    
    numeros.append(num)
    contador +=1

posicao = 0
while posicao < len(numeros):
    print(numeros[posicao])
    posicao += 1