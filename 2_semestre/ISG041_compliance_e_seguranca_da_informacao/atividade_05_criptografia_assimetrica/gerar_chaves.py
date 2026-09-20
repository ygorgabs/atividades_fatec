from cryptography.hazmat.primitives.asymmetric import rsa

private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

print("Par de chaves gerado.")
print("Tamanho da chave:",private_key.key_size,"bits")
print("Expoente publico:", public_key.public_numbers().e)
