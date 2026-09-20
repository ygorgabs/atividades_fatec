import os 
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def derivar(senha, sal):
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=sal, iterations=600000)
    return kdf.derive(senha)

usr_input = input("Digite uma senha: ").encode()
sal1 = os.urandom(16)
sal2 = os.urandom(16)

print("Sal 1:",derivar(usr_input, sal1).hex()[:16])
print("Sal 2:",derivar(usr_input,sal2).hex()[:16])
print("Sal 1:",derivar(usr_input, sal1).hex()[:16])