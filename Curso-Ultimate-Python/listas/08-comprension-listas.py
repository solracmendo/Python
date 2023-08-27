usuarios = [[4, "Jose"], [1, "Felipe"], [5, "Pulga"]]

# nombres = []
# for usuario in usuarios:
#     nombres.append(usuario[1])
# print(nombres)

nombres = [usuario[1] for usuario in usuarios]  # En una lista
indices = [usuario[0] for usuario in usuarios]

# filtrar
nombres = [usuario for usuario in usuarios if usuario[0] > 2]
print(nombres)
print(indices)
