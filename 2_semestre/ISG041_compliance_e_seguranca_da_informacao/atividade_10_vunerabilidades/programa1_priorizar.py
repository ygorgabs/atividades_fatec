# Aula 10 - Programa 1: priorizar vulnerabilidades
# Proposito: mostrar que gravidade (CVSS) nao e risco. Pergunta: qual falha corrigir primeiro?
vulnerabilidades = [
    # descricao,                                 cvss, exposto na internet, criticidade do ativo (1 a 3)
    ("Servidor web: versao antiga do Apache",     7.5, True,  3),
    ("Banco de dados: senha padrao do admin",     9.8, False, 3),
    ("Estacao do RH: Office sem correcoes",       7.8, False, 2),
    ("Impressora: painel web sem senha",          5.3, False, 1),
    ("VPN: falha com exploracao publica",         9.1, False,  3),
    ("Site institucional: CMS desatualizado",     6.1, True,  1),
]

def prioridade(cvss, exposto, criticidade):
    fator_exposicao = 2.0 if exposto else 1.0      # exposto na internet pesa o dobro
    return cvss * fator_exposicao * criticidade

ordenadas = sorted(vulnerabilidades, key=lambda v: prioridade(*v[1:]), reverse=True)
for nome, cvss, exposto, crit in ordenadas:
    p = prioridade(cvss, exposto, crit)
    onde = "internet" if exposto else "interna "
    print(f"{p:5.1f}  cvss={cvss}  {onde}  ativo={crit}  {nome}")
