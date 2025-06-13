#solicitar datos al usuario
nombre=input("ingresa tu nombre: ")
apellido=input("ingresa tu apellido: ")
edad=input("ingresa tu edad")
salario=input("ingresa tu salario:")

#formatear los datos de una linea
linea=f"{nombre},{apellido},{edad},{salario}\n"

#guardar los datos de un archivo
with open("datos de usuario.txt", "a") as archivo:
    archivo.write(linea)

print("datos guardados correctamente en 'datos_usuario.txt'.")