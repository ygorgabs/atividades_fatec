import hashlib, json

def hash_bloco(bloco):
    campos = {k: v for k, v in bloco.items() if k != "hash"}
    return hashlib.sha256(json.dumps(campos, sort_keys=True).encode()).hexdigest()

def novo_bloco(cadeia, dados):
    anterior = cadeia[-1]["hash"] if cadeia else "0" * 64
    bloco = {"indice": len(cadeia),
             "dados": dados,
             "hash_anterior": anterior}
    bloco["hash"] = hash_bloco(bloco)
    return bloco

def validar(cadeia):
    for i, b in enumerate(cadeia):
        if b['hash'] != hash_bloco(b):
            return f"INVÁLIDA - bloco {i} foi alterado"
        if i > 0 and b['hash_anterior'] != cadeia[i - 1]['hash']:
            return f"INVÁLIDA - bloco {i} elo quebrado"
    return "VALIDA"

cadeia = []
for dados in ("Genesis","Diploma 1001 emitido para Ana","Diploma 1002 emitido para Bruno","Diploma 1003 emitido para Carla"):
    cadeia.append(novo_bloco(cadeia,dados))

print("Cadeia original:", validar(cadeia))

cadeia[2][dados] = "Diploma 1002 emitido para Bruna" 
print("Após alteração:",validar(cadeia))



