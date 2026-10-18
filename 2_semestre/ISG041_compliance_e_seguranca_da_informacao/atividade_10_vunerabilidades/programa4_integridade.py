# Aula 10 - Programa 4: linha de base de integridade dos arquivos do sistema
# Proposito: detectar arquivos do sistema substituidos (trojan, rootkit) por linha de base de hashes. Pergunta: o que mudou?
import hashlib, os

def sha256(caminho):
    with open(caminho, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

# 1) estado conhecido e confiavel: grava-se o hash de cada arquivo
os.makedirs("sistema", exist_ok=True)
for nome, conteudo in {"login.exe": b"programa de login v1",
                       "rede.dll":  b"biblioteca de rede v1",
                       "config.ini": b"porta=443"}.items():
    open(f"sistema/{nome}", "wb").write(conteudo)
linha_de_base = {nome: sha256(f"sistema/{nome}") for nome in os.listdir("sistema")}

# 2) tempo depois: um arquivo foi substituido e outro apareceu
# open("sistema/login.exe", "wb").write(b"programa de login v1 MODIFICADO")
open("sistema/desconhecido.exe", "wb").write(b"conteudo desconhecido")

# 3) verificacao: compara o estado atual com a linha de base
for nome in sorted(set(linha_de_base) | set(os.listdir("sistema"))):
    if nome not in linha_de_base:
        print(f"{nome:<18} NOVO      - nao estava na linha de base")
    elif not os.path.exists(f"sistema/{nome}"):
        print(f"{nome:<18} REMOVIDO")
    elif sha256(f"sistema/{nome}") != linha_de_base[nome]:
        print(f"{nome:<18} ALTERADO  - hash diferente da linha de base")
    else:
        print(f"{nome:<18} ok")
