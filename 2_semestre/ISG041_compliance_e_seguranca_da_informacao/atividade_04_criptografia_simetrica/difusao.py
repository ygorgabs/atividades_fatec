import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

chave = os.urandom(32)

def cifrar(txt):
    cifra_obj = Cipher(algorithms.AES(chave), modes.ECB()).encryptor()
    return cifra_obj.update(txt) + cifra_obj.finalize()

ca = cifrar("Protocolo 004470".encode())
cb = cifrar("Protocolo 004471".encode())

diferentes = sum(bin(x ^ y).count("1") for x, y in zip(ca, cb))
print("Bits diferentes:",diferentes,"de 128")