# file handling

import os

# txt file
txt_file = open("intermedio/my-fyle.txt", "r+")  # leer y escriibir
# print(txt_file.read())
print(txt_file.readline())
print(txt_file.readlines())
txt_file.write("\n y tambien me gusta el javscript")


# json
import json

json_file = open("intermedio/my-fyle.json", "w+")

json_test = {
    "nombre": "yonathan",
    "apellido": "muset",
    "edad": 25,
}

json.dump(json_test, json_file, indent=2)

# csv file
import csv

# xml file
import xml

csv_file = open("intermedio/my-fyle.csv", "w+")

json_test = {
    "nombre": "yonathan",
    "apellido": "muset",
    "edad": 25,
}
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["nombre", "apellido", "edad"])
csv_writer.writerow(["yonathan", "muset", 25])
csv_file.close()
