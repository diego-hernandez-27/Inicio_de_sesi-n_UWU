from flask import render_template, make_response
from run import app
from weasyprint import HTML
import tempfile
import os
import base64

def get_logo_base64():
    logo_path = os.path.join(app.static_folder, 'img', 'logo.png')
    with open(logo_path, 'rb') as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

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

def generate_pdf_content(title, subtitle, content):
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            body {{
                font-family: Arial, sans-serif;
                line-height: 1.6;
                color: #333;
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
                background: #f5f5f5;
            }}
            h1 {{
                color: #004080;
                text-align: center;
                margin-bottom: 10px;
            }}
            h2 {{
                color: #0066cc;
                text-align: center;
                margin-bottom: 30px;
            }}
            h3 {{
                color: #004080;
                margin-top: 30px;
            }}
            .content {{
                background: #ffffff;
                padding: 20px;
                border-radius: 10px;
                margin-bottom: 20px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }}
            .highlight {{
                background: #e6f0ff;
                border-left: 4px solid #0066cc;
                padding: 15px;
                margin: 20px 0;
            }}
            ul {{
                padding-left: 20px;
            }}
            li {{
                margin-bottom: 10px;
            }}
            strong {{
                color: #004080;
            }}
            .header {{
                text-align: center;
                margin-bottom: 30px;
            }}
            .logo {{
                max-width: 150px;
                margin-bottom: 20px;
            }}
            .slogan {{
                color: #666;
                font-style: italic;
                margin-top: 10px;
                font-size: 0.9em;
            }}
        </style>
    </head>
    <body>
        <div class="header">
            <img src="data:image/png;base64,{get_logo_base64()}" class="logo" alt="Logo">
            <p class="slogan">Tan seguros que nos aseguramos de no tener un buen slogan</p>
        </div>
        <h1>{title}</h1>
        <h2>{subtitle}</h2>
        <div class="content">
            {content}
        </div>
    </body>
    </html>
    """

@app.route('/curiosidad/cifrado-cesar/pdf')
def cifrado_cesar_pdf():
    content = """
        <h3>¿Qué es el Cifrado César?</h3>
        <p>El Cifrado César es uno de los métodos de cifrado más antiguos y conocidos de la historia. Fue utilizado por Julio César para proteger sus comunicaciones militares durante las campañas romanas. Este método de cifrado es un tipo de cifrado por sustitución, donde cada letra del texto original es reemplazada por otra letra que se encuentra un número fijo de posiciones más adelante en el alfabeto.</p>
        
        <div class="highlight">
            <p><strong>Ejemplo práctico:</strong> Si usamos un desplazamiento de 3 posiciones, la letra 'A' se convierte en 'D', 'B' en 'E', y así sucesivamente. Al llegar al final del alfabeto, se continúa desde el principio.</p>
        </div>

        <h3>Historia y Origen</h3>
        <p>El Cifrado César tiene sus raíces en la antigua Roma, específicamente durante el período de Julio César (100-44 a.C.). Se dice que César utilizaba este método para comunicarse con sus generales y gobernadores en las provincias romanas. El desplazamiento de 3 posiciones que usaba César se conoce como "ROT3" en la terminología moderna de criptografía.</p>
        
        <p>Este método de cifrado fue tan efectivo para su época que incluso el gran orador Cicerón lo utilizó en algunas de sus comunicaciones privadas. La simplicidad del método lo hacía fácil de implementar, pero también lo hacía vulnerable a ataques de fuerza bruta.</p>

        <h3>Importancia Histórica</h3>
        <ul>
            <li>Fue uno de los primeros sistemas de cifrado documentados en la historia</li>
            <li>Estableció el concepto de clave de cifrado (el número de posiciones a desplazar)</li>
            <li>Demostró la importancia de la seguridad en las comunicaciones militares</li>
            <li>Sirvió como base para el desarrollo de sistemas de cifrado más complejos</li>
        </ul>

        <h3>Legado en la Criptografía Moderna</h3>
        <ul>
            <li>Inspiró el desarrollo de cifrados más complejos como el Vigenère</li>
            <li>Se utiliza como herramienta educativa para enseñar conceptos básicos de criptografía</li>
            <li>Sus principios se pueden encontrar en algoritmos modernos de cifrado</li>
            <li>Es un excelente ejemplo de la evolución de la seguridad informática</li>
        </ul>

        <h3>Vulnerabilidades y Limitaciones</h3>
        <ul>
            <li>Fácil de descifrar mediante análisis de frecuencia de letras</li>
            <li>Solo tiene 25 posibles claves (desplazamientos)</li>
            <li>No protege contra ataques de fuerza bruta</li>
            <li>No incluye autenticación ni integridad del mensaje</li>
        </ul>
    """
    html = generate_pdf_content("El Cifrado César", "El primer sistema de cifrado de la historia", content)
    pdf = HTML(string=html).write_pdf()
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=cifrado_cesar.pdf'
    return response

@app.route('/curiosidad/votacion-electronica/pdf')
def votacion_electronica_pdf():
    content = """
        <h3>¿Qué es la Votación Electrónica?</h3>
        <p>La votación electrónica es un sistema que permite a los ciudadanos emitir su voto de manera digital, utilizando dispositivos electrónicos en lugar de papeletas físicas. La criptografía juega un papel fundamental en estos sistemas, garantizando la seguridad, privacidad y autenticidad de cada voto.</p>
        
        <div class="highlight">
            <p><strong>Dato importante:</strong> La votación electrónica no solo debe ser segura, sino también verificable y transparente, permitiendo a los votantes confirmar que su voto fue contado correctamente sin revelar su elección.</p>
        </div>

        <h3>Mecanismos de Seguridad</h3>
        <ul>
            <li><strong>Cifrado de extremo a extremo:</strong> Protege los votos durante la transmisión</li>
            <li><strong>Firmas digitales:</strong> Verifican la autenticidad de cada voto</li>
            <li><strong>Pruebas de conocimiento cero:</strong> Permiten verificar la validez del voto sin revelar su contenido</li>
            <li><strong>Algoritmos de mezclado:</strong> Desvinculan los votos de los votantes</li>
        </ul>

        <h3>Desafíos y Soluciones</h3>
        <ul>
            <li><strong>Privacidad:</strong> Garantizar que nadie pueda vincular un voto con un votante específico</li>
            <li><strong>Integridad:</strong> Asegurar que los votos no puedan ser modificados</li>
            <li><strong>Verificabilidad:</strong> Permitir la verificación de resultados sin comprometer la privacidad</li>
            <li><strong>Accesibilidad:</strong> Facilitar el voto para personas con discapacidades</li>
        </ul>

        <h3>Sistemas Avanzados</h3>
        <ul>
            <li><strong>Votación con Pruebas de Conocimiento Cero:</strong> Permite verificar la validez del voto sin revelar su contenido</li>
            <li><strong>Votación Homomórfica:</strong> Permite realizar operaciones sobre votos cifrados</li>
            <li><strong>Votación con Umbral:</strong> Distribuye la autoridad de conteo entre múltiples entidades</li>
            <li><strong>Votación con Verificación de Extremo a Extremo:</strong> Permite a los votantes verificar que su voto fue contado correctamente</li>
        </ul>

        <h3>Impacto en la Democracia</h3>
        <ul>
            <li>Aumenta la accesibilidad al proceso electoral</li>
            <li>Reduce los costos de organización de elecciones</li>
            <li>Facilita el voto desde el extranjero</li>
            <li>Mejora la transparencia y confianza en el proceso electoral</li>
        </ul>

        <h3>Consideraciones Éticas y Sociales</h3>
        <ul>
            <li>Equilibrio entre seguridad y usabilidad</li>
            <li>Accesibilidad para todos los sectores de la población</li>
            <li>Transparencia en el proceso de verificación</li>
            <li>Protección contra la coerción y el voto forzado</li>
        </ul>
    """
    html = generate_pdf_content("Criptografía en Votación Electrónica", "Garantizando la seguridad y transparencia en las elecciones digitales", content)
    pdf = HTML(string=html).write_pdf()
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=votacion_electronica.pdf'
    return response

@app.route('/curiosidad/cifrado-pigpen/pdf')
def cifrado_pigpen_pdf():
    content = """
        <h3>¿Qué es el Cifrado Pigpen?</h3>
        <p>El Cifrado Pigpen, también conocido como Cifrado Masónico, es un sistema de cifrado por sustitución que utiliza símbolos geométricos en lugar de letras. Este método fue ampliamente utilizado por los masones para comunicarse de manera secreta y proteger sus rituales y documentos.</p>
        
        <div class="highlight">
            <p><strong>Característica única:</strong> A diferencia de otros cifrados, el Pigpen utiliza símbolos que se asemejan a las letras que representan, lo que lo hace más fácil de memorizar pero también más fácil de descifrar para quienes conocen el patrón.</p>
        </div>

        <h3>Origen e Historia</h3>
        <p>El Cifrado Pigpen tiene sus raíces en la masonería del siglo XVIII. Se cree que fue desarrollado como una forma de proteger la privacidad de las comunicaciones masónicas y mantener la confidencialidad de sus rituales y documentos. El nombre "Pigpen" (corral de cerdos) proviene de la apariencia de los símbolos, que algunos comparan con los corrales utilizados para encerrar cerdos.</p>
        
        <p>Este cifrado fue particularmente popular durante el período de la Ilustración, cuando las sociedades secretas como los masones necesitaban métodos de comunicación seguros para proteger sus actividades y miembros.</p>

        <h3>Estructura del Cifrado</h3>
        <ul>
            <li>Utiliza dos cuadrículas de 3x3 para las letras</li>
            <li>La primera cuadrícula contiene las letras A-I</li>
            <li>La segunda cuadrícula contiene las letras J-R</li>
            <li>Las letras restantes (S-Z) se representan con símbolos especiales</li>
            <li>Cada letra se representa por las líneas que forman su "corral" en la cuadrícula</li>
        </ul>

        <h3>Uso en la Masonería</h3>
        <ul>
            <li>Proteger la privacidad de sus rituales</li>
            <li>Comunicarse de manera segura entre logias</li>
            <li>Documentar información sensible</li>
            <li>Crear símbolos y marcas distintivas</li>
        </ul>

        <h3>Legado Cultural</h3>
        <ul>
            <li>Aparece en numerosas obras de ficción y películas</li>
            <li>Se utiliza en juegos de escape room y acertijos</li>
            <li>Es popular en la literatura de misterio y conspiración</li>
            <li>Se enseña como ejemplo de cifrado histórico en cursos de criptografía</li>
        </ul>

        <h3>Vulnerabilidades y Limitaciones</h3>
        <ul>
            <li>Fácil de descifrar una vez que se conoce el patrón</li>
            <li>No proporciona una seguridad real en la era moderna</li>
            <li>Limitado a caracteres alfabéticos</li>
            <li>No incluye números ni caracteres especiales</li>
        </ul>

        <h3>Uso Moderno</h3>
        <ul>
            <li>Educación en criptografía básica</li>
            <li>Juegos y acertijos</li>
            <li>Arte y diseño</li>
            <li>Preservación histórica</li>
        </ul>
    """
    html = generate_pdf_content("El Cifrado Pigpen", "El lenguaje secreto de los masones", content)
    pdf = HTML(string=html).write_pdf()
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=cifrado_pigpen.pdf'
    return response
