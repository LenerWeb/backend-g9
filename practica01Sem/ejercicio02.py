"""Crear un programa que dados 10 números enteros que se ingresan por teclado, 
calcular cuántos de ellos son pares, cuánto suman ellos y el promedio de los mismos"""
cp=0
sum =0
for x in range(1,11):
    num = int(input("Ingrese Numero:"))
    if num % 2 :
        cp = cp + 1
        sum = sum + num
        prom = sum / cp

print("Cantidad de Pares",cp)
print("La Suma de Pares",sum)
print("El Promedio",prom)