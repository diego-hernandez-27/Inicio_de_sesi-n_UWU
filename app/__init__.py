from flask import Flask
import secrets

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)

from app import routes  # Importa las rutas después de crear la app

print(secrets.token_hex(16))
