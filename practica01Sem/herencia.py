class vehiculo:
    def __init__(self, marca, color):
        self.m = marca
        self.n = color

    def mensaje(self):
        if self.m == "Toyota":
            print("marca recomendable")
        else:
            print("marca a evaluar")

class Auto(vehiculo):
    def __init__(self, precio):
        self.pre = precio

objeto1 = Auto(8000)
objeto1.m ="Toyota"
objeto1.mensaje()
