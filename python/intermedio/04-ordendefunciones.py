# funciones de orden superior


def sumauno(value):
    return value + 1


def sumatodos(primervalor, segundovalor):
    return sumauno(primervalor + segundovalor)


print(sumatodos(2, 2))


# closures
def funcion1(value1):
    def funcion2(value2):
        return value1 + 10 + value2

    return funcion2


clousure = funcion1(5)
print(clousure(1))


# funcion de orden superior del lenguaje
numbers = [2, 10, 22, 15]


def multiplicar(number):
    return number * 2


print(list(map(multiplicar, numbers)))


# filtre
def filtree(number):
    if number > 10:
        return True
    return False


print(list(filter(filtree, numbers)))
