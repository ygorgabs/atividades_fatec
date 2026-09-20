'''
File: cap8_exercicio02.py
Author: Ygor Gabriel
Description: Crie uma lista de dicionarios
'''
compras = [
    {"Descrição":"Arroz", "Preço":25.00},
    {"Descrição":"Feijão", "Preço":8.00},
    {"Descrição":"Frango", "Preço":15.00},
    {"Descrição":"Alface", "Preço":3.00},
    {"Descrição":"Batata", "Preço":10.00}
]

for item in compras:
    print(f"Produto: {item["Descrição"]} por {item["Preço"]} reais")