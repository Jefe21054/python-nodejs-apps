import os, time
from tabulate import tabulate
import requests

def iniciar():
    os.system('clear')
    while True:
        print('Seleccione una de las opciones: ')
        print('\t1. Registrar movimiento')
        print('\t2. Ver todos los movimientos')
        print('\t3. Buscar un movimiento')
        print('\t4. Modificar un movimiento')
        print('\t5. Eliminar un movimiento')
        print('\t6. Salir de la aplicacion')
        opcion = input('Escoja una opcion: ')

        match opcion:
            case '1':
                nuevo_movimiento()
            case '2':
                ver_movimientos()
            case '3':
                buscar_movimiento()
            case '4':
                pass
                #modificar_movimiento()
            case '5':
                pass
                #eliminar_movimiento()
            case '6':
                break
            case _:
                os.system('clear')
                print('Elija una opcion de entre las mostradas por favor\n')
                time.sleep(3)
                iniciar()

def nuevo_movimiento():
    tipo = input('Ingrese el tipo de movimiento: \n- Ingreso\n- Gasto\n')
    cantidad = input('Ingrese la cantidad: ')
    fecha = input('Ingrese la fecha: ')
    datos = {
        'tipo':tipo,
        'cantidad':cantidad,
        'fecha':fecha,
    }
    respuesta = requests.post(url='http://localhost:3000/movimientos/registrar',data=datos)
    print(respuesta.text)

def ver_movimientos():
    response = requests.get(url='http://localhost:3000/movimientos/todos')
    datos = []
    for dato in response.json():
        temp = []
        for key, value in dato.items():
            temp.append(value)
        datos.append(temp)
    headers = ['ID','TIPO DE MOVIMIENTO','CANTIDAD','FECHA']
    tabla = tabulate(datos,headers,tablefmt='fancy_grid')
    print(tabla)

def buscar_movimiento():
    id = input('Ingrese el id del movimiento a buscar: ')
    response = requests.get(url='http://localhost:3000/movimientos/todos/'+id)
    datos = []
    for dato in response.json():
        temp = []
        for key, value in dato.items():
            temp.append(value)
        datos.append(temp)
    headers = ['ID', 'TIPO DE MOVIMIENTO', 'CANTIDAD', 'FECHA']
    tabla = tabulate(datos, headers, tablefmt='fancy_grid')
    print(tabla)


try:
    iniciar()
except KeyboardInterrupt:
    os.system('clear')
    print('Programa terminado por el usuario')