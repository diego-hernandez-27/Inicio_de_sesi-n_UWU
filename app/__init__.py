from flask import Flask

app = Flask(__name__)

from app import routes  # Importa las rutas después de crear la app
