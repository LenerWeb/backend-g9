class Cursos:
    def __init__(self, nombre, precio, dura):
        self.nombre = nombre
        self.precio = precio
        self.dura = dura
    
    def imprimirDetalle (self):
        print(self.nombre, self.precio, self.dura)

    def mensajeCosto (self):
        if self.precio > 350:
            print("El curso es poco caro")
        else:
            print("El curso es aceptable")

curso1= Cursos("Python", 200, "1mes")
curso2= Cursos("Django", 300, "3mes")
curso3= Cursos("Flask", 400, "2mes")

curso1.imprimirDetalle()
curso2.imprimirDetalle()
curso3.imprimirDetalle()

curso1.mensajeCosto()
curso2.mensajeCosto()
curso3.mensajeCosto()
