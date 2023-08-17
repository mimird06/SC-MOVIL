import os
import sqlite3
import random

#Conexion a la base de datos.
coneccion = sqlite3.connect('scmovil.db')
cursor = coneccion.cursor()

def cls():
    os.system('cls')

class Sistema:
    
    def registrar(self):
        print("SC-MOVIL: Registro")

        #Peticion de datos
        nombre = input("Nombre del propetario: ")
        apellido = input("Apellido del propetario: ")
        cedula = int(input("Cedula del propetario: "))
        
        #Tipo de vehiculo
        vehiculo = input("Tipo de vehiculo: \n"
                        ">A. Carro\n"
                        ">L. Camion \n"
                        ">K. Motocicleta\n"
                        ">G. Jeepeta\n"
                        ">>>> ").lower()
        
        if vehiculo=="carro":
            letra_matricula = "A"
        elif vehiculo=="camion":
            letra_matricula = "L"
        elif  vehiculo=="motocicleta":
            letra_matricula = "K"
        elif vehiculo== "jeepeta":
            letra_matricula = "G"
        else:
            print("Hay un error")

        #Creacion de matricula aleatoria.
        numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

        for caracteres in range(6):
            cantidad_numeros = random.sample(numeros,6)

        #Matricula no limpia
        union = letra_matricula,cantidad_numeros

        #Union de la letra de la matrícula con los números usando ''.join() para eliminar las comas y espacios
        matricula = union[0] + ' ' + ''.join(union[1])

        #Peticion de mas datos
        color = input("Color del vehiculo: ")
        marca = input("Marca del vehiculo: ")

        #Guardar los cambios en la base de datos
        guardar = (matricula, marca, color, nombre, apellido, cedula )

        cursor.execute("INSERT INTO vehiculo (matricula, marca, color, nombre, apellido, cedula) VALUES (?,?,?,?,?,?)", guardar)
        coneccion.commit()
        print("Datos guardados correctamente")

        
    def buscar(self):
        print("SC-MOVIL: Buscar datos.")

        buscarCedula = input("Ingresa la cedula del propetario: ")

        datosCedula = cursor.execute(f"SELECT * FROM vehiculo WHERE cedula={buscarCedula}")
        datosPropetario = datosCedula.fetchone()
        print(datosPropetario)


    def actualizar(self):
        print("SC-MOVIL: Actualizar datos.")

        buscarCedula = input("Ingresa la cedula del propetario: ")

        datosCedula = cursor.execute(f"SELECT cedula FROM vehiculo WHERE cedula={buscarCedula}")
        datosPropetario = datosCedula.fetchone()
        buscarNombre = cursor.execute(f"SELECT nombre FROM vehiculo WHERE cedula={buscarCedula}")
        nombrePropetario = buscarNombre.fetchone()
        
        print(f"Bienvenido {nombrePropetario}, por favor ingresa: ")
        print("")
        datos = ''.join(map(str,datosPropetario))

        if buscarCedula in datos:
            
            vehiculo = input("Tipo de vehiculo: \n"
                        ">A. Carro\n"
                        ">L. Camion \n"
                        ">K. Motocicleta\n"
                        ">G. Jeepeta\n"
                        ">>>> ").lower()
        
            if vehiculo=="carro":
                letra_matricula = "A"
            elif vehiculo=="camion":
                letra_matricula = "L"
            elif  vehiculo=="motocicleta":
                letra_matricula = "K"
            elif vehiculo== "jeepeta":
                letra_matricula = "G"
            else:
                print("Hay un error")

            #Creacion de matricula aleatoria.
            numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

            for caracteres in range(6):
                cantidad_numeros = random.sample(numeros,6)

            #Matricula no limpia
            union = letra_matricula,cantidad_numeros

            #Union de la letra de la matrícula con los números usando ''.join() para eliminar las comas y espacios
            matricula = union[0] + ' ' + ''.join(union[1])

            #Peticion de mas datos
            color = input("Color del vehiculo: ")
            marca = input("Marca del vehiculo: ")

            cursor.execute(f"UPDATE vehiculo SET matricula='{matricula}', marca='{marca}', color='{color}' WHERE cedula={buscarCedula}")
            coneccion.commit()

            traerActualizacion = cursor.execute(f"SELECT * FROM vehiculo WHERE cedula={buscarCedula}")
            mostrarModificacion = traerActualizacion.fetchone()
            print(mostrarModificacion)
        else:
            print("Ahora no es posible, se ha detectado un error.")


    def eliminar(self):
        print("SC-MOVIL: Eliminar datos.")

        buscarCedula = input("Ingresa la cedula del propetario: ")
        datosCedula = cursor.execute(f"SELECT * FROM vehiculo WHERE cedula={buscarCedula}")
        datosPropetario = datosCedula.fetchone()
        print(datosPropetario)

        eliminarDatos = input("¿Estas seguro/a de eliminar esos datos: ").lower()
        if eliminarDatos == "si":
            cursor.execute(f"DELETE FROM vehiculo WHERE cedula={buscarCedula}")
            print("Datos eliminados correctamente")
        elif eliminarDatos == "no":
            print("PROCESO CANCELADO...")
        else:
            print("Ha ocurrido un error, intentalo mas tarde.")

                

scMovil = Sistema()

while True:
    cls()
    print("Menu: \n"
          "Escoge:\n 1. Registrar\n 2. Buscar \n 3. Actualizar \n 4. Eliminar \n 5. Salir")
    
    opcion = int(input(">>> "))

    if opcion == 1:
        cls()
        scMovil.registrar()
        input(">>> ENTER: ")
    elif opcion == 2:
        cls()
        scMovil.buscar()
        input(">>> ENTER: ")
    elif opcion == 3:
        cls()
        scMovil.actualizar()
        input(">>> ENTER: ")
    elif opcion == 4:
        cls()
        scMovil.eliminar()
        input(">>> ENTER: ")
    elif opcion == 5:
        print("Gracias por escoger nuestro sistema.")
        break
    else:
        print("Intentalo mas tarde. ")