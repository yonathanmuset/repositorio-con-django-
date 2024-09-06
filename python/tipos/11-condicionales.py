# condicionales,m elif
my_condicion = False
if my_condicion:  # es evidente que tiene que ser true
    print("Se ejecuta la condicion")

print("la ejecucion continua")
my_condicion2 = 9
if my_condicion2 == 10:
    print(" es iguaal a 10")
elif my_condicion2 < 10:
    print("es menor a 10")
else:
    print("no es igual a 10")


mi_cadena = ""
if mi_cadena:
    print("tiene texto")

if not mi_cadena:
    print("no tiene texto")
