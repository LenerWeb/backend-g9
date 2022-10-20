#el try siempre va de la mano con el except, no pueden ir separados
from multiprocessing.sharedctypes import Value


try:
    #si no se emite ningun error dentro del try, JAMAS ingresara al except
    #print(10/0) #CRASHEE

    int('a')
    
except ZeroDivisionError:
    # aca ingresara si el error es de tipo ZeroDivisionError
    print('Hubo un error al dividir entre cero')

except ValueError:
    # aca entrara si hubo un error de conversion a entero
    print('Error al convertir el numero')

except Exception as error:
    # aca entrara si el error es otro generico
    # .args> es el atributo de toda instancia de excepcion que me devolvera el porque se dio ese error (argumentos)
    print(error.args)
    print('Hubo un error al dividir entre cero')

print('Yo no soy un error')

try:
    #ARGS son los argumentos que nosotros indicamos o que recibimos cuando se de un error, en este atributo se podran obtener todos los argumentos del porque se dio ese error
    raise Exception('eres menor de erad', 'no eres peruano') # throw new Error() > JS
except Exception as error:
    print(error.args)

#---------------------------------------
try:
    resultado = 5/1
    raise Exception('Error desconocido') # si se comenta entonces se habilita el ELSE   

except Exception as error:
    print(error.args)

else:
    #en el caso que el codigo se ejecutae sin nuingun error (siningresar akl except)
    print('la operacion se realizo exitosamente')

finally:
    # ingresa si la ejecusion estuvo bien o si eingreso al except
    print('si la operacion estuvo bien o mal igual se ejecuta')

#EJERCICIO
#RECIBIR PO EL TECLADO UN NUMERO
#Luego tratar de convertir ese numero a un entero (si no se puede indicar que el valor es incorrecto). sumar 10 + ese numero ingresado y devolver

numero = input('ingresa un numero')

try:
    numeroEntero = int(numero)
except ValueError:
    print('el valor ingresado es incorrecto')
else :
    print (numeroEntero + 10)

