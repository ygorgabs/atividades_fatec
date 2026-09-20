import hashlib

def newFile(path, content):
    with open(path, "w", encoding="utf-8") as file:
        file.write(content)

def hashFile(path):
    h = hashlib.sha256()
    with open(path, "rb") as file:
        for block in iter(lambda: file.read(65536),"".encode()):
            h.update(block)
    return h.hexdigest()

originalPath = "original.txt"
copyPath = "copia.txt"

newFile(originalPath,"Edital de matricula\nInscricoes ate 30/09")
newFile(copyPath,"Edital de matricula\nInscricoes ate 31/09")

originalHash = hashFile(originalPath)
print (originalHash)

for name in (originalPath, copyPath):
    print(name,"->","INTEGRO" if hashFile(name) == originalHash else "CORROMPIDO")