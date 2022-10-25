# Herencia > sirve para reutilizar una clase previamente definida

class Usuario:
    def __init__(self, nombre, apellido, correo):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo

    def mostrar_resumen(self):
        return {
            'nombre': self.nombre,
            'apellido': self.apellido,
            'correo': self.correo
        }

class Alumno(Usuario):
    def __init__(self, nombre, apellido, correo, telefono_emergencia):
        self.telefono_emergencia = telefono_emergencia
        super().__init__(nombre, apellido, correo) #sirve para trabajar con los metodos del padre

    def saludar(self):
        print('hola yo soy la clase alumno y el nombre es {}' .format(self.nombre))

    def mostrar_resumen(self):
        #Polimorfismo > Poli > muchas |morfa > formas, muchas formas o muchos significados, la forma en la cual un metodo depe3ndiendo de donde se utilize va a trabajar de una manera u otra
        resumen = super().mostrar_resumen()
        resumen['telefono_emergencia'] = self.telefono_emergencia
        return resumen
        

usuario01 = Usuario(nombre='Eduardo', apellido='De Rivero', correo='ederiveroman@gmail.com')
usuario02 = Usuario('Alejandra', 'Perez', 'aperez@gmail.com')
usuario03 = Usuario(correo='jdiaz@hotmail.com', apellido='Diaz', nombre='Javier') # no es recomendable

print(usuario01.mostrar_resumen())

alumno01 = Alumno('Juan', 'Martinez', 'jmartinez@yahoo.es', '954863278')
alumno01.saludar()
print(alumno01.mostrar_resumen())
