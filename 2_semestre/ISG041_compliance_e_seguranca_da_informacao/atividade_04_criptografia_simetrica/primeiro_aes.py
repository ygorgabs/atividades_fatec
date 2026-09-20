import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

chave = os.urandom(32)
txt_byte = b"Protocolo 004471"

cifra_obj = Cipher(algorithms.AES(chave), modes.ECB()).encryptor()
txt_cripto = cifra_obj.update(txt_byte) + cifra_obj.finalize()

decifra_obj = Cipher(algorithms.AES(chave), modes.ECB()).decryptor()
txt_descripto = decifra_obj.update(txt_cripto) + decifra_obj.finalize()

print("Cifrado:", txt_cripto.hex())
print("Decifrado:", txt_descripto.decode())
print("Decifrado igual ao original:", txt_byte == txt_descripto)