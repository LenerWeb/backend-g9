from flask_restful import Resource, request
from config import conexion
from models.usuarios import UsuarioModel
from dtos.usuarioDto import UsuarioRequestDto

class UsuariosController(Resource):
    # los metodos que no queramos utilizar (GET, POST) lo tendremos que definir como metodo de la clase
    def get(self):
        # https://docs.sqlalchemy.org/en/14/orm/query.html#query-api
        # SELECT * FROM usuarios;
        # me devolvera una lista con toddas las instancias de la clase UsuarioModel pero las tengo que formatear para poder devolverlas al frontend
        usuarios = conexion.session.query(UsuarioModel).all()

        # --------------------------------------------
        # MODO NORMAL
        # si que remos pasarle un conjunto de instancia (lista) al DTO se agrega many=True
        serializador = UsuarioRequestDto(many=True)
        # A este metodo le pasamos informacion proveniente de la vbase de datos y nos los convertira a un tipo de dato que pueda ser legible por el frontend
        # en base al modelo que estamos trabajando en ese DTO hara la conversion de tipos de datos (str, int, float, etc)
        # el metodo dum solamente  espera recibir una instancia a la vez
        data = serializador.dump(usuarios)
        # -------------------------------------

        # --------------------------------------
        # modo principiante
        # >print(usuarios)
        # >print(usuarios[0].nombre)
        # hacer un for en el cual se iteran todos los usuarios y cada usuario convertirlo a un diccionario que tenga el siguiente formato

        # y luego agreagarlo a la lista
        # usuariosFinales = []
        # for usuario in usuarios:
        #     usuarioDiccionario = {
        #         'id':usuario.id,
        #         'nombre':usuario.nombre,
        #         'correo':usuario.correo,
        #         'telefono':usuario.telefono
        #     }
        #     usuariosFinales.append(usuarioDiccionario)
        # --------------------------------------------
        return {
            'message': 'Los usuarios son:',
            'content': data
        }

    def post(self):
        body = request.get_json()
        try:
            # Instancia de mi DTO de usuario
            serializador = UsuarioRequestDto()
            dataSerializada = serializador.load(body)
            print(dataSerializada)

            # Primero creo una nueva instancia de mi clase model
            # para mayor informacion mira el archivo reapso_funciones_infinitas.py
            nuevoUsuario = UsuarioModel(**dataSerializada)
            # asigno los valores a los atributos provenientes del body
            # INSERT INTO usuarios(nombre, correo, telefono) VALUES ('...', '...', '...');

            # Forma principiante 
            # nuevoUsuario.correo = body.get('correo')
            # nuevoUsuario.nombre = body.get('nombre')
            # nuevoUsuario.telefono = body.get('telefono')

            # ahora agregamos a la base de datos ese nuevo registro creado en vase a la instancia
            conexion.session.add(nuevoUsuario)
            # guardar de manera permanente la informacion agregada al nuevo usuario
            conexion.session.commit()
            # print(body)
            return{
                'message': 'Usuario creado exitosamente'
            }

        except Exception as error:
            print(error)
            return{
                'message':'Error al crear el usuario',
                'content': error.args
            }

class UsuarioController(Resource):
    def get(self, id):
        # NOTA: EL PARAMETRO QUE NOSOTROS INDICAMOS AL METODO TIENE QUE SER EXACTAMENTE EL MISMO QUE HERMOS definido en la ruta
        #devolver un solo usuario
        # SELECT*FROM usuarios WHERE id = 2 LIMIT 1;
        usuarioEncontrado = conexion.session.query(UsuarioModel).filter_by(id=id).first()
        # UTILIZANDO EL USUARIOrEQUESTdTO PASARLE EL USUARIOeNCONTRADO Y DEVOLVER ESA INFORMACION
        serializador = UsuarioRequestDto()
        #esto seria sin usar el serializado
        # data = {
        #     'id' : usuarioEncontrado['id'],
        #      ...
        # }

        data = serializador.dump(usuarioEncontrado)

        return {
            'content': data
        }

    def put(self, id):
        try:
            #buscare ese usuario por el id
            usuarioEncontrado = conexion.session.query(UsuarioModel).filter_by(id=id).first()
            # si no hay usuario con ese id
            if usuarioEncontrado is None:
                raise Exception('Usuario no existe')

            body = request.get_json()
            serializador = UsuarioRequestDto()
            data = serializador.load(body)
            print(data['telefono'])
            # posdemos utilizar un try-except dentro de otro pero este funcionara solamente para el codigo que esta delntrop del try y acada uno actuara de manera indepéndiente

            # si el usuario no me envie el telefono entonces conservar el valor anterior pero si me envia el valor null ahi si le eliminamos el telefono
            telefono = usuarioEncontrado.telefono
            try:
                # si la llave 'telefono' no existe emitira un error por lo que ingresara al except y por ende, en este caso, no haremos nada 
                telefono = data['telefono']
            except:
                pass
            # aca sobreescribimos la informacion nueva del usuario
            usuarioEncontrado.nombre = data.get('nombre')
            usuarioEncontrado.correo = data.get('correo')
            usuarioEncontrado.telefono = telefono # ojo revisar repositorio profe

            conexion.session.commit()

            return {
                'message': 'Usuario actualizado exitosamente'
            }

        except Exception as error:
            return {
                'message':'error al actualizar el usuario',
                'content': error.args
            }
            
    def delete(self, id):
        try:
            # Buscamos el usuario
            usuarioEncontrado = conexion.session.query(UsuarioModel).filter_by(id=id).first()
            # Si no hay el usuario emitimos un error
            if usuarioEncontrado is None:
                raise Exception ('Usuario no existe')
            # asi eliminamos el usuario de la base de datos
            conexion.session.delete(usuarioEncontrado)
            #aqui confirmamos la eliminacion de manera permanente
            conexion.session.commit()
            return {
                'message':'El usuario se elimino exitosamente'
            }
        except Exception as error:
            return {
                'message':'Error al eliminar el usuario',
                'content': error.args
            }