'''
File: cap9_exercicio05.py
Author: Ygor Gabriel
Description: Solicita nomes e adciona na lista usando funçoes
'''
def solicitar_nome():
    return str(input("Digite um nome: "))

def adicionar_a_lista(lista, nome):
    lista.append(nome)

def imprimir_nomes(lista):
    for nome in lista:
        print(nome)

nomes = []

for i in range(5):
    nome = solicitar_nome()
    adicionar_a_lista(nomes,nome)

imprimir_nomes(nomes)


