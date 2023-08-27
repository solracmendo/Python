saludo = "Hola global"


def saludar():
    global saludo
    saludo = "Hola mundo"
    print(saludo)


def saludaChanchito():
    saludo = "Hola chanchito"
    print(saludo)


saludar()
saludaChanchito()
print(saludo)
