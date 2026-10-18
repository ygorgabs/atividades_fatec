# Aula 10 - Programa 3: detectar propagacao de worm na rede interna
# Proposito: reconhecer a assinatura de rede de um worm (muitos destinos, mesma porta). Pergunta: ha um worm se espalhando?
from collections import defaultdict

# (origem, destino, porta) das conexoes internas registradas em 1 minuto
conexoes = [("10.0.0.7", f"10.0.0.{i}", 445) for i in range(20, 50)]     # 10.0.0.7 fala com 30 maquinas
conexoes += [("10.0.0.3", "10.0.0.50", 3389), ("10.0.0.3", "10.0.0.50", 3389),
             ("10.0.0.4", "10.0.0.50", 445), ("10.0.0.4", "10.0.0.50", 445),
             ("10.0.0.4", "10.0.0.51", 445)]

destinos = defaultdict(set)
for origem, destino, porta in conexoes:
    destinos[(origem, porta)].add(destino)          # quantas maquinas diferentes cada origem procurou

for (origem, porta), alvos in sorted(destinos.items(), key=lambda x: -len(x[1])):
    tipo = "PROPAGACAO: possivel worm" if len(alvos) >= 2 else "normal"
    print(f"{origem:<10} porta {porta:<5} {len(alvos):>2} destinos distintos  -> {tipo}")
