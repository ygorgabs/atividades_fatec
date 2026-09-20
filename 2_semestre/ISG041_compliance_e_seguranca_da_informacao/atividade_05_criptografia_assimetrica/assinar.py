from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature

private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()
padd = padding.PSS(mgf=padding.MGF1(hashes.SHA256()),salt_length=padding.PSS.MAX_LENGTH)

doc = "Declaro que o aluno concluiu o curso.".encode()
sign = private_key.sign(doc, padd, hashes.SHA256())
print("Assinatura:",len(sign),"bytes")

public_key.verify(sign, doc, padd, hashes.SHA256())
print("Documento original: assinatura válida")

modified = "Declaro que o aluno concluiu o curso!".encode()

try:
    public_key.verify(sign, modified, padd, hashes.SHA256())
except InvalidSignature:
    print("Documento modificado: assinatura inválida")