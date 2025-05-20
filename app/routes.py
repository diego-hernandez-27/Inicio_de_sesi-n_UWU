from flask import render_template
from run import app

@app.route('/')
def inicio():
    return render_template('iniciar_sesion.html')

@app.route('/registrarse')
def registrarse():
    return render_template('registrarse.html')

@app.route('/restablecer')
def restablecer():
    return render_template('restablecer_contraseña.html')
