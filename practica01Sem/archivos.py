import csv

def mostrarInformacion():
    csvArchivo = open('juntaVecinos.csv', 'r', encoding='utf-8')
    entrada = csv.reader(csvArchivo) #Leer todos los registros
    for reg in entrada:
        print(reg)
    csvArchivo.close()
    del csvArchivo

mostrarInformacion()



