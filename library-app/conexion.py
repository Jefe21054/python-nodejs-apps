import mysql.connector as mysql

def conectar():
    try:
        conexion = mysql.connect(
            host = 'localhost',
            user = 'jefe21054',
            password = 'admin',
            database = 'libros',
        )
        print('Se ha conectado a la base de datos')
        return conexion
    except mysql.Error as err:
        print('Ha ocurrido un error',err)
