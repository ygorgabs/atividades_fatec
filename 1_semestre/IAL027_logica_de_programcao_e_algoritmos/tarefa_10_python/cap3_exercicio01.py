'''
File: cap3_exercicio01.py
Author: Ygor Gabriel
Description: Calcula a média e verifica se o aluno foi aprovado
'''
nota1 = float(input('Digite a primeira note: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

media = (nota1 + nota2 + nota3)/3

if media >= 7:
    print('Aluno aprovado')
else:
    print('Aluno reprovado')