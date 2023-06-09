import os, time
from tabulate import tabulate
import requests

def iniciar():
    os.system('clear')
    while True:
        print('Seleccione una de las opciones: ')
        print('\t1. Registrar producto')
        print('\t2. Ver todos los productos')
        print('\t3. Buscar un producto')
        print('\t4. Modificar un producto')
        print('\t5. Eliminar un producto')
        print('\t6. Nueva venta')
        print('\t7. Salir de la aplicacion')
        opcion = input('Escoja una opcion: ')

        match opcion:
            case '1':
                nuevo_producto()
            case '2':
                ver_productos()
            case '3':
                buscar_producto()
            case '4':
                modificar_producto()
            case '5':
                eliminar_producto()
            case '6':
                nueva_venta()
            case '7':
                break
            case _:
                os.system('clear')
                print('Elija una opcion de entre las mostradas por favor\n')
                time.sleep(3)
                iniciar()

def nuevo_producto():
    nombre = input('Ingrese el nombre del producto: ')
    descripcion = input('Ingrese la descripcion del producto: ')
    precio = input('Ingrese el precio del producto: ')
    datos = {
        'nombre':nombre,
        'descripcion':descripcion,
        'precio':precio,
    }
    respuesta = requests.post(url='http://localhost:3000/productos/registrar',data=datos)
    print(respuesta.text)

def ver_productos():
    respuesta = requests.get(url='http://localhost:3000/productos/todos')
    datos = []
    for dato in respuesta.json():
        temp = []
        for key,value in dato.items():
            temp.append(value)
        datos.append(temp)
    headers = ['ID','NOMBRE','DESCRIPCION','PRECIO']
    tabla = tabulate(datos,headers,tablefmt='fancy_grid')
    print(tabla)

def buscar_producto():
    id = input('Ingrese el id del producto a buscar: ')
    respuesta = requests.get(url='http://localhost:3000/productos/buscar/'+id)
    datos = []
    for dato in respuesta.json():
        temp = []
        for key,value in dato.items():
            temp.append(value)
        datos.append(temp)
    headers = ['ID','NOMBRE','DESCRIPCION','PRECIO']
    tabla = tabulate(datos,headers,tablefmt='fancy_grid')
    print(tabla)

def modificar_producto():
    id = input('Ingrese el id del producto a modificar: ')
    campo = input('Seleccione el campo a modificar:\n1. Nombre\n2. Descripcion\n3. Precio\n')
    if ((campo == '1') or (campo == '2') or (campo == '3')):
        nuevo_valor = input('Ingrese el nuevo valor: ')
        datos = {
            'campo':campo,
            'nuevo_valor':nuevo_valor,
        }
        respuesta = requests.post(url='http://localhost:3000/productos/modificar/'+id,data=datos)
        print(respuesta.text)
    else:
        print('No existe el campo seleccionado')

def eliminar_producto():
    id = input('Ingrese el id del producto a eliminar: ')
    respuesta = requests.post(url='http://localhost:3000/productos/eliminar/'+id)
    print(respuesta.text)

def nueva_venta():
    cliente = input('Ingrese el nombre del cliente: ')
    total = 0
    productos = []
    print('Seleccione los productos. Presione 0 para salir.')
    while True:
        id = input('Ingrese el id del producto: ')
        if (id == '0'):
            break
        else:
            producto = requests.get(url='http://localhost:3000/productos/buscar/'+id)
            if len(producto.json()):
                nombre = producto.json()[0]['nombre']
                precio = producto.json()[0]['precio']
                cantidad = input('Ingrese la cantidad: ')
                total_por_producto = int(cantidad) * float(precio)
                total += total_por_producto
                productos.append([id, nombre, precio, cantidad, total_por_producto])
                mostrar_venta(cliente, productos, total)
            else:
                print('Producto no encontrado')

def mostrar_venta(cliente, productos, total):
    print('\n\t\tComprobante de venta')
    print('\nCliente: '+cliente)
    headers = ['ID', 'NOMBRE', 'PRECIO', 'CANTIDAD', 'TOTAL']
    tabla = tabulate(productos, headers, tablefmt='simple')
    print(tabla)
    print('\t\t\tTotal a pagar: '+ str(total))

try:
    iniciar()
except KeyboardInterrupt:
    os.system('clear')
    print('Programa terminado por el usuario')