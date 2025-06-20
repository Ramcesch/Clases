# Programa que lee el contenido de un archivo
nombre_archivo = input("Ingrese el nombre del archivo a leer: ")
archivo = open(nombre_archivo, "r", encoding="utf-8")
contenido = archivo.read()
print("Contenido del archivo:")
print(contenido)
archivo.close()
