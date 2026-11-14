# Aula 11 - Programa 5: componentes vulneraveis (A06 / cadeia de suprimentos)
# Proposito: comparar as versoes instaladas com os boletins publicados - a analise de composicao de software (SCA) em miniatura.
instalados = {"django": "3.2.4", "requests": "2.31.0", "pillow": "8.1.0", "jinja2": "3.1.2"}

# boletins publicos: pacote -> (primeira versao corrigida, identificador, gravidade)
boletins = {"django": ("3.2.25", "CVE-2024-27351", "alta"),
            "pillow": ("9.0.1",  "CVE-2022-22817", "critica"),
            "jinja2": ("3.1.3",  "CVE-2024-22195", "media")}

def versao(texto):
    return tuple(int(parte) for parte in texto.split("."))    # "3.2.4" -> (3, 2, 4)

for pacote, v in instalados.items():
    if pacote in boletins:
        corrigida, cve, gravidade = boletins[pacote]
        if versao(v) < versao(corrigida):
            print(f"VULNERAVEL  {pacote:<9} {v:<8} atualizar para {corrigida:<7} {cve} ({gravidade})")
            continue
    print(f"ok          {pacote:<9} {v}")
