numeros = list(range(1, 4))
print(numeros)

primero, *otros = numeros
primero, *otros, ultimo = numeros

print(primero)
print(otros)
print(ultimo)
