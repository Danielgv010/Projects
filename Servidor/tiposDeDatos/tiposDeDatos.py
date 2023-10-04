#!C:\Users\zx22student3206\AppData\Local\Programs\Python\Python311\python.exe

print("Content-type: text/html\n")

import os
from urllib.parse import urlparse, unquote, parse_qs

ru = os.environ.get("REQUEST_URI")
parsed_url = urlparse(ru)
param = parse_qs(parsed_url[4])

dato = param["dato"][0]

equiposFutbolBuenos = "         Sporting Madrid Barsa Atletico Betis Sevilla"

if dato not in equiposFutbolBuenos:
    print(f"El equipo {dato} no es bueno")
else:
    print(f"El equipo {dato} es bueno")

#Imprime caracteres desde la posicion 10 del array hasta la 14
print(equiposFutbolBuenos[10:15]+"<br>")
#Imprime caracteres desde la posicion 0 del array hasta la 14
print(equiposFutbolBuenos[:15]+"<br>")
#Imprime caracteres desde la posicion 10 del array hasta la última
print(equiposFutbolBuenos[10:]+"<br>")
#Imprime caracteres desde la ultima posicion-5 del array hasta la última
print(equiposFutbolBuenos[-5:]+"<br>")
#Imprime el texto en mayúsculas
print(equiposFutbolBuenos.upper()+"<br>")
#Imprime el texto en minúsculas
print(equiposFutbolBuenos.lower()+"<br>")

print(equiposFutbolBuenos.strip()+"<br>")
#Cambia las a por A
print(equiposFutbolBuenos.replace("a","A")+"<br>")
#Parte el string por los espacios y lo guarda en un array
listaEquipos = equiposFutbolBuenos.split(" ")
print(listaEquipos[1])
#Devuelve true o false si coincie con el tipo de dato
print(dato.isdecimal())
print(dato.isdigit())
#Para imprimir un string con comillas
print("En un lugar de \"La mancha\"<br>")
#Para imprimir longitud de un string
print(len(equiposFutbolBuenos))
#Devuelve true
print(bool("aaaa"))
print(bool("1341"))
#Devuelve false
print(bool(""))
print(bool(0))