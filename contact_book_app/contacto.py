from conexion import *

def registrar(nombre,apellidos,empresa,telefono,email,direccion):
    try:
        con = conectar()
        cursor = con.cursor()
        sentencia_sql = ''' INSERT INTO contacto(
            nombre,apellidos,empresa,telefono,email,direccion) values
            (?,?,?,?,?,?) '''
        datos = (nombre,apellidos,empresa,telefono,email,direccion)
        cursor.execute(sentencia_sql, datos)
        con.commit()
        con.close()
        return 'Registro correcto'
    except sqlite3.Error as err:
        print('Ha ocurrido un error: ',err)

def mostrar():
    datos = []
    try:
        con = conectar()
        cursor = con.cursor()
        sentencia_sql = ''' SELECT * FROM contacto '''
        cursor.execute(sentencia_sql)
        datos = cursor.fetchall()
        con.close()
        return datos
    except sqlite3.Error as err:
        return 'Ha ocurrido un error: ' + str(err)

def buscar(nombre):
    datos = []
    try:
        con = conectar()
        cursor = con.cursor()
        sentencia_sql = ''' SELECT * FROM contacto WHERE nombre=? '''
        cursor.execute(sentencia_sql,(nombre,))
        datos = cursor.fetchall()
        con.close()
        return datos
    except sqlite3.Error as err:
        return 'Ha ocurrido un error: ' + str(err)

def modificar(id,nombre,apellidos,empresa,telefono,email,direccion):
    try:
        con = conectar()
        cursor = con.cursor()
        sentencia_sql = ''' UPDATE contacto SET nombre=?, 
        apellidos=?, empresa=?, telefono=?, email=?, direccion=? 
        WHERE id=? '''
        datos = (nombre,apellidos,empresa,telefono,email,direccion,id)
        cursor.execute(sentencia_sql,datos)
        con.commit()
        con.close()
        msje = 'Se actualizo correctamente'
        return msje
    except sqlite3.Error as err:
        return 'Ha ocurrido un error: ' + str(err)

def eliminar(nombre):
    try:
        con = conectar()
        cursor = con.cursor()
        sentencia_sql = ''' DELETE FROM contacto WHERE nombre=? '''
        cursor.execute(sentencia_sql,(nombre,))
        con.commit()
        con.close()
        msje = 'Se elimino correctamente'
        return msje
    except sqlite3.Error as err:
        return 'Ha ocurrido un error: ' + str(err)    
