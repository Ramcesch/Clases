archivo= "estudiantes.txt"
clave='admin123'

def inicio():
    print("INICIO DE SESION")
    intento=input("ingresa la contraseña")
    if intento== clave:
        print("Acceso permitido\n")
        return True
    else:
        print("contraseña incorrecta. Acceso denegado")
        return False