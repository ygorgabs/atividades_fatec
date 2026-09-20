'''
File: cap9_exercicio04.py
Author: Ygor Gabriel
Description: Verifica qual o maior numero e retorna o dobro dele
'''

def maior_valor(num1, num2, num3):
    maior = None

    if num1 > num2 and num1 > num3:
        maior = num1
    elif num2 > num1 and num2 > num3:
        maior = num2
    else:
        maior = num3

    return maior

def dobrar_maior(maior):
    return maior*2

primeiro = int(input("Digite o primeiro valor: "))
segundo = int(input("Digite o segundo valor: "))
terceiro = int(input("Digite o terceiro valor: "))

maior = maior_valor(primeiro, segundo, terceiro)

print(dobrar_maior(maior))