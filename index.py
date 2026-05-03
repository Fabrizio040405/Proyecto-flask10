from flask import Flask,render_template,request
import json 
from lector_json import Lector

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('login.html',message='Ingrese su usuario')

@app.route('/menu',methods=["POST"])
def ingresar():
    nombre = request.form.get('nombre')
    contraseña = request.form.get('contraseña')

    archivo : Lector = Lector('C:\Proyecto-flask10\listado.json') # Lector(ruta)

    if archivo.validar_contra(nombre,contraseña):
        return render_template('otro.html',messages='Bienvenido')
    else:
        return render_template('login.html',message='Usuario no encontrado')

@app.route('/',methods=['POST'])    
def regresar():
    return render_template('login.html',message='Ingrese su usuario')

if __name__=='__main__':
    app.run(debug=True,port=5001)