# Aula 11 - Programa 7: validar o destino de uma requisicao feita pelo servidor (A10, SSRF)
# Proposito: so permitir que o servidor acesse hosts de uma lista, por HTTPS, nunca enderecos internos.
import ipaddress
from urllib.parse import urlparse

HOSTS_PERMITIDOS = {"api.correios.com.br", "cep.exemplo.com.br"}

def destino_permitido(url):
    u = urlparse(url)
    if u.scheme != "https":
        return False, "esquema nao permitido"
    host = u.hostname or ""
    try:
        ip = ipaddress.ip_address(host)              # e um IP literal?
        if ip.is_private or ip.is_loopback or ip.is_link_local:
            return False, "endereco interno"
        return False, "IP literal nao permitido"
    except ValueError:
        pass                                         # e um nome de host
    if host not in HOSTS_PERMITIDOS:
        return False, "host fora da lista"
    return True, "ok"

for url in ["https://api.correios.com.br/cep/01310-100",
            "http://api.correios.com.br/cep/01310-100",
            "https://10.0.0.5/",
            "https://127.0.0.1/",
            "https://outro-site.exemplo/",
            "https://api.correios.com.br.outro.exemplo/"]:
    ok, motivo = destino_permitido(url)
    print(f"{'PERMITE ' if ok else 'BLOQUEIA'}  {url:<42} {motivo}")
