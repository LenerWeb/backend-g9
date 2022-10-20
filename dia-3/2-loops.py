numeros = [4, 5, 8, 3, 2, 1, 9]

for numero in numeros:
   # print(numero)
   pass

alumnos = ['Jose', 'Miguel', 'Raul', 'Eduardo', 'Jorge']

for i, alumno in enumerate(alumnos):
   if i == 2:
      # pass pasa el array
      # break rompe en el 2, ya no sigue
      continue  # se salta el 2 y cintinua
   #print(i, alumno)

for numero in range(10):
   print(numero)

palabra = 'hola mundo'
for letra in palabra:
   print(letra)
