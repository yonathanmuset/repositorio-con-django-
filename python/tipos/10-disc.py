# diccionarios
# clave valor
mi_dicc = dict()
mi_otro_dicc = {
    "nombre": "yonathan",
    "apellido": "muset",
    "edad": 25,
    "lenguajes": {"javascript", "python", "html%css"},
    1: 1.85,
}
print(len(mi_otro_dicc))
print(mi_otro_dicc["lenguajes"])
mi_otro_dicc["nombre"] = "yona"
mi_otro_dicc["novia"] = "valeria"

print(mi_otro_dicc.items())
print(mi_otro_dicc.keys())
print(mi_otro_dicc.values())
