'''
File: cap10_exercicio05.py
Author: Ygor Gabriel
Description: Exibe os números pares digitados pelo usuario
'''
def escrever_array(array):
    for valor in array:
        print(valor)

numeros = []

for indice in range(10):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

pares = filter(lambda numero: numero % 2 == 0, numeros)
impares = filter(lambda numero: numero % 2 == 1, numeros)

escrever_array(pares)
escrever_array(impares)