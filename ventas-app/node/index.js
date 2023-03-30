const express = require('express')
const conexion = require('./conexion')

const app = express()

app.use(express.urlencoded({extended:false}))
app.use(express.json())

app.listen(3000, ()=>{
    console.log('Aplicacion corriendo en el puerto 3000')
})