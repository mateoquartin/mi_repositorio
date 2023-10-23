import re
def ingresar_usuario(base_datos):
    usuario = input("Ingresar usuario a registrar: ")
    while True:
        print("La contraseña debe cumplir con los siguientes requisitos\n°Tener al menos 8 caracteres \n°Tener al menos un caracter especial \n°Tener una mayuscula ")
        contraseña = input("Ingresar una contraseña: ")
        contraseña2 = input("Repetir contraseña: ")
        if len(contraseña) < 8:
            print("la contraseña debe tener 8 caracteres o mas!")
        else:
            if any(c.isdigit() for c in contraseña):
                if any(c.isupper() for c in contraseña):
                    if re.search(r'[!@#$%^&*()_+{}\[\]:;<>,.?~\\\-]', contraseña):
                        if contraseña == contraseña2:
                            base_datos.update({usuario: contraseña})
                            return base_datos
                        else:
                            print("Las contraseñaseñas no coinciden!")
                    else: 
                        print("Debe tener un caracter especial!")
                else:
                    print("La contraseña debe tener una letra mayuscula por lo menos")
            else:
                print("La contraseña debe tener un numer!")

def leer_datos(base_datos):
    if len(base_datos) > 0:
        print("la informacion de los usuarios registrados en la base de datos es: ")
        for clave in base_datos: 
            valor = base_datos[clave]
            print(f'Nombre del usuario: {clave} contraseña: {valor}')
    else:
        print("No hay usuarios registrados aun!")

def logear(base_datos):
    while True: # creo un bucle true para que si no se encuentran los datos ingresados los vuelva a pedir 
        usuario = input("Ingresar usuario: ")
        contraseña = input("Ingresar contraseña: ")
        if usuario in base_datos and base_datos[usuario] == contraseña: #comprobamos que el usuario(clave) y contraseña(valor) ingresados coincidan con alguno ya en la base
            print("Has iniciado sesión correctamente!")
            break  # Sale del bucle si las credenciales son correctas
        else:
            print("Usuario o contraseña incorrecta. Por favor, inténtalo de nuevo.")


base_datos = {} #creamos diccionario para trabajar la base de datos de los usuarios en las funciones
while True: #menu de interaccion
    print("-----BIENVENIDO-----")
    print("1) Registrarse en la pagina")
    print("2) Ver usuarios registrados")
    print("3) Ingresar con usuario y contraseña")
    print("0) Salir")
    opcion = int(input("Ingresar la opcion a realizar: "))
    if opcion == 1:
        ingresar_usuario(base_datos)
    if opcion == 2:
        leer_datos(base_datos)
    if opcion == 3:
        logear(base_datos)
    if opcion == 0:
        break
    else:
        print("Opcion incorrecta, Ingrese una detallada en el menu!")     
