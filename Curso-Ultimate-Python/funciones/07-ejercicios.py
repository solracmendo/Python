def es_palindromo(texto):
    indice = 0
    cadenaGirada = texto[::-1]
    texto = texto.replace(" ", "").lower()
    cadenaGirada = cadenaGirada.replace(" ", "").lower()
    for letra in texto:
        if letra != cadenaGirada[indice]:
            return False
        indice += 1
    return True


print(es_palindromo("Amo la paloma"))
