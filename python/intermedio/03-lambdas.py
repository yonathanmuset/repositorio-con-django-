# lambdas

var = lambda primer_valor, segundo_valor: primer_valor + segundo_valor
print(var(5, 5))
mul_var = lambda primer_valor, segundo_valor: primer_valor * segundo_valor
print(mul_var(5, 5))


def sum_var(value):
    return lambda primer_valor, segundo_valor: primer_valor + segundo_valor + value


print(sum_var(5)(4, 5))
