#como leer un archivo
nombre_archivo="rata.txt"
with open(nombre_archivo, "r",encoding="utf-8") as archivo:
    contenido=archivo.read
    print("el contenido es:", contenido)