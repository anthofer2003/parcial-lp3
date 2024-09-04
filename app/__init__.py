from flask import Flask

app = Flask(__name__)

# importar referencias

from app.rutas.referenciales.ciudad.ciudad_routes import ciumod

# registrar referenciales

app.register_blueprint(ciumod, url_prefix='/ciudad')

