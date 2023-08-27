"""
1o Ingresar numero
2o Si hay numero, ingrese operacion
3o Ingrese otro numero
4o Mostrar resultado y guardar como primer numero
"""
print("Bienvenido a la calculadora")
print("Para salir escriba salir")
n1 = int(input("Ingrese numero: "))
comando = ""
while comando != "salir":
    comando = input("Ingrese un comando")
    if (comando == "salir"):
        break
    n2 = int(input("Ingrese el segundo número"))
    if comando == "suma":
        n1 = n1 + n2
        print(n1)
    elif comando == "resta":
        n1 = n1 - n2
        print(n1)
    elif comando == "multi":
        n1 = n1 * n2
        print(n1)
    elif comando == "div":
        n1 = n1 / n2
        print(n1)

print("Saliendo de la calculadora")
