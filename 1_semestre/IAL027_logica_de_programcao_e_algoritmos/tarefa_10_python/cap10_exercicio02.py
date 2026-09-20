'''
File: cap10_exercicio02.py
Author: Ygor Gabriel
Description: Solicita nome e idade e retorna com função lambda
'''
escrever_nome_idade = lambda nome, idade: print(f"{nome} possui {idade} anos.")
nome_digitado = str(input("Digite seu nome: "))
idade_digitada = int(input("Digite sua idade: "))
escrever_nome_idade(nome_digitado, idade_digitada)