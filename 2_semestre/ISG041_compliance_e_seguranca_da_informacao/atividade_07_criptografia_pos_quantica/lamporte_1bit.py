import hashlib, os

def h(x):
    return hashlib.sha256(x).digest()

segredo0 = os.urandom(32)
segredo1 = os.urandom(32)
publico0 = h(segredo0)
publico1 = h(segredo1)

def assinar(bit):
    if bit == 0:
        return segredo0
    elif bit == 1:
        return segredo1
    else:
        raise ValueError("O bit deve ser apenas 0 ou 1")

def verificar(bit, assinatura):
    hash_assinatura = h(assinatura)
    if bit == 0:
        return hash_assinatura == publico0
    elif bit == 1:
        return hash_assinatura == publico1
    else: 
        return False

minha_assinatura = assinar(1)
print("Assinatura verificada para bit para 1?",verificar(1, minha_assinatura))
print("Assinatura verificada para bit para 0?",verificar(0, minha_assinatura))