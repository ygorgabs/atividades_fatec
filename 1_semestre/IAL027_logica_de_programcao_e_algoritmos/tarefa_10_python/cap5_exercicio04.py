'''
File: cap5_exercicio04.py
Author: Ygor Gabriel
Description: Cria uma lista e exclui um elemento
'''
nomes = []
nomes.append(input('Digite o primeiro nome: '))
nomes.append(input('Digite o segundo nome: '))
nomes.append(input('Digite o terceiro nome: '))
nomes.append(input('Digite o quarto nome: '))
nomes.append(input('Digite o quinto nome: '))

posicao = int(input('Digite uma posição de 0 a 4 para excluir: '))

if posicao >= 0 and posicao <=4 :
    del nomes[posicao]
    print(nomes)
else:
    print('O valor digitado está fora do range')