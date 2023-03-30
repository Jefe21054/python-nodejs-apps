const express = require('express')
const app = express()
require('./conexion')

app.use(express.urlencoded({extended: false}))
app.use(express.json())

app.listen(3000, ()=>{
    console.log('Aplicacion corriendo en el puerto 3000')
})