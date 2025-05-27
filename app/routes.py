from flask import render_template, flash, redirect, url_for, jsonify, request
from run import app
from app.pdf_generator import generate_cifrado_cesar_pdf, generate_votacion_electronica_pdf, generate_cifrado_pigpen_pdf
from app.forms import RegistrationForm
from app.models import User

@app.route('/')
def inicio():
    return render_template('iniciar_sesion.html')

@app.route('/registrarse', methods=['GET', 'POST'])
def registrarse():
    form = RegistrationForm()
    if request.method == 'POST':
        try:
            # Verificar si el usuario ya existe
            if User.get_by_username(request.form['username']):
                return jsonify({
                    'success': False, 
                    'message': 'Este nombre de usuario ya está en uso'
                })

            # Verificar si el email ya existe
            if User.get_by_email(request.form['email']):
                return jsonify({
                    'success': False, 
                    'message': 'Este email ya está registrado'
                })

            # Si no existe, crear el nuevo usuario
            user = User(
                username=request.form['username'],
                email=request.form['email'],
                password=request.form['password']
            )
            user.save()
            return jsonify({
                'success': True, 
                'message': '¡Registro exitoso! Ahora puedes iniciar sesión.'
            })
        except Exception as e:
            return jsonify({
                'success': False, 
                'message': f'Error al registrar usuario: {str(e)}'
            })
    return render_template('registrarse.html', form=form)

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
