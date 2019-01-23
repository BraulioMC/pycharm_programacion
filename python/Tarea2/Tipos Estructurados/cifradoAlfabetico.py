'''
5.
Dentro de los cifrados de sustitución monoalfabética, existe una variante del cifrado César
consistente en la introducción de una clave, sin caracteres repetidos, a partir de la cual se
creará el alfabeto de cifrado por sustitución.
Para crear el alfabeto de cifrado, hacemos coincidir las letras del alfabeto con la clave,
creando las parejas de sustitución. Cuando lleguemos al final de la clave, vamos añadiendo
en orden el resto de los caracteres del alfabeto que no hayan sido usados.
Por ejemplo, supongamos que la clave es: ZAFIRO . La hacemos coincidir con los primeros
caracteres del alfabeto:
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
Z A F I R O
A continuación, seguimos añadiendo en orden los restantes caracteres no usados:
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
Z A F I R O B C D E G H J K L M N P Q S T U V W X Y
Ahora ya podemos usar esa tabla tanto para cifrar como descifrar:
“ESTO ES UN MENSAJE SECRETO” <<<<< >>>>> “ RQSL RQ TK JRKQZER QRFPRSL ”
Crea un programa que permita cifrar y descifrar mensajes utilizando este sistema.
Debes tener en cuenta que:
● Puedes implementar la tabla de cifrado de diferentes maneras:
1. empleando dos listas, una para cada alfabeto
2. almacenando la tabla de cifrado en un único diccionario
3. creando dos diccionarios, uno para cifrar y otro para descifrar
● Debes comprobar que la clave introducida no contenga la letra Ñ y no contenga
letras repetidas.
● Para eliminar las tildes, tanto del mensaje como de la clave, puedes hacer uso de la
función elimina_tildes del módulo mod_u05
● Antes de cifrar/descifrar debes comprobar que se ha inicializado la tabla de cifrado
según la clave proporcionada
'''
import time

var_klave_dic = {}
var_klave_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                  "U", "V", "W", "X", "Y", "Z"]

var_klave = "ZAFIRO"
var_klave_list_len = len(var_klave_list)
var_klave_len = len(var_klave)
var_set_klave = set(var_klave)

for i in range (0, var_klave_len):
    key = var_klave_list[i]
    tmp = var_klave[i]
    var_klave_dic.update({key:tmp})

var_klave_set = set(var_klave_list)

for i in var_klave:
    var_klave_set.discard(i)

var_lista = list(var_klave_set)
var_lista = ''.join((sorted(var_lista)))
count = 0

for i in range(var_klave_len, var_klave_list_len):
    key = var_klave_list[i]
    valor = var_lista[count]
    var_klave_dic.update({key:valor})
    count += 1




print(var_klave_dic)

time.sleep(2)