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
                modificar_libro()
            case '5':
                pass
                eliminar_libro()
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

def modificar_libro():
    id = input('Ingrese el id del libro a modificar: ')
    nuevoValor = ''
    respuesta = ''
    campo = input('Seleccione el campo que desea modificar\n1. Titulo\n2. Autor\n3. Estado\n')
    if campo == '1':
        nuevoValor = input('Ingrese el nuevo titulo del libro: ')
    elif campo == '2':
        nuevoValor = input('Ingrese el nuevo autor del libro: ')
    elif campo == '3':
        nuevoValor = input('Ingrese el nuevo estado del libro: ')
    else:
        print('El campo elegido no existe')
    respuesta = modificar(id, campo, nuevoValor)
    print(respuesta)

def eliminar_libro():
    id = input('Ingrese el id del libro a eliminar: ')
    respuesta = eliminar(id)
    print(respuesta)

try:
    iniciar()
except KeyboardInterrupt:
    os.system('clear')
    print('Programa terminado por el usuario')
