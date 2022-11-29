from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.request import Request

class SoloAdmin(BasePermission):
    # si queremos cambiar el mensaje de respuesta cuando falle la validacion:
    message = 'Tu no tienes los permisos necesarios'
        
    def has_permission(self, request:Request, view):
        # View > es la vista a la cual se esta tratando de acceder
        # SAFE_METHODS > es un listado en ekl cual me muestra los metodos seguros (los que no afectan la modificacion de datos (GET, OPTIONS, HEAD))
        print(SAFE_METHODS)
        if request.method in SAFE_METHODS:
            # si el metodo que esta utilizando para acceder es GET | OPTIONS | HEAD
            return True
        
        print(request.user)
        print(view)

        if request.user.tipoUsuario == 'ADMIN':
            return True
        else:
            return False
        