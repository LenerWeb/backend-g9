from .models import UsuarioModel, PlatoModel
from rest_framework import serializers

class UsuarioSerializer(serializers.ModelSerializer):

    def save(self):
        # es el qeui se encarga de guardar el registro en la base de datos
        # 1.crea la instancia de nuetro nuevo usuario
        # ** sirve para poner los mismos parametros 

        # self.validated_data = {
        #       'nombre':'Eduardo',
        #       'apellido':'de Rivero'
        #       ...
        # }
        # nuevoUsuario = UsuarioModel(
        #     nombre = self.validated_data.get('nombre'), 
        #     apellido = self.validated_data.get('apellido')
        #     )
        
        nuevoUsuario = UsuarioModel(**self.validated_data)

        # 2. genero el hash de la password
        nuevoUsuario.set_password(self.validated_data.get('password'))

        # 3. guardamos el usuario en la base de datos
        nuevoUsuario.save()

        return nuevoUsuario

    class Meta:
        fields = '__all__'
        # exclude = ['correo']
        model = UsuarioModel
        # https://www.django-rest-framework.org/api-guide/serializers/#additional-keyword-arguments
        # Definimos un nuevo atributo llamado extra_kwargs en el cual se reraliza mediante un diccionario y se utiliza  para indicar parametros adicionales a nuestroas columnas
        extra_kwargs = {
            'password': {
                'write_only':True
            },
            'id':{
                'read_only':True
            }
        }
        # con la anterior configurtacion estamos indicando que el atributo password' solamente sera para escribir mas no para devolver (read) y mientras que el 'id' sera solamente para la lectura, mas nunca se podra utilizar para la escritura (write)

class PlatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlatoModel
        fields = '__all__'
        # utilizando el atributo extra_kwargs indicar que solamente la disponibilidad sera de solo lectura
        extra_kwargs = {
            'disponibilidad':{
                'read_only':True
            }
        }