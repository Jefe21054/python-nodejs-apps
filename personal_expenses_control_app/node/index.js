const express = require('express')
const movimientoRouter = require('./routes/movimiento')
const app = express()

app.use(express.urlencoded({extended:false}))
app.use(express.json())

app.use('/movimientos', movimientoRouter)

app.listen(3000, ()=>{
    console.log('Aplicacion corriendo en el puerto 3000')
})