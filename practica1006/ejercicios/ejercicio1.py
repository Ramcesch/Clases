# Programa que guarda frases en un archivo

nombre_archivo = input("Ingrese el nombre del archivo (ej: frases.txt): ")
archivo = open(nombre_archivo, "w", encoding="utf-8")
print("Escriba frases. Para terminar, escriba 'SALIR'.")
while True:
    frase = input("Frase: ")
    if frase.upper() == "SALIR":
        break
    archivo.write(frase + "\n")
archivo.close()
print("Frases guardadas correctamente.")
