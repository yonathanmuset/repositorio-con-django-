# expresiones regulares
import re

my_string = "esta es la leccion numero 7:expresiones regulares"
my_other_string = "esta no es la ccion numero 6:ficheross"

print(re.match("esta es la leccion", my_string))  # empeza a buscar desde el pincipio
print(re.match("esta es la leccion", my_other_string))


match = re.match("Esta no es la lección", my_other_string)
print(match)
# search
search = re.search("leccion", my_string, re.I)
print(search)
# findalll
findall = re.findall("leccion", my_string, re.I)
print(findall)

# split
print(re.split(":", my_string))

# sub
print(re.sub("leccion", "comida", my_string))
# patterns
patter = r"[lL]eccion"
print(re.findall(patter, my_string))
