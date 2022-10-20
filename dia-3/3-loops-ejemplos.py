alumnos = [
    {
        "id":1,
        "nombre": "Eduardo",
        "dni": 75989642,
        "status": True
    },
    {
        "id":2,
        "nombre": "Jorge",
        "dni": 75989642,
        "status": True
    },
    {
        "id":3,
        "nombre": "Raul",
        "dni": 75989642,
        "status": True
    },
    {
        "id":4,
        "nombre": "Miguel",
        "dni": 75989642,
        "status": False
    },
    {
        "id":5,
        "nombre": "Jose",
        "dni": 75989642,
        "status": False
    }
]

#Extraer nombre solo si el alumno esta activo
def extraerNombre(lista_alumnos):
    for alumno in lista_alumnos:
        if alumno['status'] == True:
            print(alumno['nombre'])
        else:
            pass
#extraerNombre(alumnos)

#---------------------------------------------------------
alumnos_activos = []
def obtenerAlumnosActivos(lista_alumnos):
    for alumno in lista_alumnos:
        if alumno['status'] == True:
            alumnos_activos.append(alumno)
    
#obtenerAlumnosActivos(alumnos)

#print(alumnos_activos)



#funcion que cuente la cantidad de palabras que contenga una frase

def contarPalabras():
    frase = input('ingresa la frase :')
    espacios = 1
    for letra in frase:
        if letra == ' ':
            #espacios = espacios + 1
            espacios += 1
    return espacios

print(contarPalabras())
