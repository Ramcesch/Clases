#ejeccutando archivos de texto en python
#creando el archivo
arch1=open("rata.txt","a") #"w" modo escritura

arch1.write("Primera linea \n")
arch1.write("segunda linea \n")
arch1.write("tercera linea \n")
arch1.write("fin del archivo \n")
arch1.close()
print("Fin del programa")