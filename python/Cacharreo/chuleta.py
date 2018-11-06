from _md5 import md5

s = "HOla que tal"
print(s)

print(s.upper())
print(s.title())
print(s.capitalize())

print("En la frase \"Donde esta Wally\" lo encontramos en la posicion:", "Dónde está Wally?".find("Wally"))

print(
    s.replace("que", "lala", 1) # Reemplaza "que" por "lala" una vez
)

print(
    "123456"[1:3], abs(-45)
)

b = float(2.65)
print(
    round(8.45 , 1) # Redondea a un decimal. 8.45,2 sería a dos decimales
)

#import hashlib
#user = input("Enter text here ")
#h = hashlib.md5(user.encode())
#h2 = h.hexdigest()
#print(h2)


print("La suma de {0} mas {1} menos {2} es {3}".format(1,3,5,(1+3-5)))

print("Una prueba de splitter".split())