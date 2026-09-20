import os 
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.exceptions import InvalidTag

chave = AESGCM.generate_key(bit_length=256)
cofre = AESGCM(chave)
nonce = os.urandom(12)

cripto = cofre.encrypt(nonce, "Empenho aprovado no valor de R$1.000,00".encode(), None)
print("Sem alteração: ",cofre.decrypt(nonce, cripto, None))

adulterado = bytearray(cripto)
adulterado[0] ^= 1
try:
    cofre.decrypt(nonce, bytes(adulterado), None)
except InvalidTag:
    print("Texto original modificado: InvalidTag Exception")