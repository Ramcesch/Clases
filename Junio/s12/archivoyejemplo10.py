#abrir el archivo en modo creacion
#ejemplo, solicitando el nombre del archivo usuario
ruta=input("nombre del archivo:")
arch1=open(ruta,"a")
arch1.write("primera linea\n")
arch1.write("segunda linea\n")
arch1.write("tercera linea\n")
arch1.close()
print("fin del programa")