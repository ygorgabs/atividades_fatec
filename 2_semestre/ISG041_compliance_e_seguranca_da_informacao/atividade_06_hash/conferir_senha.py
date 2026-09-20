import hashlib

def getHash(password):
    return hashlib.sha256(password.encode()).hexdigest()

def compareHash(hash1, hash2):
    return "ACEITA" if hash1 == hash2 else "Rescusada"

password = getHash("fatec2026")
print("Hash guardado:",password)
print("fatec2025 ->",compareHash(password,getHash("fatec2025")))
print("Fatec2026 ->",compareHash(password,getHash("Fatec2026")))
print("fatec2026 ->",compareHash(password,getHash("fatec2026")))