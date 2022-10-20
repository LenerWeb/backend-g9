pag_hora = int(input("Ingrese el Pago Por Hora:"))
hor_trab = int(input("Ingrese Horas Trabajadas:"))
if hor_trab>35:
     totalhe = hor_trab - 35
     phe = totalhe * 1.5
else:
     phe = 0
sueldo = (hor_trab * pag_hora) + phe
if sueldo >20000:
    imp = sueldo * 0.20
else:
    imp = 0

neto = sueldo + imp
print("El Neto a percibir es",neto)    
