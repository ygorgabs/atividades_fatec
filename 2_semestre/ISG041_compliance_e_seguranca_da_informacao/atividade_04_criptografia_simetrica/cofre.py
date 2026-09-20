import os 
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

def cifrar(txt, chave):
    iv = os.urandom(16)
    complementador = padding.PKCS7(128).padder()
    txt_completo = complementador.update(txt) + complementador.finalize()
    cp = Cipher(algorithms.AES(chave), modes.CBC(iv)).encryptor()
    return iv + cp.update(txt_completo) + cp.finalize()

def decifrar(pacote, chave):
    iv = pacote[:16]
    cifra = pacote[16:]

    cp = Cipher(algorithms.AES(chave), modes.CBC(iv)).decryptor()
    completo = cp.update(cifra) + cp.finalize()
    descomplementador = padding.PKCS7(128).unpadder()
    return descomplementador.update(completo) + descomplementador.finalize()

usr_input = input("Digite um texto: ").encode()
chave = os.urandom(32)

cifrado1 = cifrar(usr_input, chave)
decifrado1 = decifrar(cifrado1, chave)

cifrado2 = cifrar(usr_input, chave)
decifrado2 = decifrar(cifrado2, chave)

print("Texto cifrado 1:", cifrado1.hex())
print("Texto decifrado 1:",decifrado1.decode())

print("Texto cifrado 2:", cifrado2.hex())
print("Texto decifrado 2:", decifrado1.decode())