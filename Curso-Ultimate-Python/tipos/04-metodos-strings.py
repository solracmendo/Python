animal = ' CHanchito feliz '
print(animal.lower())  # Pasa a minuscula
print(animal.upper())  # Pasa a mayuscula
print(animal.capitalize())  # Pone a mayuscula la primera letra
print(animal.title())  # Pone a mayuscula la primera de cada palabra
print(animal.strip())  # Elimina espacios por izq y der
print(animal.strip().capitalize())  # Necesario
print(animal.lstrip())  # Strip por la izq
print(animal.find("CP"))  # Indice de la cadena pasada
print(animal.replace("CH", "j"))  # Reemplaza lo de la izq por lo de la der
print("45" in animal)  # True o False dependiendo de si esta (booleano)
print("45" not in animal)  # True o False dependiendo de si NO esta (booleano)
