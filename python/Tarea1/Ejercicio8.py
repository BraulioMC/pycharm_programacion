'''
Dada la cadena "  esto es un ejemplo de una cadena de ejemplo "
'''


#   a) Guardala en una variables llamada cadena

cadena = "  esto es un ejemplo de una cadena de ejemplo "

print("a)" , cadena)

#   b) Cuántos caracteres tiene?

print("b)" , len(cadena))

#   c) Elimina los espacios en blanco al principio y al final. Cuántos caracteres tiene ahora

print("c)" , len(cadena.strip()))

#   d) Divídela en palablas. Cuantas tiene

print("d)" , len(cadena.split()))

#   e) Cámbiala de forma que la frase empiece por mayusculas

print("e)" , cadena.title())

#   f) Extrae la subcadena "cadena de ejemplo" y guardala en una variable llamada cola
'''
 Buscamos la posicion de la palabra cadena y mostramos la segunda parte
 Es como hacer un 'cut -d f1' en bash
'''
print("f)" ,
      cadena[cadena.find("cadena"):] ,
      "\n" ,
      "  La posicion de la palabra es: " ,
      cadena.find("cadena")
)

cola = cadena[cadena.find("cadena"):]

#   g) Reemplaza en cola "ejemplo" por "muestra""

print("g)" , cola.replace("ejemplo" , "muestra" , 1))

#   h) Extrae la subcadena "Esto es un ejemplo de una" y guárdala en una variable llamada principio

principio = cadena[:cadena.find("cadena")]
print("h)" , principio)

#   i) Crea una variable frase que sea el resultado de concatenar principio y cola e imprimela

frase = principio + cola

print("i)" , frase)




