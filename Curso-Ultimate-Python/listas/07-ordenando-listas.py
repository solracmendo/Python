numeros = [2, 3, 4, 5, 34, 23, 65, 1]
numeros.sort(reverse=True)
numeros2 = sorted(numeros)  # Esto devuelve una NUEVA lista
print(numeros)
print(numeros2)

usuarios = [[4, "Jose"], [1, "Felipe"], [5, "Pulga"]]
# usuarios.sort()  # Solo ordena por el primer elemento (si es ordenable) a sort tenemos que indicarle en base a qué


def ordena(elemento):
    return elemento[1]


usuarios.sort(key=ordena)
# Expresion lambda, si solo la usas aqui, utiliza una funcion lambda
usuarios.sort(key=lambda el: el[1])
print(usuarios)
