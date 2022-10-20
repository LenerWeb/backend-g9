#Listas (tiene las mismas funcionalidades que un arreglo en JS array)
#Coleccion de datos ORDENADAS y MODIFICABLES

from __future__ import print_function


nombre = ['Angel', 'Carmen', 'Sofia', 'Adolfo', 'Henry', 'Felipe']

#las listas pueden contener diferrentes tipos de datos
miscelaneo = ['jueves', 13, 'Soleado', False, [1,2,3]]

#podemos acceder a su contenido mediante las posiciones
print(nombre[0])

#longitud = cantidad de elementos que hay en una coleccion
#posicion = ubicacion de un elemento determinado, que siempre empieza en 0
#len()= devuelve el numero de items de un contenedor, puede der un string y retorna los caracteres o una coleccion de datos y retorna los items
print(len(nombre))
longitud = len(nombre)
print(nombre[longitud-1])

#la ultima posicion de la lista
print(nombre[-1])
print(nombre[-2])
#desde la posicion 1 hasta manor que 4
print(nombre[1:4])
#desde la posicion 1 hasta el final
print(nombre[1:])
#desde el inicio hasta menor quie 5
print(nombre[:5])

#copiar el contenido de un arreglo (colocando en otra posicion de memoria)
print(nombre[:])
print(id(nombre))
alumnos_lima = nombre #agregando [:] al final de nombre tienen dos ubicaciones diferentes
print(id(alumnos_lima))
#si cambiamos el contenido  de una posicion de memoria gregamos o eliminamos el contenido se vera reflejado tanto en la variable original como en la variable huesped
nombre[0]='Felix'
#si cambiamos el contenido de la variable ahi recien la variable huesped 'alumnos_lima' cambiara su ubicacion en la memoria
nombre = 'hola mundo'
print(alumnos_lima)

print ([1,2,3]+[4,5,6])
#mostrar solo a Angel y Carmen, luego mostrar a Adolfo, henry y Felipe y concatenar las dos listas
nombre = ['Angel', 'Carmen', 'Sofia', 'Adolfo', 'Henry', 'Felipe']
print(nombre[:2] + nombre[3:])

#agregar un nuevo elemento a la lista
nombre.append('Juan Pablo')

print(nombre)

#eliminar segun el indice
alumno_eliminado = nombre.pop(0)
print(alumno_eliminado)
print(nombre)

#remove(valor)> si no existe el valor emitira un error, si si existe, lo elimina, no devuelve nada
alumno_eliminado_2= nombre.remove('Adolfo')
print(nombre)
print (alumno_eliminado_2)

#elimina la posicion ( muy parecida al pop pero no devuelve nada)
del nombre[0]
print(nombre)

#limpia porcompleto la lista
nombre.clear()
print(nombre)

#para mas informacion: https://docs.python.org/3/tutorial/datastructures.html


#---------------------------------------------------
#Tuplas
#son ordenadas pero no se pueden modificar ( una vez definidas nos e puede alterar)

cursos = ('backend','frontend')
mix= (1, 80.2, False, 'Eduardo', (1,2,3))

print(cursos[0])

print(cursos[:1])
#ni agregar
#cursos.append('desing')

#ni editar
#cursos[0]='mobile'

#ni eliminar
#del cursos[0]
print(cursos)
print (len(cursos))

#-----------------------------------------
#conjunto (Set)
#coleccion de datos DESORDENADA una vez creada ya no se puyede accedeer mediante sus posiciones

primos = {19,1,3,11,5,7,13,17}
print(primos)
estaciones = {'Verano','Otoño','Primavera','Invierno'}
print(estaciones)
print(17 in primos)
#se puede agregar los elementos a un set
primos.add(23)
print(primos)

#se puede eliminar
primos.pop()
print(primos)

#del primos[2] #no se puede eliminar definitivamente por popsicion

#----------------------------------------------------------
#DICCIONARIOS
#Una coleccion ordenada por llaves (no por indice) y editable
persona = {
    'nombre':'Eduardo',
    'apellido': 'Suarez',
    'correo':'ederrivero@hotmail.com',
    'telefono': '+51985476584'
}

print(persona)
print(persona['nombre'])
#tratara de devolver el contenido de esa llave, si no existe retornara None o lo que se defina en el segundo paraametro
print(persona.get('direccion','No hay'))

#devuelve una lista con todas las llaves
print(persona.keys())

#devuelve una lista con todos los valores
print(persona.values())

persona['nombre'] = 'luis'
persona['direccion'] = 'calle los ruiseñores 1740'
#persona.get('direccion')='calle los ruiseñores1740'
print(persona)

#remueve el valor de esallave y la elimina y opcionalmente podemos almacenar el valor en otra variable
correo_eliminado = persona.pop('correo')
print(persona)
print(correo_eliminado)

#para mas informacion: https://docs.python.org/3/tutorial/datastructures.html#dictionaries


