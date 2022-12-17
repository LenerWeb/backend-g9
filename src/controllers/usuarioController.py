from flask_restful import Resource, request
from dtos.request.registroDto import RegistroDto
from dtos.request.loginDto import LoginDto
from dtos.response.usuarioDto import UsuarioDto
from models.usuario import UsuarioModel
from config import conexion
from bcrypt import gensalt, hashpw, checkpw
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_jwt

class RegistroController(Resource):
    def post(self):
        body = request.get_json()
        try:
            # load sirve para cargar la informacion y validar si es o no correcta
            data = RegistroDto().load(data=body)
            # usuariomodel(nombre=data)
            nuevoUsuario = UsuarioModel(**data)
            # hash completamente aleatorio
            salt = gensalt(rounds=10)

            password = data.get('password')
            password_bytes = bytes(password, 'utf-8')

            #combinamos el salt con la contraseña enviada
            hash_password = hashpw(password_bytes, salt)
            hash_password_string = hash_password.decode('utf-8')

            # modificamos la contraseña antes de guardarla en la bd
            nuevoUsuario.password =hash_password_string
            conexion.session.add(nuevoUsuario)
            conexion.session.commit()
            return {
                'message': 'Usuario creado exitosamente',
            }

        except Exception as e:
            return {
                'message': 'Error al registrar el usuario',
                'content': e.args
            }

class LoginController(Resource):
    def post(self):
        body = request.get_json()
        try: 
            data = LoginDto().load(body)
            # SELECT * FROM  usuarios WHERE correo= '..' LIMIT1
            usuarioEncontrado = conexion.session.query(UsuarioModel).filter_by(correo=data.get('correo')).first()
            if usuarioEncontrado is None:
                raise Exception('El usuario no existe')

            password = bytes(data.get('password'), 'utf-8')
            hashed_password = bytes(usuarioEncontrado.password,'utf-8')
            if checkpw(password, hashed_password):    
                # es la contraseña correcta
                payload = {
                    'jti': usuarioEncontrado.id,
                    'nombre': usuarioEncontrado.nombre
                }
                token = create_access_token(identity=usuarioEncontrado.id, additional_claims=payload)
                return {
                    'message': 'Bienvenido',
                    'content': token
                }
            else:
                raise Exception('Contraseña incorrecta')

        except Exception as e:
            return{
                'message':'Error al hacer el login',
                'content': e.args
            }


class PerfilController(Resource):
    @jwt_required()
    def get(self):
        # para utiliar estos metodos la token tioen que ser valida y tiene que lograr desencriptarse utilizando la contraseña
        usuarioId = get_jwt_identity() 
        print(get_jwt_identity()) # mostrara el contenido que hemos seteado en nuestro parametro identity al momnento de rear la token (sub en el payload)
        print(get_jwt()) # mostrara todo el payload de la token
        usuarioEcontrado = conexion.session.query(UsuarioModel).filter_by(id=usuarioId).first()
        resultado = UsuarioDto().dump(usuarioEcontrado)
        return {
            'content': resultado
        }
