'''
File: cap8_exercicio04.py
Author: Ygor Gabriel
Description: Listar pessoas de um dicionario
'''
pessoas = [
    {"nome":"Ygor", "sobrenome":"Silva"},
    {"NOME":"Luana", "SOBRENOME":"Silva"},
    {"nome":"Rosangela", "sobrenome":"Bento"},
    {"NOME":"Lucas", "SOBRENOME":"Bento"},
    {"nome":"Pedro", "sobrenome":"Alves"}
]

for pessoa in pessoas:
    nome = pessoa.get("nome",None)
    sobrenome = pessoa.get("sobrenome",None)

    if not nome:
        nome = pessoa.get("NOME",None)

    if not sobrenome:
        sobrenome = pessoa.get("SOBRENOME",None)
    
    print(nome,sobrenome)