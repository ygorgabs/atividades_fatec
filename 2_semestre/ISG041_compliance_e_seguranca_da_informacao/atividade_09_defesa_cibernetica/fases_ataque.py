FASES = {                                
    "falhas de login":"4 Exploracao",
    "login OK":"4 Exploracao",
    "tarefa agendada":"5 Instalacao",
    "conexao":"6 Comando e controle",
    "comando":"7 Acoes nos objetivos",
}

eventos = [
    "02:10 cinco falhas de login a partir de 198.51.100.23",
    "02:14 login OK usuario=scada a partir de 198.51.100.23",
    "02:20 tarefa agendada criada: 'manutencao.bat'",
    "02:25 conexao periodica para 192.0.2.77:8443",
    "03:05 comando de parada enviado a bomba B2"
]

for ev in eventos:
    fase = next((f for pista, f in FASES.items() if pista in ev), "? não classificado")
    print(f"{fase:<24} {ev}")