# Aula 11 - Programa 2: dados sao dados, codigo e codigo (A03, injecao)
# Proposito: mostrar por que concatenar a entrada no comando SQL e errado e como a consulta parametrizada resolve.
import sqlite3

db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE clientes (nome TEXT, cidade TEXT)")
db.executemany("INSERT INTO clientes VALUES (?, ?)",
               [("Ana Lima", "Sao Paulo"), ("Conor O'Brien", "Dublin"), ("Bruno Reis", "Recife")])

busca = "O'Brien"                                   # entrada do usuario, com apostrofo

# jeito ERRADO: a entrada vira parte do texto do comando
sql = "SELECT nome, cidade FROM clientes WHERE nome LIKE '%" + busca + "%'"
print("comando montado:", sql)
try:
    print("resultado      :", db.execute(sql).fetchall())
except sqlite3.OperationalError as erro:
    print("ERRO de sintaxe SQL:", erro)

# jeito CERTO: a entrada e enviada separada, como dado, no lugar do ?
sql = "SELECT nome, cidade FROM clientes WHERE nome LIKE ?"
print("parametrizada  :", db.execute(sql, ("%" + busca + "%",)).fetchall())
