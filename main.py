from flask import Flask, render_template, request
from persona import Persona
import sqlite3


app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def index():
  if request.method=='POST':
    nombre=request.form.get('nombre')
    apellido=request.form.get('apellido')
    edad=request.form.get('edad')
    persona=Persona(nombre,apellido,edad)
    return f' la persona{persona.nombre} se guardo correctamente'

  
  return render_template('formulario.html')


app.run(host='0.0.0.0', port=81)
if __name__ == '__main__':
    app.run(debug=True)
