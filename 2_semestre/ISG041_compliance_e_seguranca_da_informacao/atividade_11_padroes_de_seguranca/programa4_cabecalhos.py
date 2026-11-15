# Aula 11 - Programa 4: verificador de configuracao da resposta HTTP (A05)
# Proposito: conferir cabecalhos de seguranca e flags de cookie, como faz a primeira verificacao de um scanner DAST.
resposta = {                                   # cabecalhos devolvidos pelo servidor
    "Content-Type":    "text/html; charset=utf-8",
    "Server":          "Apache/2.4.29 (Ubuntu)",
    "Set-Cookie":      "sessao=abc123; Path=/; Secure; HttpOnly; SameSite=Lax",
    "X-Frame-Options": "DENY",
    "Strict-Transport-Security": "max-age=31536000",
}

ESPERADOS = {
    "Strict-Transport-Security": "obriga HTTPS nas proximas visitas",
    "Content-Security-Policy":   "limita de onde scripts podem vir (reduz XSS)",
    "X-Content-Type-Options":    "impede o navegador de adivinhar o tipo do conteudo",
    "X-Frame-Options":           "impede que a pagina seja embutida em outro site",
}
for cabecalho, motivo in ESPERADOS.items():
    estado = "ok    " if cabecalho in resposta else "FALTA "
    print(f"{estado} {cabecalho:<28} {motivo}")

cookie = resposta.get("Set-Cookie", "").lower()
for flag, motivo in (("Secure",   "so trafega por HTTPS"),
                     ("HttpOnly", "script da pagina nao consegue ler o cookie"),
                     ("SameSite", "nao e enviado em requisicoes vindas de outros sites")):
    estado = "ok    " if flag.lower() in cookie else "FALTA "
    print(f"{estado} cookie {flag:<21} {motivo}")

if "Server" in resposta:
    print(f"AVISO  cabecalho Server revela a versao: {resposta['Server']}")
