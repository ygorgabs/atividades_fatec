'''
File: cap8_exercicio03.py
Author: Ygor Gabriel
Description: Verifica o item mais caro e o mais barato da lista
'''

compras = [
    {"Descrição":"Arroz", "Preço":25.00},
    {"Descrição":"Feijão", "Preço":8.00},
    {"Descrição":"Frango", "Preço":15.00},
    {"Descrição":"Alface", "Preço":3.00},
    {"Descrição":"Batata", "Preço":10.00}
]

contador = 0
mais_barato = None
mais_caro = None

while contador < len(compras):

    item = compras[contador]
    if contador == 0:
        mais_barato = item
        mais_caro = item
    else:
        if item["Preço"] > mais_caro["Preço"]:
            mais_caro = item
        
        if item["Preço"] < mais_barato["Preço"]:
            mais_barato = item

    contador += 1

print(f"Produto mais caro: {mais_caro["Descrição"]} por {mais_caro["Preço"]} reais")   
print(f"Produto mais barato: {mais_barato["Descrição"]} por {mais_barato["Preço"]} reais") 