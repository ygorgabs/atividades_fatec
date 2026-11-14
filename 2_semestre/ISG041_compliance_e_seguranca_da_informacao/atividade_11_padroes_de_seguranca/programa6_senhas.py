# Aula 11 - Programa 6: senhas conforme a orientacao atual (A07)
# Proposito: aplicar as duas regras que importam - comprimento e lista de senhas conhecidas - e guardar com sal e PBKDF2.
import hashlib, os

CONHECIDAS = {"123456", "senha", "password", "12345678", "qwerty", "fatec2026", "admin123"}

def avaliar(senha):
    problemas = []
    if len(senha) < 12:
        problemas.append("menos de 12 caracteres")
    if senha.lower() in CONHECIDAS:
        problemas.append("consta de lista de senhas conhecidas")
    return problemas

def guardar(senha):                              # nunca a senha: sal + hash lento (aula 6)
    sal = os.urandom(16)
    return sal, hashlib.pbkdf2_hmac("sha256", senha.encode(), sal, 600_000)

for s in ("123456", "fatec2026", "Primavera2026", "cafe com leite as 7h"):
    problemas = avaliar(s)
    if problemas:
        print(f"REJEITADA  {s:<22} {'; '.join(problemas)}")
    else:
        sal, h = guardar(s)
        print(f"aceita     {s:<22} guardado: sal={sal.hex()[:8]}... hash={h.hex()[:16]}...")
