 cifrado = "H ZLNBYHUJH KLWLUKL KH JOHCL L UHV KV HSNVYPATV"
 decifrado = ""
 chave = 7
 for item in cifrado:
     if(item != " "):
         numAscii = ord(item)
         if numAscii - chave < 65 :
             decifrado += chr(numAscii - chave + 26)
         else:
             decifrado += chr(numAscii - chave)
     else:
         decifrado += " "

 print(decifrado)

