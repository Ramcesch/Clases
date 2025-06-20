# Programa que lee y muestra el contenido del archivo ASCII

archivo = open("ascii.txt", "r", encoding="utf-8")
print("Contenido del archivo ASCII:")
for linea in archivo:
    print(linea, end="")  # evitamos doble salto de línea
archivo.close()

