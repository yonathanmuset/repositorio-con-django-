# manejo de errores

num1, num2 = 5, "3"
# if type(num2) == int:
# print(num1 + num2)
# else:
# print("es un error")
try:
    print(num2 + num2)
    print("no hay errores")
except:  # se ejecuta si hay error
    print("hay un error")
else:  # ser ejecuta si no hay error
    print("la ejecucion trabaja correctamente")
finally:  # ser ejecuta siempre
    print("la ejecucion continua")
