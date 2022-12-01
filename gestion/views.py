from rest_framework.generics import CreateAPIView, ListCreateAPIView, UpdateAPIView, ListAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .models import	UsuarioModel, PlatoModel
from .serializers import UsuarioSerializer, PlatoSerializer
# IsAuthenticated > solamente verifica que en la peticion este enviando una toquen valida
# IsAuthenticatedOrReadOnly > Solamente para los metodos QUE NO SEAN GET pedira una token valida
# IsAdminUser > verifica que el usuario de la token sea un usuario administrador (is_superuser = True)
# AllowAny > Permite el libre acceso a todo el mundo
# https://www.django-rest-framework.org/api-guide/permissions/
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view
from .permissions import SoloAdmin
# para utilizar la raw queries 
from django.db import connection


class RegistroUsuarioApiView(CreateAPIView):
    queryset = UsuarioModel.objects.all()
    serializer_class= UsuarioSerializer
    permission_classes = [ SoloAdmin ]

    def post(self, request:Request):
        informacion = self.serializer_class(data=request.data)
        # donde valida que todosd los datos sean correctos
        es_valida = informacion.is_valid()

        if not es_valida:
            return Response(data={
                'message':'Error al crear el usuario',
                'content': informacion.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            # Gracias que el serializador es un modelSerializer el metodo save sirve para registrar ese nuevo usuario en la base de datos
            nuevoUsuario = informacion.save()
            # utilizamos el serializador para convertir el nuevo usuario creado a una data legible
            nuevoUsuarioSerializado = self.serializer_class(instance=nuevoUsuario)

            return Response(data={
                'message':'Usuario creado exitosamente, ya se puede logear',
                # contiene todo el valor del registro pero con sus valores ya registrados en la base de datos
                'content': nuevoUsuarioSerializado.data
            }, status=status.HTTP_201_CREATED)
        
class PlatosApiView(ListCreateAPIView):
    queryset = PlatoModel.objects.all()
    serializer_class = PlatoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request:Request):
        # podemos pasar dos parametroos PERO o es uno o es el otro
        # parametro data> queremos pasar informacion que uan no esta guardad en la base de datos eso se usa para ahcer la validacion de esa info
        # parametro instance > pasar una INSTANCIA de ese registro que ya se encuentra en la base de datos, se utiliza para convertir esa ingormacion en una informacion legible para el cliente
        data = self.serializer_class(data=request.data)
        # raise_exception > si hay algun error, automaticamente detiene todo el proceso y emite el error
        data.is_valid(raise_exception=True)

        nuevoPlato = data.save()

        return Response(data={
            'message':'plato creado exitosamente',
            'content': self.serializer_class(instance=nuevoPlato).data
        })
        
    def get(self, request:Request):
        # ejecuta el queryset para que otra vez se vuelva a llamar a la extraccion de la informacion
        # https://docs.djangoproject.com/en/4.1/topics/db/queries/
        # SELECT *FROM platos WHERE disponibilidad = true;
        platos = PlatoModel.objects.filter(disponibilidad = True).all()
        # many > sirve para iondicar al serializador quye se le pasara un conjuyto de instancias y las tiene que iterar para poder serializarlas / deserializarlas
        platos_serializados = self.serializer_class(instance=platos, many=True)

        return Response(data={
            'message':'los platos son:',
            'content': platos_serializados.data
        })
    
class PlatoToggleApiView(UpdateAPIView):
    queryset = PlatoModel.objects.all()
    serializer_class = PlatoSerializer
    permission_classes = [ IsAuthenticated ]

    def put(self, request:Request, id:str):
        # primero busco si existe ekl plato
        # SELECT * FROM platos WHERE id= ... LIMIT 1;  
        platoEncontrado = PlatoModel.objects.filter(id=id).first()

        if platoEncontrado is None:
            return Response(data={
                'message':'plato no encontrado'
            }, status=status.HTTP_404_NOT_FOUND)
        
        # actualizare el estado de la disponibilidad
        # la nueva disponibilidad sera la anterior al reves
        platoEncontrado.disponibilidad = not platoEncontrado.disponibilidad

        platoEncontrado.save()

        return Response(data={
            'message':'Plato actualizado exitosamente',
            'content': self.serializer_class(instance=platoEncontrado).data
        }, status=status.HTTP_201_CREATED)

class PlatoUpdateApiView(UpdateAPIView):
    queryset = PlatoModel.objects.all()
    serializer_class = PlatoSerializer
    permission_classes = [ IsAuthenticated ]

class VistaProtegidaPlatosApiView(ListAPIView):
    queryset = PlatoModel.objects.all()
    serializer_class = PlatoSerializer
    # Autentication_classes > indica la forma que se utiliara para autenticar, en este caso no necesitamos indicar ningun autentication ya que estamos utilizando la libreria simple-jwt, este seria su valor por defecto que  esta indicadoen el archivo settings.py
    authentication_classes = [JWTAuthentication] # con: from rest_framework_simplejwt.authentication import JWTAuthentication, no es necesario si ya esta el siguiente comando
    # Me permite agregar autenticacion a mis metodos de esta vista generica
    permission_classes = [ SoloAdmin ]

    def get(self, request:Request):
        # request.auth > me devolcera lo que se esta utilizando para la autenticacion (la JWT)
        print('El auth es:', request.auth)
        # request.user > una vez que ya comprobo que el usuario existe y la token es coorecta, ahora en el request.user se almacenara el usuario que esta utilizando esa token (gracias al parametro 'USER_ID_CLAIM')
        print('El user es:', request.user)
        return Response(data={
            'message':'Hola',
            'usuario': {
                'id': request.user.id,
                'correo': request.user.correo
            }
        })

@api_view(http_method_names=['GET'])
def mostrar_usuarios_raw(request):
    with connection.cursor() as cursor:
        # al utilizar un SP, funcion, vista o algoque no se haya definido en los modelos en el ORM, la unica forma de utilizarlo desde el backend es mediante una raw query
        cursor.execute('CALL DevolverTodosLosUsuarios()')
        resultado = cursor.fetchall()
        # print (resultado)
        # ahora mapeariamos el resultado (se recomienda utilizar un serializador pero no un ModelSerializer puesto que no estamos utilizando ningun modelo)
        for usuario in resultado:
            print(usuario[3]) # nombre

        # este seruia el caso en el cual nosotros queremos utilizar un SP que devuelve cierta informacion con un parametro OUT
        cursor.execute("CALL DevolverUsuarioSegunTipo('ADMIN', @usuarioId)")
        cursor.execute('SELECT @usuarioId')
        # fetchone(): devolvera la primera fila de todo el resultado
        # fetchall(): devolvera todos los registros
        # fetchmany(registros) > devolver la cantidad de registros indicada
        resultado2 = cursor.fetchone()
        print(resultado2)
        return Response(data={
            'message':'Procedimiento almacenado ejecutado exitosamente',
            'content': {
                'admin': resultado2[0]
            }
        })
