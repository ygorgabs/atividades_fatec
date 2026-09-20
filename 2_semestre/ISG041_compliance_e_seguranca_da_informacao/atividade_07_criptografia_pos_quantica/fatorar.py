import time

def fatorar(numero):
    i = 3
    while i * i <= numero:
        if numero % i == 0:
            return i, numero
        i += 2

for n in (2053273751, 705130309843, 182107122594619):
    t = time.perf_counter()
    fatores = fatorar(n)
    dt = time.perf_counter() - t
    bits = n.bit_length()
    print(f"Numero {n} Bits: {bits} Fatores: {fatores} Tempo: {dt: .3f}s")
    print("-"*40)