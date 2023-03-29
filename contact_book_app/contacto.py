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
        return str('Ha ocurrido un error: ',err)
