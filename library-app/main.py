import os, time
from tabulate import tabulate
from conexion import *
from libro import *
con = conectar()

def iniciar():
    os.system('clear')
    while True:
        print('Seleccione una de las opciones: ')
        print('\t1. Agregar un libro')
        print('\t2. Ver todos los libros')
        print('\t3. Buscar un libro')
        print('\t4. Modificar un libro')
        print('\t5. Eliminar un libro')
        print('\t6. Salir de la aplicacion')
        opcion = input('Escoja una opcion: ')

        match opcion:
            case '1':
                nuevo_libro()
            case '2':
                ver_libros()
            case '3':
                buscar_libro()
            case '4':
                pass
                #modificar_libro()
            case '5':
                pass
                #eliminar_libro()
            case '6':
                break
            case _:
                os.system('clear')
                print('Elija una opcion de entre las mostradas por favor\n')
                time.sleep(3)
                iniciar()

def nuevo_libro():
    titulo = input('Ingrese el titulo del libro: ')
    autor = input('Ingrese el autor del libro: ')
    estado = 'Disponible'
    respuesta = registrar(titulo, autor, estado)
    print(respuesta)

def ver_libros():
    datos = mostrar()
    headers = ['ID','TITULO','AUTOR','ESTADO',]
    tabla = tabulate(datos,headers,tablefmt='fancy_grid')
    print(tabla)

def buscar_libro():
    id = input('Ingrese el id del libro: ')
    datos = buscar(id)
    headers = ['ID','TITULO','AUTOR','ESTADO',]
    tabla = tabulate(datos,headers,tablefmt='fancy_grid')
    print(tabla)

try:
    iniciar()
except KeyboardInterrupt:
    os.system('clear')
    print('Programa terminado por el usuario')
