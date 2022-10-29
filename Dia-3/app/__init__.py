

from flask import Flask, request
# from os import getenv

app = Flask(__name__)
# clave_secreta = getenv('SECRET')
# print(clave_secreta)

@app.route("/")
def index():
    return 'Hola soy un servidor de Flask'

usuarios = [
    {
        "nombre":"Paolo",
        "dni": "77777777"
    },
    {
        "nombre":"Eduardo",
        "dni": "78787878"
    }
]


@app.route("/<dni>")
def home(dni):
    for usuario in usuarios:
        if usuario ['dni']  == dni:
            return f'El nombre del usuario es: {usuario["nombre"]}'
    return f'El usuario con el numero de dni: {dni} no fue encontrado'

@app.route("/auth/login", methods=['POST'])
def login():
    usuario = {
        "username":"paolo",
        "password":"osito123"
    }
    json = request.get_json()
    if (usuario['username']==json['username']and usuario['password']==json['password']):
        return 'Usuario logueado'
    return 'las credenciales son incorrectas'


@app.route("/products", methods=['POST', 'GET', 'PUT', 'DELETE'])
def products():
    return 'Esta es la ruta productos'