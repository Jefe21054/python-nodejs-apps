import os
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
                pass
                #ver_movimientos()
            case '3':
                pass
                #buscar_movimiento()
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

try:
    iniciar()
except KeyboardInterrupt:
    os.system('clear')
    print('Programa terminado por el usuario')