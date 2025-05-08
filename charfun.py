import string
import unicodedata

def esPalindromo(cadena):
    """
    Con esto lo que realizaremos es probar si la cadena de texto que añadamos es palindromo o no.
    A continuación, crearemos unas cadenas que ignorarán los espacios, la puntuación y la diferencia entre mayúsculas y minúsculas.
    """
    # Normalizar la cadena para eliminar acentos. 
    cadena_normalizada = unicodedata.normalize('NFD', cadena)
    cadena_sin_acentos = ''.join(char.lower() for char in cadena_normalizada if unicodedata.category(char) != 'Mn')

    # Se ignorarán los espacios, la puntuación y las palabras serán todas minúsculas. 
    cadena_texto = ''.join(char.lower() for char in cadena_sin_acentos if char.isalnum())
    
    # Se comprobará si la cadena de texto es igual tanto al derecho como al revés.
    return cadena_texto == cadena_texto[::-1]

if __name__ == "__main__":
    # Introducimos la frase la cual será determinada como palíndroma o no.
    frase = "12345678"
    if esPalindromo(frase):
        print("La frase es un palíndromo.")
    else:
        print("La frase no es un palíndromo.")

