'''
File: cap6_exercicio04.py
Author: Ygor Gabriel
Description: Solicita valores para o usuario e adiciona a lista
'''
numeros = []

for i in range(10):
    digitado = int(input(f'Digite o {i+1}º valor: '))

    if digitado % 2 == 0:
        digitado += 1
    
    numeros.append(digitado)

for num in numeros:
    print(num)