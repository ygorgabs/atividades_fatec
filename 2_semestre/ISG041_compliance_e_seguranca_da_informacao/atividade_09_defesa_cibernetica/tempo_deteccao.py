from datetime import datetime

incidentes = [
    ("acesso indevido ao SCADA","2026-08-14 02:14","2026-08-14 03:05","2026-08-14 03:40"),
    ("phishing na contabilidade","2026-09-01 09:30","2026-09-19 16:00","2026-09-19 18:30"),
    ("notebook com malware","2026-09-22 11:00","2026-09-22 11:05", "2026-09-22 13:00")
]

def horas(inicio, fim):
    f = "%Y-%m-%d %H:%M"
    return (datetime.strptime(fim,f) - datetime.strptime(inicio,f)).total_seconds() / 3600

for nome, invasao, deteccao, contencao in incidentes:
    print(f"{nome:<26} permanencia {horas(invasao, deteccao):6.1f}h resposta {horas(deteccao,contencao):4.1f}h")

media = sum(horas(i, d) for _,i,d,_ in incidentes)/len(incidentes)
print(f"\nTempo medio ate a deteccao: {media:.1f}h ({media/24:.1f} dias)")