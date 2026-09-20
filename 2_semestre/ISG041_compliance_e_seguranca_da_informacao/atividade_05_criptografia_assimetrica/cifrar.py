from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

message = "Reuniao na sala 12 as 14h"

private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

padd = padding.OAEP(mgf=padding.MGF1(hashes.SHA256()),algorithm=hashes.SHA256(),label=None)

cripto = public_key.encrypt(message.encode(),padd)


print("Mensagem original:",message)
print("Tamanho criptograma",len(cripto),"bytes")
print("Decifrado:",private_key.decrypt(cripto,padd).decode())
print("São iguais:",private_key.decrypt(cripto,padd).decode() == message)