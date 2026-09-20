import hashlib, hmac

key = "chave-combinada-entre-secretaria-e-diretoria".encode()

def certifyMessage(msg, tag):
    result = hmac.new(key, msg, hashlib.sha256).digest()
    return hmac.compare_digest(result, tag)


originalMsg = "Reuniao de pais adiada para 20/09".encode()
modifiedMsg = "Reuniao de pais adiada para 27/09".encode()

tag = hmac.new(key, originalMsg, hashlib.sha256).digest()

print("Original:", certifyMessage(originalMsg,tag))
print("Modificada:",certifyMessage(modifiedMsg,tag))