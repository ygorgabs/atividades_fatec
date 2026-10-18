# Aula 10 - Programa 2: janela de exposicao de cada vulnerabilidade
# Proposito: medir a janela de exposicao e a janela de risco real. Pergunta: por quanto tempo cada falha ficou aberta?
from datetime import date

correcoes = [
    # sistema,            divulgacao publica, exploracao conhecida, correcao aplicada
    ("servidor de e-mail", date(2026, 3, 14), date(2026, 3, 20),    date(2026, 3, 16)),
    ("VPN",                date(2026, 1, 9),  date(2026, 1, 12),    date(2026, 4, 2)),
    ("estacoes Windows",   date(2026, 5, 13), None,                 date(2026, 5, 27)),
    ("CMS do site",        date(2025, 11, 2), date(2025, 12, 1),    date(2026,5,20)),
]
hoje = date(2026, 6, 1)

for sistema, divulgacao, exploracao, correcao in correcoes:
    fim = correcao or hoje                                  # se nao corrigiu, conta ate hoje
    janela = (fim - divulgacao).days
    situacao = "corrigido" if correcao else "AINDA EXPOSTO"
    if exploracao and exploracao < fim:                     # houve exploracao antes de corrigir?
        risco = f"exploracao publica desde {exploracao}: {(fim - exploracao).days} dias em risco real"
    else:
        risco = "corrigido antes de exploracao conhecida"
    print(f"{sistema:<19} janela {janela:>3} dias  {situacao:<14} {risco}")
