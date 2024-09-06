# classes


class MyPerson:
    pass


print(MyPerson)


class MyPersonaa:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname  # pro.publica
        self._name = name  # pro.privada

    def caminar(self):
        print(f"{self.name} esta caminando")


person = MyPersonaa("yonathan", "muset")
print(f"{person.name} {person.surname}")
person.caminar()
