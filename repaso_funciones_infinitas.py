
def prueba(**argumentos):
    print(argumentos)

prueba(nombre='eduardo', apellido='de rivero')

persona = {
    'nombre':'eduardo',
    'apellido':'de rivero'
}

prueba(persona = persona)

# Cuando nosotros en una funciona pasamos un diccionario pero con doble asterisco antes (**) significa que sacara las llaves (keys) y lo colocara como parametro de la funcion y sus valores como los valores de esos parametros
prueba(**persona)
prueba(nombre=persona['nombre'], apellido=persona['apellido'])

# si usamos una funcion con parametros definidos entonces tenemos que indicar en el diccionario ESE MISMO NOMBRE DE PARAMETROS ya que si es diferente, arrojara un error
def saludar(nombre, apellido):
    print(nombre)

usuario = {
    'nombre':'eduardo',
    'apellido':'de rivero'
}

saludar(**usuario)

saludar(**usuario2)
saludar(nombrecito=saludar)