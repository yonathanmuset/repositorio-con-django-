# sets
# un sets no es una estructura ordenada
# un sets no admite repeticiones
mi_set = set()
mi_otro_set = {"yonathan", "muset", 25}  # es un diccionario
mi_otro_set.add("yona")
print(mi_otro_set)
print(type(mi_otro_set))
print(len(mi_otro_set))
print("yoni" in mi_otro_set)
print("yona" in mi_otro_set)
mi_otro_set.remove("yona")
print(mi_otro_set)
lenaguajes = {"python", "javascript", "html&css"}
mi_nuevo_set = mi_otro_set.union(lenaguajes)
print(mi_nuevo_set)
