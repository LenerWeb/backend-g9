# Crear una clase llamada Persona en la cual se guarden: nombre, fecha_nacimiento, nacionalidad y dni. Crear otra clase llamada Alumno que va a heredar la clase Persona y ademas va a tener sus atributos: num_seguro, num_emergencia, matriculado (Boolean), el alumno tendra un metodo llamado mostrar_datos y ademas otro metodo llamado matricular en el cual si esta matriculado no se podra matricular, caso contrario, si. Y tambien tener otra clase Profesor que va a tener cta_pago y maestria (str) y el profesor puede mostrar su cta_pago y ademas si tiene maestria al momento de mostrar la cta_pago indicar que se le tiene que agregar 100 soles.

class Persona:
    def __init__(self, nombre, fecha_nac, nacionalidad, dni):
        self.nombre = nombre
        self.fecha_nac = fecha_nac
        self.nacionalidad=nacionalidad
        self.dni = dni

    def mostrar_datos(self):
        return {
            'nombre':self.nombre,
            'fecha_nac':self.fecha_nac,
            'nacionalidad':self.nacionalidad,
            'dni': self.dni
        }

class Alumno(Persona):
    def __init__(self, nombre, fecha_nac, nacionalidad, dni, num_seguro, num_emerg, matricula):
        self.num_seguro = num_seguro
        self.num_emerg = num_emerg
        self.matricula = matricula
        super().__init__(nombre, fecha_nac, nacionalidad, dni)

    def mostrar_datos(self):
        datos = super().mostrar_datos()
        datos['num_seguro'] = self.num_seguro
        datos['num_emerg'] = self.num_emerg
        datos['matricula'] = self.matricula
        return datos

    def matriculado(self):
        if (self.matricula == True):
            print ('{} estas matriculado, no puedes matricularte nuevamente' .format(self.nombre))
        else:
            print ('Felicidades {} si puedes matricularte' .format(self.nombre))
        
class Profesor(Persona):
    def __init__(self, nombre, fecha_nac, nacionalidad, dni, ctta_pago, maestria):
        self.ctta_pago = ctta_pago
        self.maestria = maestria
        super().__init__(nombre, fecha_nac, nacionalidad, dni)

    def mostrar_datos(self):
        profesores = super().mostrar_datos()
        profesores['ctta_pago'] = self.ctta_pago
        profesores['maestria'] = self.maestria
        return profesores
    
    def mostrar_cttapago(self):
        if (self.maestria == True):
            print('Profesor {} usted tiene maestria, se agregara 100 soles mas a su cuenta' .format(self.nombre))
        else:
            print('Profesor {}, su cuenta de pago es {}' .format(self.nombre, self.ctta_pago))

cliente01 = Alumno('Lener', '25-10-2000','peruana', 15487524, 24587, 948756812, True)
cliente02 = Alumno('Jose', '08-03-1998','colombiana', 59781364, 45879, 999588746, False)

profesor01 = Profesor('Pedro', '26-12-1990', 'Mexicana', 45879652, '570-284567-0-02', False)
profesor02 = Profesor('Juan', '12-07-1989', 'Boliviana', 14587965, '570-124583-0-07', True)

#print(cliente02)
print(cliente01.mostrar_datos())
cliente01.matriculado()
print(cliente02.mostrar_datos())
cliente02.matriculado()

print(profesor01.mostrar_datos())
profesor01.mostrar_cttapago()
print(profesor02.mostrar_datos())
profesor02.mostrar_cttapago()
