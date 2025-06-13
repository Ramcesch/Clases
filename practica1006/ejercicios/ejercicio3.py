# Programa que añade texto a un archivo sin borrar el contenido

nombre_archivo = input("Ingrese el nombre del archivo: ")
archivo = open(nombre_archivo, "a", encoding="utf-8")
print("Escriba texto para agregar. Escriba 'SALIR' para terminar.")
while True:
    linea = input("Texto: ")
    if linea.upper() == "SALIR":
        break
    archivo.write(linea + "\n")
archivo.close()

print("Texto añadido correctamente.")
