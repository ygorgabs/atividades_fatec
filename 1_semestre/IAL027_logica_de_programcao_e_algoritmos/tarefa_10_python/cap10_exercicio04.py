'''
File: cap10_exercicio04.py
Author: Ygor Gabriel
Description: Solicita valores ao usuario e exibe somente os maiores que 10
'''
numeros = []
for indice in range(5):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

maiores = filter(lambda numero: numero > 10, numeros)

for maior in maiores:
    print(maior)