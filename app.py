from flask import Flask
from flask_migrate import Migrate
from os import environ
from dotenv import load_dotenv
from flask_restful import Api

from config import conexion
from models.usuarios import UsuarioModel
from models.tareas import TareaModel
from controllers.usuarioController import UsuariosController, UsuarioController
from controllers.pruebaController import PruebaController
from controllers.tareaController import TareasController, TareaController


# Para cargar las variables del archivo .env para que puedan ser utilizadas como variables de entorno
load_dotenv()

app = Flask(__name__)

# Aca inicializamos la clase Api que nos servira para poder utilizar todos los controladores dentro de la aplicacion de flask
api = Api(app)

# la conexion a la base de datos que susara para SQLALCHEMY conectarse 
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URI')

# mostrara todas las consultas en lenguaje SQL que se realiza a la base de ddatos
app.config['SQLALCHEMY_ECHO'] = environ.get('MOSTRAR_SQL') # esto es un boolean

# inicializamos la instancia de Flask-SQLAlchemy con las aplicaciones seteadas en la aplicacion de Flask
conexion.init_app(app)

# inicializamos la clase migrate con la configuracion de nuestra Base de Datos y aplicacion de Flask
migrate = Migrate(app, conexion)

# Declarar todas las rutas que vamos a utilizar mediante los controladores
api.add_resource(UsuariosController, '/usuarios')
api.add_resource(PruebaController, '/prueba')
api.add_resource(UsuarioController, '/usuario/<int:id>')
api.add_resource(TareasController, '/tareas')
api.add_resource(TareaController, '/tarea/<int:usuarioId>')

if __name__ == '__main__':
    app.run(debug = True)
