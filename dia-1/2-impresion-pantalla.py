correo = 'lener20@hotmail.com'
estatura = 1.65
print(correo)

#juntar dos textos, al momento de poner la coma se agrega un espacio al imprimir
print('el correo del usuario es',correo)

print('el correo del usuario es '+correo)

#concatenacion por el mas (+)solo se hace entre string
print('la estatura del usuario es ',estatura)

#parsear > convertir un tipo de dato a otro
print('la estatura del usuario es '+str(estatura))

tipo_calculo = "raiz cuadrada de dos"
valor = 2**0.5
print('el resultado de %s es %f'%(tipo_calculo,valor))

nom=""
sue=0
bon=0
nom=input("ingrese su nombre: ")
sue=int(input("ingrese su sueldo: "))
tser=int(input("Tiempo de servicio: "))

if tser>=1 and tser<=3:
    bon = sue*0.02
    #print("la bonificacion de: "+ nom + " es: " +str(bon))
elif tser >= 4 and tser <= 5:
    bon = sue*0.03
    #print("la bonificacion de: "+ nom + " es: " +str(bon))
else:
    bon = sue*0.04
print("la bonificacion de: "+ nom + " es: " +str(bon))
