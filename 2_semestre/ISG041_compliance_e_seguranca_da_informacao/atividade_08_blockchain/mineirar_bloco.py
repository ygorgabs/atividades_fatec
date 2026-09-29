import hashlib

def mineirar(dados, dificuldade):
    alvo = "0" * dificuldade
    nonce = 0
    while True:
        h = hashlib.sha256(f"{dados}{nonce}".encode()).hexdigest()
        if h.startswith(alvo):
            return nonce, h
        nonce += 1

for d in (1, 2, 3, 4):
    nonce, h = mineirar("Diploma 1001 emitido para Ana", d)
    print(f"Dificuldade {d}: nonce = {nonce:>8} hash = {h[:12]}...")