#request > toda la informacion que puedo leer del usuario, dentro de ella tendremos el body
from flask import Flask, request
from datetime import datetime

usuarios = [
    {
        'correo': 'lenerweb@hotmail.com',
        'nombre':'lener',
        'apellido':'zavaleta'
    },
    {
        'correo': 'Rutty@hotmail.com',
        'nombre':'Ruth',
        'apellido':'Rosas'
    }
]

# __name__ > muestra si el archivo es el archivo principal del proyecto; mostrara el valor de '__main__' y si no entonces mostrara otro valor.
#print(__name__) # imprime __main__
app = Flask(__name__)

# Endpoint > es cuando definimos una ruta para que pueda ser accedida
# si no se define que verbo HTTp puede acceder, entonces el valor por defecto sera GET
@app.route('/', methods = ['GET'])
def inicio():
    # Controlador (Controller) > la funcionalidad que tendra mi endpoint
    print('ingreso al endpoint inicial')
    # siempre en todo controlador hay que retornar algo
    return 'Bienvenido a mi primera API en Flask semana 2'

@app.route('/estado', methods = ['GET'])
def estado():
    # https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
    hora_servidor = datetime.now().strftime('%Y-%m-%d %I:%M:%S %p')
    return {
        'estado': True,
        'hora': hora_servidor
    }

@app.route('/registrarse', methods=['POST'])
def registro():
    #request.data > el body pero en formato puro (formato bytes)
    print(request.data)
    # request.get_json > convierte informacion entrante en un diccionario para utilizarlos in problemas en python
    print('request',request.get_json())
    body = request.get_json()
    #iterar el arreglo de usuarios y validar que no exista un usuario con ese correo proveniente del body
    
    # como extraer la informacion de un diccionario:
    # body.get('correo') # trae vacio si no hay
    # body['correo'] # trae error si no hay

    # Si no existe entonces agregar ese usuario al arreglo, caso contrario, retornar un mensaje que diga que el usuario ya esta registrado
        
    for usuario in usuarios:
        print("usuario",usuario)
        correo = usuario.get('correo')
        if correo == body.get('correo'):
            return{
                'message':'El usuario ya esta registrado'
            }
    
    usuarios.append(body)

    return {
        'message':'Usuario registrado exitosamente'
    }

# crear un endpoint que sea /listar-usuarios y este devolviera el siguiente resultado
# {message: 'los usuarios son' content: [{...},{...}]}
@app.route('/listar-usuarios', methods=['GET'])
def listar():
    return {
        'message':'los usuarios son',
        'content': usuarios
    }

# run > sirve para correr nuestro servidor en modo de desarrollo
# si declaramos algo despues del metodo run este nunca se llamara porque aca se queda 'pegado' esperando peticiones del cliente

# debug > indicara si guardamos algun archivo dentro del proyecto reiniciara automaticamente el servidor
app.run(debug=True)

#hacer el FrontEnd dela tabla y del formulario en html con css para el miercoles.