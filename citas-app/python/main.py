import os, time
import requests
from tabulate import tabulate
from datetime import date

def iniciar():
    os.system('clear')
    while True:
        print('Seleccione una opcion:')
        print('\t1. Registrar una cita médica')
        print('\t2. Ver todas las citas médicas')
        print('\t3. Ver citas médicas de hoy')
        print('\t4. Modificar estado de cita médica')
        print('\t5. Eliminar una cita médica')
        print('\t6. Salir de la aplicación')
        opcion = input('Escoja una opción: ')

        match opcion:
            case '1':
                nueva_cita()
            case '2':
                mostrar_citas()
            case '3':
                buscar_citas()
            case '4':
                modificar_estado()
            case '5':
                eliminar_cita()
            case '6':
                break
            case _:
                os.system('clear')
                print('Elija una opcion de entre las mostradas por favor\n')
                time.sleep(3)
                iniciar()

def nueva_cita():
    paciente = input('Ingrese el nombre del paciente: ')
    detalle = input('Ingrese el detalle de la cita: ')
    dia = input('Ingrese el día de la cita: ')
    hora = input('Ingrese la hora de la cita: ')
    data = {
        'paciente':paciente, 
        'detalle': detalle, 
        'dia':dia, 
        'hora':hora, 
        'estado':'Agendada'
    }
    respuesta = requests.post(url='http://localhost:3000/citas-medicas/registrar', data=data)
    print(respuesta.text)

def mostrar_citas():
    respuesta = requests.get(url='http://localhost:3000/citas-medicas/todas')
    datos = []
    for dato in respuesta.json():
        temp = []
        for key, value in dato.items():
            temp.append(value)
        datos.append(temp)
    headers = ['ID', 'PACIENTE', 'DETALLE', 'DÍA', 'HORA', 'ESTADO']
    tabla = tabulate(datos, headers, tablefmt='fancy_grid')
    print(tabla)

def buscar_citas():
    dia = date.today()
    respuesta = requests.get(url='http://localhost:3000/citas-medicas/buscar', data={'dia':dia})
    datos = []
    for dato in respuesta.json():
        temp = []
        for key, value in dato.items():
            temp.append(value)
        datos.append(temp)
    headers = ['ID', 'PACIENTE', 'DETALLE', 'DÍA', 'HORA', 'ESTADO']
    tabla = tabulate(datos, headers, tablefmt='fancy_grid')
    print(tabla)

def modificar_estado():
    id = input('Ingrese el id de la cita médica: ')
    estado = input('Ingrese el estado:\n- Agendada\n- Atendida\n')
    respuesta = requests.post(url='http://localhost:3000/citas-medicas/modificar/'+id, data={'estado':estado})
    print(respuesta.text)

def eliminar_cita():
    id = input('Ingrese el id de la cita médica: ')
    respuesta = requests.post(url='http://localhost:3000/citas-medicas/eliminar/'+id)
    print(respuesta.text)

try:
    iniciar()
except KeyboardInterrupt:
    os.system('clear')
    print('Programa terminado por el usuario')
