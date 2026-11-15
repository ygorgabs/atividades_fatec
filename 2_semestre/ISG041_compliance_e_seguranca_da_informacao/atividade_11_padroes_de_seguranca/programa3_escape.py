# Aula 11 - Programa 3: escape de saida (A03, XSS)
# Proposito: mostrar que texto do usuario inserido em HTML sem escape vira parte da pagina, e como html.escape evita isso.
import html

comentarios = ["Produto otimo, recomendo!",
               "Achei <b>caro</b> demais",
               'Veja minha loja: <a href="http://outro-site.exemplo">aqui</a>',
               "Nota: 5 > 4"]

def pagina_insegura(c):
    return f"<p>{c}</p>"                      # o texto entra como esta

def pagina_segura(c):
    return f"<p>{html.escape(c)}</p>"         # < > & " viram entidades

for c in comentarios:
    print("insegura:", pagina_insegura(c))
    print("segura  :", pagina_segura(c))
    print()
