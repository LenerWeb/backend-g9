# funciones deficnidas por el usuario

def miFuncion():
    print('Hola mundo')


def suma(a, b, c):
    return a + b + c


print(suma(3, 5, 8))


def comprobarEdad(edad):

    #    if (edad >= 18) :
    return 'Eres mayor de edad'
#    else:
#        return 'no eres mayor de edad, no puedes ingresar'

# print(comprobarEdad(int(input("Ingresa tu edad "))))


alumnos = ['Eduardo', 'Pepe', 'Jose', 'Miguel', 'Julia', 'Raul']


def buscarNombre():
    if 'Eduardo' in alumnos:
        return False
    return True


print(buscarNombre())

# ingresar una lista de 4 nombres por consola y que una funcion haga la busqueda del ultimo nombre

# uso del input

nombres = []

primer_nombre = input('Ingrese el primer nombre: ')
segundo_nombre = input('Ingrese el primer nombre: ')
tercer_nombre = input('Ingrese el primer nombre: ')
cuarto_nombre = input('Ingrese el primer nombre: ')

nombres.append(primer_nombre)
nombres.append(segundo_nombre)
nombres.append(tercer_nombre)
nombres.append(cuarto_nombre)

nombreBuscar = input('Ingrese el nombre a buscar: ')


def buscarPersona(nombre):

    if nombre in nombres:
        return 'El nombre {} ha sido encontrado {}'.format(nombre, ';)')
    return f'No pudimos encontrar a {nombre}'


# print(buscarPersona(nombreBuscar))
# --------------------------------------------------------------
usuarios = []
usuarios = input('Ingrese 4 nombres separados por comas: ')

nombreBuscar2 = input('Ingrese el nombre a buscar: ')


def buscarPersona2(nombre):

    if nombre in usuarios:
        return 'El nombre {} ha sido encontrado {}'.format(nombre, ';)')
    return f'No pudimos encontrar a {nombre}'


print(buscarPersona2(nombreBuscar2))

# --------------------------------------------

todos_lo_nombres = input('Ingrese 4 nombres separados por comas: ')

nombreBuscar = input('Ingrese el nombre a buscar: ')


def separarNombres(lista_nombres):
    nombres = lista_nombres.split(',')
    print(nombres)
    return nombres


def buscarPersona(nombre):
    array_nombres = separarNombres(todos_lo_nombres)

    if nombre in array_nombres:
        return 'El nombre {} ha sido encontrado {}'.format(nombre, ';)')
    return f'No pudimos encontrar a {nombre}'


print(buscarPersona(nombreBuscar))

# ------------------------------------------------------------
