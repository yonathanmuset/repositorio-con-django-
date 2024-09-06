###challenges###
# el famoso fizz buzz
""" * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""


def fizzbuzz():
    for index in range(1, 101):
        if index % 3 == 0 and index % 5 == 0:
            print("fiizbuz")
        elif index % 3 == 0:
            print("fizz")
        elif index % 5 == 0:
            print("buzz")
        else:
            print(index)


fizzbuzz()

# ES UN ANAGRAMA
"""Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama."""


def anagrama(palabra1, palabra2):
    if palabra1.lower() == palabra2.lower():
        return False
    return sorted(palabra1.lower()) == sorted(palabra2.lower())


print(anagrama("Amor", "Amor"))


# fibonacci
"""
DIFÍCIL | Publicación: 10/01/22 | Resolución: 17/01/22
/*
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
 */
Ver el Ejercicio en GitHub
Reto #1: ¿ES UN ANAGRAMA?"""


def fibonacci():
    pret = 0
    next = 1
    while next <= 50:
        fibb = pret + next
        pret = next
        next = fibb
        # print(index)
        print(fibb)


fibonacci()
# es primo
"""* Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100."""


def esprimo():
    for number in range(1, 101):
        if number >= 2:
            is_divisible = False
            for index in range(2, number):
                if number % index == 0:
                    is_divisible = True
                    break

            if not is_divisible:
                print(number)


esprimo()


# invirtiendo cadenas


def reverse(texto):
    return texto[::-1]


print(reverse("hola mundo"))
