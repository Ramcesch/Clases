# Programa que escribe los caracteres ASCII del 32 al 126

archivo = open("ascii.txt", "w", encoding="utf-8")
for i in range(32, 127):
    archivo.write(f"{i}: {chr(i)}\n")
archivo.close()

print("Archivo 'ascii.txt' creado con la lista de caracteres ASCII.")
