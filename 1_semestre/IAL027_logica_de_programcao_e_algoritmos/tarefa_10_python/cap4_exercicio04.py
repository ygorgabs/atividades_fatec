'''
File: cap4_exercicio04.py
Author: Ygor Gabriel
Description: Solicita nome completo e exibe somente o segundo nome
'''
nome_completo = input('Digite seu nome completo: ')
nome_dividido = nome_completo.split(" ")

print(nome_dividido[1])