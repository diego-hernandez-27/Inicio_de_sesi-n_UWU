from flask import render_template
from run import app
from app.pdf_generator import generate_cifrado_cesar_pdf, generate_votacion_electronica_pdf, generate_cifrado_pigpen_pdf

@app.route('/')
def inicio():
    return render_template('iniciar_sesion.html')

@app.route('/registrarse')
def registrarse():
    return render_template('registrarse.html')

@app.route('/restablecer')
def restablecer():
    return render_template('restablecer_contraseña.html')

@app.route('/curiosidades')
def curiosidades():
    return render_template('curiosidades.html')

@app.route('/curiosidad/cifrado-cesar')
def cifrado_cesar():
    return render_template('curiosidades/cifrado_cesar.html')

@app.route('/curiosidad/votacion-electronica')
def votacion_electronica():
    return render_template('curiosidades/votacion_electronica.html')

@app.route('/curiosidad/cifrado-pigpen')
def cifrado_pigpen():
    return render_template('curiosidades/cifrado_pigpen.html')

@app.route('/curiosidad/cifrado-cesar/pdf')
def cifrado_cesar_pdf():
    return generate_cifrado_cesar_pdf()

@app.route('/curiosidad/votacion-electronica/pdf')
def votacion_electronica_pdf():
    return generate_votacion_electronica_pdf()

@app.route('/curiosidad/cifrado-pigpen/pdf')
def cifrado_pigpen_pdf():
    return generate_cifrado_pigpen_pdf()
