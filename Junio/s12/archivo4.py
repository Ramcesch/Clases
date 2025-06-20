arch1=open("rata.txt", "r")
lineas=arch1.readlines()
print("el  archivo tiene", len(lineas),"lineas")
print("el contenido del archivo")
for linea in lineas:
    print(linea,end="")
arch1.close()