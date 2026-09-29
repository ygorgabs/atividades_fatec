import hashlib, json

def hash_bloco(bloco):
    texto = json.dumps(bloco, sort_keys=True)
    return hashlib.sha256(texto.encode()).hexdigest()

def novo_bloco(cadeia, dados):
    anterior = cadeia[-1]["hash"] if cadeia else "0" * 64
    bloco = {"indice": len(cadeia),
             "dados": dados,
             "hash_anterior": anterior}
    bloco["hash"] = hash_bloco({k: v for k, v in bloco.items() if k != "hash"})
    return bloco

cadeia = []
for dados in ("Genesis","Diploma 1001 emitido para Ana","Diploma 1002 emitido para Bruno","Diploma 1003 emitido para Carla"):
    cadeia.append(novo_bloco(cadeia,dados))

for block in cadeia:
    print(f"[{block['indice']}] anterior = {block['hash_anterior'][:8]} hash = {block['hash'][:8]} {block['dados']} ")

