mascotas = ["Pelusa", "Pulga", "Felipe", "Chanchito", "Wolfgang", "Pulga"]

mascotas.insert(1, "JODSJDI")
mascotas.append("JIJDIJS")
mascotas.remove("Pulga")  # Solo elimina el primero que encuentre
mascotas.pop()  # Elimina el ultimo
mascotas.pop(1)  # Saca el elemento situado en ese indice
del mascotas[3]  # Elimina el elemento situado en ese indice
mascotas.clear()  # Limpia COMPLETAMENTE la lista
print(mascotas)
