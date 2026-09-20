cifrado = "HOFTNNAGGG"
chave = "FATEC"
chave_extendida = ""
decifrado = ""

if len(chave) < len(cifrado):
    cont = 0
    for item in cifrado:

        if item != " ":
            chave_extendida += chave[cont]
            cont += 1
        else:
            chave_extendida += " "

        if cont >= len(chave):
            cont = 0

contador = 0
for item in cifrado:

    num_c = ord(item) - 65
    num_k = ord(chave_extendida[contador]) - 65

    if item != " ":
       num_d = (num_c - num_k) % 26
       decifrado += chr(num_d + 65)

       contador += 1

    else:
        decifrado += " "

print(decifrado)
