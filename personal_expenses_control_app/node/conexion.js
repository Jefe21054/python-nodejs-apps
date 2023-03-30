const mysql = require('mysql2')

const conexion = mysql.createConnection({
    host: "localhost",
    user: "jefe21054",
    password: "admin",
    database: "gastos",
})

conexion.connect((err, conn)=>{
    if (err) {
        console.log('Ha ocurrido un error al conectarse a la base de datos: ' + err)
    }else{
        console.log('Conexion exitosa')
        return conn    
    }
})

module.exports = conexion