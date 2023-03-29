import os, time
from tabulate import tabulate
from conexion import *
from contacto import *

con =conectar()
crear_tabla(con)

def iniciar():
    os.system('clear')
    print('Seleccione una opcion:')
    print('\t1. Agregar un contacto')
    print('\t2. Mostrar todos los contactos')
    print('\t3. Buscar un contacto')
    print('\t4. Modificar un contacto')
    print('\t5. Eliminar un contacto')
    print('\t6. Salir de la aplicacion')
    opcion = input('Escoja una opcion: ')

    match opcion:
        case '1':
            nuevo_contacto()
        case '2':
            ver_contactos()
        case '3':
            buscar_contacto()
        case '4':
            pass
        case '5':
            pass
        case '6':
            pass
        case _:
            os.system('clear')
            print('Elija una opcion de entre las mostradas por favor\n')
            time.sleep(3)
            iniciar()

def nuevo_contacto():
    nombre = input('Ingrese el nombre: ')
    apellidos = input('Ingrese el apellido: ')
    empresa = input('Ingrese la empresa: ')
    telefono = input('Ingrese el telefono: ')
    email = input('Ingrese el email: ')
    direccion = input('Ingrese la direccion: ')
    respuesta = registrar(nombre, apellidos, empresa, telefono, email, direccion)
    print(respuesta)

def ver_contactos():
    datos = mostrar()
    headers = ['ID','NOMBRE','APELLIDO','EMPRESA','TELEFONO','EMAIL','DIRECCION']
    tabla = tabulate(datos,headers,tablefmt='fancy_grid')
    print(tabla)

def buscar_contacto():
    name = input('Ingrese el nombre del contacto a buscar: ')
    datos = buscar(str(name))
    headers = ['ID','NOMBRE','APELLIDO','EMPRESA','TELEFONO','EMAIL','DIRECCION']
    tabla = tabulate(datos,headers,tablefmt='fancy_grid')
    if datos == []:
        print('El contacto no ha sido registrado dentro de su agenda')
    else:
        print(tabla)

try:
    iniciar()
except KeyboardInterrupt:
    os.system('clear')
    print('Programa terminado por el usuario')
