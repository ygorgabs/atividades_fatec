import hashlib

def h(x):
    return hashlib.sha256(x.encode()).hexdigest()

def calcular_raiz_merkle(doc1, doc2, doc3, doc4):
    folha1 = h(doc1)
    folha2 = h(doc2)
    folha3 = h(doc3)
    folha4 = h(doc4)

    hash_1_2 = h(folha1 + folha2)
    hash_3_4 = h(folha3 + folha4)

    return (hash_1_2 + hash_3_4)

raiz_original = calcular_raiz_merkle("Ata 01", "Ata 02", "Ata 03", "Ata 04")
print(f"Raiz original: {raiz_original}")
raiz_alterada = calcular_raiz_merkle("Ata 01", "Ata 02", "Ata 03(alterada)", "Ata 04")
print(f"Raiz alterada: {raiz_alterada}")
print("A raiz mudou?",raiz_original != raiz_alterada)
