'''
    Diseña un programa que nos diga si una cadena es palíndromo o no. Una cadena
    es palíndromo si se lee igual de izquierda a derecha que de derecha a izquierda. Por
    ejemplo, las cadenas “ana”, “Ana” y “Oí lo de mamá: me dolió” son palíndromos.
    Ten en cuenta que en la frase podría haber diferentes signos de puntuación y que
    Python distingue entre mayúsculas y minúsculas. El programa no debería distinguir
    tampoco entre una vocal con tilde o sin ella

    PISTA:
    Recuerda que la clase String dispone de métodos para hacer búsquedas, reemplazos y
    diferentes comprobaciones sobre el contenido de las cadenas de caracteres
'''

frase = input("Introduce el palíndromo: ")

procesada = str.maketrans("áéíóúäëïöüÁÉÍÓÚÄËÏÖÜ.,;!?¿:¡", "aeiouaeiouAEIOUAEIOU        ")
frase1 = frase.translate(procesada)  # Cambia en frase lo que se le indicó en maketrans
frase1 = frase1.lower()              # Todo en minusculas
frase1 = "".join(frase1.split())     # Une con un espacio " ".join las palabras que se le pasen


if frase1 == frase1[::-1]:
    print(frase, " - és un palíndromo")
else:
    print(frase, " - no és un palíndromo")


