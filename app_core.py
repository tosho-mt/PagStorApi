""" App core """
from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt


app = Flask(__name__)

bcrypt = Bcrypt(app)

app.config['SECRET_KEY'] = 'SisFiabPagoStore'


#controlar errores rutas no existentes y mas
@app.errorhandler(404)
def page_not_found(err):
        return jsonify({'mensage':'inicio API, Ruta no existe'})