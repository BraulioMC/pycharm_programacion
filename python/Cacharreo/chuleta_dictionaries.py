'''x =[]
x.append(1)             # Añades lo que quieras a la lista x
x.append("hola mundo")
print(x)
'''

'''
def fun(x):
    x = ["Hello", "world!"]
x = ["Hello"]
fun(x)
print(x)


def fun(x):
    x += ["world!"]
x = ["Hello"]
fun(x)
print(x)


def autor(nom:str, apel:str, f_nac:str) -> bool:
    print()

autor(apel="Frank", nom="Miller", f_nac="27/01/1957")
'''

def tupla(*a):
    print(a)
    print(type(a))

tupla(1,2,3,4)

print("\n")

def diccionario(**datos):
    print(datos)
    print(type(datos))

diccionario(nom='Manolo', apel='Cupeiro', dni=32754654)

