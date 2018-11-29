'''
from random import randint
from datetime import datetime

for i in range(0, 10):
    print(randint(-90, 90), end=' ') # Random de números enteros

print("\n")
print(datetime.now()) # Fecha y hora de sistema
'''

'''
import sys, logging

logging.basicConfig(
    filename="log.txt",
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s)") # Formato de salida como print("".format)

logging.debug("Mensaje debugeado")
logging.error("Mensaje de error")
logging.log(35, "Nivel de log inventado")
'''

