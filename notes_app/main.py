import os,time
from tabulate import tabulate
from conexion import *
from nota import Nota
con = conectar()

def iniciar():
    os.system('clear')
    while True:
        print('Seleccione una de las opciones: ')
        print('\t1. Nueva nota')
        print('\t2. Ver notas')
        print('\t3. Ver contenido')
        print('\t4. Modificar nota')
        print('\t5. Eliminar nota')
        print('\t6. Salir de la aplicacion')
        opcion = input('Escoja una opcion: ')

        match opcion:
            case '1':
                nueva_nota()
            case '2':
                ver_notas()
            case '3':
                ver_contenido()
            case '4':
                modificar_contenido()
            case '5':
                eliminar_nota()
            case '6':
                break
            case _:
                os.system('clear')
                print('Elija una opcion de entre las mostradas por favor\n')
                time.sleep(3)
                iniciar()

def nueva_nota():
    nombre = input('Ingrese el nombre de la nota: ')
    contenido = input('Ingrese el contenido de la nota:\n')
    nota = Nota(nombre=nombre,contenido=contenido)
    respuesta = nota.registrar()
    print(respuesta)

def ver_notas():
    nota = Nota()
    datos = nota.mostrar()
    headers = ['ID','NOMBRE DEL ARCHIVO','FECHA DE CREACION']
    tabla = tabulate(datos,headers,tablefmt='fancy_grid')
    print(tabla)

def ver_contenido():
    id = input('Ingrese el id de la nota: ')
    nota = Nota(id=id)
    resultado = nota.buscar()
    if len(resultado):
        file = open(f'./notas/{resultado[0][1]}','r')
        print('\n'+file.read()+'\n')
        file.close()
    else:
        print('No se encontro el archivo')

def modificar_contenido():
    archivos = os.listdir('./notas')
    for numero, archivo in enumerate(archivos):
        print(f'{numero+1} {archivo}' )
    seleccionado = input('Escoja el archivo a modificar: ')
    nuevo_contenido = input('\nIngrese el nuevo contenido:\n')
    file = open(f'./notas/{archivos[int(seleccionado)-1]}', 'w')
    file.write(nuevo_contenido)
    file.close()
    print('Archivo modificado')

def eliminar_nota():
    id = input('Ingrese el id de la nota a eliminar: ')
    nota = Nota(id=id)
    resultado = nota.eliminar()
    print(resultado)

try:
    iniciar()
except KeyboardInterrupt:
    os.system('clear')
    print('Programa terminado por el usuario')