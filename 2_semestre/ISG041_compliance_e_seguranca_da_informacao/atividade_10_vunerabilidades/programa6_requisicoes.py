# Aula 10 - Programa 6: pico legitimo ou ataque de negacao de servico?
# Proposito: separar pico legitimo de ataque por taxa, origens e requisicoes por origem. Pergunta: e pico ou ataque?
from collections import Counter

def janela(pares):                      # (ip, quantidade) -> lista com uma entrada por requisicao
    lista = []
    for ip, n in pares:
        lista += [ip] * n
    return lista

# requisicoes recebidas pelo site em tres janelas de 10 segundos
janelas = {
    "03:00 madrugada": janela([(f"203.0.113.{i}", 1)   for i in range(1, 9)]),     # 8 req de 8 IPs
    "20:00 promocao":  janela([(f"198.51.100.{i}", 3)  for i in range(1, 201)]),   # 600 req de 200 IPs
    "20:10 ataque":    janela([(f"192.0.2.{i}", 400)   for i in range(1, 21)]),    # 8000 req de 20 IPs
    "20:20 botnet": janela([(f"10.{i // 256}.{i % 256}.9", 4) for i in range(1, 2001)]),
}

for nome, reqs in janelas.items():
    total = len(reqs)
    ips = len(Counter(reqs))
    media = total / ips
    taxa = total / 10                                    # requisicoes por segundo
    if taxa > 300 and media > 50:
        veredito = "ATAQUE: poucos IPs, centenas de requisicoes cada"
    elif taxa > 30:
        veredito = "pico legitimo: muitos IPs, poucas requisicoes cada"
    else:
        veredito = "normal"
    print(f"{nome:<16} {taxa:7.1f} req/s  {ips:>4} IPs  media {media:6.1f} req/IP  -> {veredito}")
