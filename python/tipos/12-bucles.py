# bucle,looops

# while,si se cumple la condicion
mi_condicion = 0
while mi_condicion < 10:
    print(mi_condicion)
    mi_condicion += 2
if mi_condicion == 10:
    print("es el limite perra")

while mi_condicion < 20:
    mi_condicion += 1
    if mi_condicion == 15:
        print("hasta 15")
        break


# for

mi_list = [35, 24, 65, 52, 30, 30, 17]
for ele in mi_list:
    print(ele)


mi_tupla = (24, 1.85, "yonathan", "muset")
for ele in mi_tupla:
    print(ele)

mi_otro_set = {"yonathan", "muset", 25}
for ele in mi_otro_set:
    print(ele)

mi_otro_dicc = {
    "nombre": "yonathan",
    "apellido": "muset",
    "edad": 25,
    "lenguajes": {"javascript", "python", "html%css"},
    1: 1.85,
}
for ele in mi_otro_dicc:
    print(ele)
