# Aca definiremos todas las rutas que tendra accesoi nuestra aplicacion
# listado de los anexos de esta aplicacion
from django.urls import path
from .views import saludar, parametros, PruebaApiView, DepartamentosApiView, DepartamentoApiView

# Tenemos que crear esta variable pero no se puede llamar de otra manera
urlpatterns = [
    # todas la rutas no pueden empezar con un '/' siempre al final para POST, GET es opcional
    path('inicio/', saludar),
    path('parametros/<str:nombre>', parametros),
    # el metodo as_view convierte la clase en una vista para que pueda ser consumida por Django
    path('prueba/', PruebaApiView.as_view()),
    path('departamentos/', DepartamentosApiView.as_view()),
    path('departamento/<int:pk>', DepartamentoApiView.as_view()),
    path()
]