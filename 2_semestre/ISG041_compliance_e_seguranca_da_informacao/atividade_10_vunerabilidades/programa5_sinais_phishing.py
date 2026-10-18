# Aula 10 - Programa 5: pontuar os sinais de phishing em mensagens recebidas
# Proposito: transformar os sinais de phishing em regras de filtro e expor seu limite (BEC). Pergunta: esta mensagem merece atencao?
DOMINIOS_CONFIAVEIS = {"mercadobompreco.com.br"}
PALAVRAS_DE_URGENCIA = ("urgente", "imediatamente", "ultimo aviso", "24 horas", "bloqueada", "suspensa")
EXTENSOES_DE_RISCO = (".exe", ".scr", ".js", ".bat", ".docm", ".zip")

mensagens = [
    {"remetente": "financeiro@mercadobompreco.com.br", "assunto": "Relatorio mensal",
     "texto": "segue o relatorio de outubro para conferencia",
     "links": [("portal interno", "https://portal.mercadobompreco.com.br")],
     "anexos": ["relatorio.pdf"], "pede_credencial": False},
    {"remetente": "seguranca@mercadobompreco-login.com", "assunto": "URGENTE: conta bloqueada",
     "texto": "sua conta sera suspensa em 24 horas, confirme sua senha imediatamente",
     "links": [("portal.mercadobompreco.com.br", "http://mercadobompreco-login.com/entrar")],
     "anexos": [], "pede_credencial": True},
    {"remetente": "rh@mercadobompreco.com.br", "assunto": "Holerite de outubro",
     "texto": "segue o holerite em anexo",
     "links": [], "anexos": ["holerite.zip"], "pede_credencial": False},
    {"remetente": "diretoria@mercadobompreco.com.br",
      "assunto": "Pagamento urgente",
      "texto": "transfira hoje para a nova conta do fornecedor",
      "links": [], "anexos": [], "pede_credencial": False},
]

def sinais(m):                                   # m: dicionario com os campos da mensagem
    encontrados = []
    if m["remetente"].split("@")[-1] not in DOMINIOS_CONFIAVEIS:
        encontrados.append("remetente fora dos dominios conhecidos")
    conteudo = (m["assunto"] + " " + m["texto"]).lower()
    if any(p in conteudo for p in PALAVRAS_DE_URGENCIA):
        encontrados.append("tom de urgencia ou ameaca")
    for texto, destino in m["links"]:
        if "." in texto and texto not in destino:   # texto parece um endereco, destino e outro
            encontrados.append(f"link mostra '{texto}' mas leva a outro dominio")
    for anexo in m["anexos"]:
        if anexo.lower().endswith(EXTENSOES_DE_RISCO):
            encontrados.append(f"anexo de risco: {anexo}")
    if m["pede_credencial"]:
        encontrados.append("pede senha ou dados de acesso")
    return encontrados

for m in mensagens:
    s = sinais(m)
    nivel = "ALTO RISCO" if len(s) >= 3 else ("ATENCAO" if s else "sem sinais")
    print(f"[{nivel}] {m['assunto']} (de {m['remetente']})", *s, sep="\n   - ")
