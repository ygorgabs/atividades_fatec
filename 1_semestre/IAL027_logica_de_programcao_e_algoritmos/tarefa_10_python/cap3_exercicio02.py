'''
File: cap3_exercicio02.py
Author: Ygor Gabriel
Description: Solicita o ano de nascimento e verifica se o usuario fez 18 anos
'''
ano_nasc = int(input('Digite seu ano de nascimento: '))
idade = 2025 - ano_nasc

if idade == 18:
    print('O usuário fez ou fará 18 anos esse ano')