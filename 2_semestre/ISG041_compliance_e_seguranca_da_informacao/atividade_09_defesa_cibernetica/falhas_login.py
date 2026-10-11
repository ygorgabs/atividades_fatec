from collections import Counter

log = """
02:10:05 FALHA usuario=operador ip=198.51.100.23
02:10:06 FALHA usuario=operador ip=198.51.100.23
02:10:06 FALHA usuario=admin    ip=198.51.100.23
02:10:07 FALHA usuario=scada    ip=198.51.100.23
02:10:08 FALHA usuario=root     ip=198.51.100.23
07:58:40 FALHA usuario=marcia   ip=10.1.0.12
07:58:52 OK    usuario=marcia   ip=10.1.0.12
08:15:01 OK    usuario=joao     ip=10.1.0.30
12:40:10 FALHA usuario=joao     ip=10.1.0.30
12:40:30 OK    usuario=joao     ip=10.1.0.30
"""

falhas = Counter()

for linha in log.strip().splitlines():
    if "FALHA" in linha:
        ip = linha.split("ip=")[1].strip()
        falhas[ip] += 1

for ip, n in falhas.most_common():
    alerta = " <- ALERTA" if n >= 5 else ""
    print(f"{ip:<14} {n:>2} falhas{alerta}")