# encapsulamiento > es el metodo de 'ocultar' cierta informacion sensiuble o que no debe ser manipulada desde fuera de la clade ( atributo o metodo privado)

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        # _ _ atributo > estaremos indicando que sera privado y por ende no puede ser accedido desde fuera de la clase PRIVADO
        self.__ventas = []
        # _atributo > atributo PROTEGIDO en Python mas que todo funciona para cuando queremos utilizar este atributo con herencia
        self._precio_mayorista = 100

    def verificar_stock(self):
        # si hay ventas modificar la informacion del atributo contenido en cantidad
        if (self.cantidad <= 1):
            print('No hay stock')
        else:
            text_stock = 'Hay en stock {}' .format(self.cantidad)
            print(text_stock)

    def generar_venta(self, fecha, cliente, cantidad):
        # antes de agregar la venta validar si aun tenemos en stock para dicha venta
        # TODO: primero ver si tenemos ventas, si hay iteramos esas ventas y sacamos cuanto de cantidad hemos vendido. lugo ver si ese numero es menor que la cantidad total  (el atributo cantidad) si es mayor indicar que ya hemos sobregirado las ventas. Por ultimo a esa cantidad de productos vendidos sumar cantidad entrante y ver si es menor o igual que la cantidad total, si lo es, entonces generar la venta, caso contrario, no permitir la venta e indicar que no hay stock suficiente. Si es que no hay el saldo suficiente indicar cuanto es lo que tenemos para vender.
        venta = {
            'fecha': fecha,
            'cliente': cliente,
            'cantidad': cantidad
        }
        if cantidad <= self.cantidad:
            self.__ventas.append(venta)
            self.cantidad = self.cantidad - cantidad

            anuncio = 'Venta registrada exitosamente. Stock restante: {}' .format(self.cantidad)
            print(anuncio)

        else:
            deficit = cantidad-self.cantidad  
            text_venta = 'Quedan en stock {} unidades, No se puede hacer ventas, faltan {} unidades' .format(self.cantidad, deficit)
            print(text_venta)
            #print('Venta registrada exitosamente')

    def mostrar_ventas(self):
        # retornar las ventas registradas de ese producto
        return self.__ventas


detergente = Producto(nombre='Detergente Sapito', precio=4.50, cantidad=55)
detergente.nombre = 'Detergente Lechuga'
print(detergente.nombre)
detergente.verificar_stock()
#detergente.editar_stock()

detergente.generar_venta(fecha='2022-10-19', cliente='Eduardo de Rivero', cantidad=10)
detergente.generar_venta(fecha='2022-10-29', cliente='Julissa Perez', cantidad=30)
detergente.generar_venta(fecha='2022-10-30', cliente='Franco Portugal', cantidad=20)
detergente.generar_venta(fecha='2022-11-02', cliente='Michelle Ordoñez', cantidad=15)
# print(detergente.__ventas)


print(detergente.mostrar_ventas())
