from flask import Flask, render_template, request
from persona import Persona
import sqlite3


app = Flask(__name__)

@app.route('/hola')
def a():
  return "Hola pepo!!"
@app.route('/', methods=['GET','POST'])
def index():
  if request.method=='POST':
    nombre=request.form.get('nombre')
    apellido=request.form.get('apellido')
    edad=int(request.form.get('edad'))
    #persona=Persona(nombre,apellido,edad)
    coneccion = sqlite3.connect("db/mi_base_datos.db")
    cursor = coneccion.cursor()
    cursor.execute(f'INSERT INTO personas(nombre, apellido, edad) VALUES(?,?,?)',(nombre,apellido,edad))
    coneccion.commit()
    coneccion.close()
    return f' la persona se guardo correctamente'


  return render_template('formulario.html')

#creación de la bd
def crear_base_datos():
  sqlite3.connect('db/mi_base_datos.db')


#crear tabla
def crear_tabla():
  cursor.execute(f'CREATE TABLE personas (nombre TEXT,apellido TEXT,edad INT)')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81,debug=True)
    #crear_base_datos()
    #crear_tabla()

