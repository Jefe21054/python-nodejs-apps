from conexion import *

def registrar(titulo,autor,estado):
    try:
        con = conectar()
        cursor = con.cursor()
        sentencia_sql = ''' INSERT INTO libro (titulo,
        autor,estado) values (%s,%s,%s) '''
        datos = (titulo,autor,estado,)
        cursor.execute(sentencia_sql,datos)
        con.commit()
        con.close()
        msje = 'Registro Correcto'
        return msje
    except mysql.Error as err:
        print('Ha ocurrido un error',err)

def mostrar():
    datos = []
    try:
        con = conectar()
        cursor = con.cursor()
        sentencia_sql = ''' SELECT * FROM libro '''
        cursor.execute(sentencia_sql)
        datos = cursor.fetchall()
        con.close()
        return datos
    except mysql.Error as err:
        print('Ha ocurrido un error',err)

def buscar(id):
    datos = []
    try:
        con = conectar()
        cursor = con.cursor()
        sentencia_sql = ''' SELECT * FROM libro WHERE id=%s '''
        cursor.execute(sentencia_sql,(id,))
        datos = cursor.fetchall()
        con.close()
        return datos
    except mysql.Error as err:
        print('Ha ocurrido un error',err)

def modificar(id,campo,nuevoValor):
    try:
        sentencia_sql = ''
        con = conectar()
        cursor = con.cursor()
        if campo == '1':
            sentencia_sql = 'UPDATE libro SET titulo=%s WHERE id=%s'
        elif campo == '2':
            sentencia_sql = 'UPDATE libro SET autor=%s WHERE id=%s'
        elif campo == '3':
            sentencia_sql = 'UPDATE libro SET estado=%s WHERE id=%s'
        else:
            print('El campo elegido no existe')
        datos = (nuevoValor,id,)
        cursor.execute(sentencia_sql,datos)
        con.commit()
        con.close()
        msje = 'Se actualizo correctamente'
        return msje
    except mysql.Error as err:
        print('Ha ocurrido un error',err)

def eliminar(id):
    try:
        con = conectar()
        cursor = con.cursor()
        sentencia_sql = 'DELETE FROM libro WHERE id=%s'
        cursor.execute(sentencia_sql,(id,))
        con.commit()
        con.close()
        msje = 'Se ha eliminado'
        return msje
    except mysql.Error as err:
        print('Ha ocurrido un error',err)
