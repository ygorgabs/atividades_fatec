'''
File: cap7_exercicio04.py
Author: Ygor Gabriel
Description: Lista de opções com while
'''
opcoes = [1,2,3]
opcao = 0

while opcao not in opcoes:
    print("Selecione uma das opções a seguir:\n1- Olá mundo \n2- Eu programo em python \n3- Laços de repetição")
    opcao = int(input('Digite a opção: '))

if opcao == 1:
    print("Olá mundo!")
elif opcao == 2:
    print("Esta é minha lição de python")
else:
    print("Esta é uma tarafa do laço while")