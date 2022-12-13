from flask import Flask
from os import environ
from flask_migrate import Migrate
from config import conexion
#declaramos los modelos para que el historial de migraciones lo registre
from models.usuario import UsuarioModel
from models.intercambio import IntercambioModel
from models.regalo import RegaloModel

#Para utilizar ñas varoables declaradas en el archivo .env como variable de entorno
from dotenv import load_dotenv
load_dotenv()

aplicacion = Flask(__name__)

#variable que utiliza sqlalchemy pra poder conectarse a la base de datos
aplicacion.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URI')

#inicializamos la conexion utilizando la variable seteada previamente
conexion.init_app(app=aplicacion)

# comenzamos a utilizar las migraciones
Migrate(app=aplicacion, db=conexion)

if __name__ == '__main__':
    aplicacion.run(debug=True)