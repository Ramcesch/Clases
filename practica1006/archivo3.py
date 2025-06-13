#lectura de un archivo de texto
arch1=open("rata.txt","r")
linea=arch1.readline()
while linea!="":
    print(linea, end="")
    linea=arch1.readline()
arch1.close()    