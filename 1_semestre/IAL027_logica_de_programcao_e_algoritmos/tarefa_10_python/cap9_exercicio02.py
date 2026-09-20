'''
File: cap9_exercicio02.py
Author: Ygor Gabriel
Description: Solicita nome e idade do usuario para imprimir
'''
def imprime_user(nome, idade):
    print(f"{nome} possui {idade} anos")

nome_digitado = input("Digite seu nome: ")
idade_digitada = int(input("Digite sua idade: "))

imprime_user(nome_digitado,idade_digitada)