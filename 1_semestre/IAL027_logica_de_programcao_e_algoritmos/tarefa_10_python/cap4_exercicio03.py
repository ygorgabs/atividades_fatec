'''
File: cap4_exercicio03.py
Author: Ygor Gabriel
Description: Verifica se a idade digitada é válida
'''
idade = input('Digite sua idade: ')
if idade.isdigit():
    print(f"Você tem {idade} anos.")
else:
    print("Você digitou uma idade inválida")