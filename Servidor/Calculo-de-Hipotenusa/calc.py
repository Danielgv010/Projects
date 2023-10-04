#!C:\Users\zx22student3206\AppData\Local\Programs\Python\Python311\python.exe

print("Content-type: text/html\n")

import os 
from urllib.parse import urlparse, unquote, parse_qs
import math

#Recupera las variables del sistema
ru = os.environ.get("REQUEST_URI")
parsed_url = urlparse(ru)
#Extrae los valores del form de las variables del sistema
parameters = parse_qs(parsed_url[4])

#Convierte el valor de los inputs de string a float
cat1 = float(parameters["cat1"][0])
cat2 = float(parameters["cat2"][0])

#Realiza el cálculo para obtener la hipotenusa
resultado = math.sqrt(cat1**2+cat2**2)

#Imprime el resultado en pantalla
salida = "La hipotenusa mide: {}cm"
print("<html><head/><body><h3>")
print(salida.format("%.2f" % resultado))
print("</h3></body></html>")