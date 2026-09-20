'''
File: cap5_exercicio03.py
Author: Ygor Gabriel
Description: Verifica se um número está na lista ou não
'''
numeros = [5, 8, 22, 37, 77, 104, 999, 251]
num_user = int(input('Digite um número: '))

if num_user in numeros:
    print(f"O número {num_user} está na lista")
else:
    print(f"O número {num_user} não está na lista")