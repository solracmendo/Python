# and or not

gas = True
encendido = False
edad = 18

if gas and (encendido and edad > 34):
    print("Puedes avanzar")

if gas or encendido:
    print("Puedes avanzar")

if not gas:
    print("Puedes avanzar")
