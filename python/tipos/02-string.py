nombre_curso = "ultimate python"
descripsion_curso = """
ultimate pithon,
este curso completa todos los detalles que necesitas para encontrar un trabajo de programador
"""
# /n salto de linea
print(nombre_curso, descripsion_curso)
print(len(nombre_curso))
print(nombre_curso[0])
print(nombre_curso[0:8])
print(nombre_curso[9:])
print(nombre_curso[:8])
print(nombre_curso[:])


# tab
my_tab_string = "\\teste es un string con tabulacion \\n escapado"
print(my_tab_string)

name, surname, edad = "yonathan", "muset", 24
print("mi nombre es %s %s y mi edad es %d" % (name, surname, edad))
print("mi nombre es {} {} y mi edad es {}".format(name, surname, edad))
print(f"mi nombre es {name} {surname} y mi edad es {edad}")


lenguaje = "python"
(
    a,
    b,
    c,
    d,
    e,
    f,
) = lenguaje
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# reverse
reverse = lenguaje[::-1]
print(reverse)
