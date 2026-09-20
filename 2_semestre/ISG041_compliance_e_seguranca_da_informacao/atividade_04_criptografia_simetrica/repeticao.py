import os 
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

chave = os.urandom(32)
txt_byte = b"Protocolo 004471" * 4

cifra_ecb = Cipher(algorithms.AES(chave),modes.ECB()).encryptor()
txt_ecb = cifra_ecb.update(txt_byte) + cifra_ecb.finalize()

for i in range(0, len(txt_ecb),16):
    print(txt_ecb[i:i+16].hex())

print()

iv = os.urandom(16)
cifra_cbc = Cipher(algorithms.AES(chave),modes.CBC(iv)).encryptor()
txt_cbc = cifra_cbc.update(txt_byte) + cifra_cbc.finalize()

for i in range(0, len(txt_cbc),16):
    print(txt_cbc[i:i + 16].hex())