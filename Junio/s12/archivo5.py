#añadir lineas
arch1=open("rata.txt", "a")
arch1.write("nueva linea 1\n")
arch1.write("nueva linea 2\n")
arch1.close()
arch1=open('rata.txt',"r")
contenido=arch1.read()
print(contenido)
arch1.close()
