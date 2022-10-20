#operadores aritmeticos
numero1, numero2 = 10, 50

#suma solo si las dos variables son numericas, si son string se hace una concatenacion.
print (numero1 + numero2)

#resta solamente para numeros
print (numero1 - numero2)
#print("ab"-"bc")

#multiplicacion si se hace multiplicacion de string, entonces se repetira el numero de veces entre unstring y un numero
print (numero1 * numero2)
print ('hola'*5)

#division
print (numero1 / numero2)

#modulo
print (numero1 % numero2)

#cociente
print (numero1 // numero2)

#exponente
print (numero1 ** numero2)

#raiz cuadrada
print (numero1 ** 0.5)

#----------------------------------------------

#OPERADORES DE ASIGNACION
#IGUAL ASIGNAR UN NUEVO VALOR A UNA VARIABLE
numero1 = 100

#Incremento
numero1 += 1 #incrementa el valor del numero1 en una unidad
print(numero1)

#Decremento
numero1 -= 1 #reduce el valor del numero1 en una unidad numero1 = numero1 -1
print(numero1)

#Multiplicador
numero1 *= 2 #multiplica el valor por 2
print(numero1)

#dividendo
numero1 /= 5 #numero1 = numero1 / 5
print(numero1)

#-----------------------------------------------
#OPERADORES DE COMPARACION

#IGUAL QUE, a diferencia de JS no existe el === igual (comparador de tipos de datos)
print(numero1)
print(numero2)
print(numero1 == numero2) #booleano false o true
print(int(40.7))
#int('eduardo')#no se puede convertir tipos de datos irreales
print(type(numero1)==type(numero2))

#MAYOR O MAYORIGUAL
print(10>9.58)
print(10>int('5'))
print(50>=30)

#MENOR O MENORIGUAL
print(50<80)
print(50<=50)
print(50<=30)
#Nota siempre va el simbolo "=" al final, sino python entiende que se esta tratandode una asignacion

print (100>= float("40.24"))

#------------------------------------------
#OPERADORES LOGICOS
#sirve apara conparar varias condiciones
#&& en JS se sua un AND en pythion se usa la palabra AND
#|| en JS se usa un OR, en python se usa la palabra OR
# 
# AND > TODAS las condiciones tienen que ser verdaderas para que todo sea verdadero
eduardo = 30
ronald = 25
henry = 25
carmen = 19
angel = 15

print((angel>eduardo)and (ronald<henry))
print((eduardo>angel)and(carmen<ronald))
#or > AL MENOS una condicion tiene qe ser verdadera pararque todo sea verdadero
print((carmen>ronald) or (eduardo > ronald))


# COMPUERTA LOGICA (operador AND)
# V1 | V2 | R
#  F | F  | F
#  V | F  | F
#  F | V  | F
#  V | V  | V

# COMPUERTA LOGICA (operador OR)
#  V1 |  V2  |  R
#  F  |   F  |  F
#  V  |   F  |  V
#  F  |   V  |  V
#  V  |   V  |  V

#--------------------------------------
#OPERADORES DE CONTENIDO
verduras = ['apio','rocoto','zanahoria']
print('tomate cherry' in verduras)
print('champiñon' not in verduras)

